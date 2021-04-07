"""
pycraigslist.models.sessions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Handles requests and constructs BeautifulSoup objects.
"""

import concurrent.futures
import tenacity
import requests
from bs4 import BeautifulSoup

HEADERS = {"headers": {"User-Agent": "Mozilla/5.0"}}
# Retry 10 times, starting with 0.01 second and doubling the delay every time
_RETRY_ARGS = {
    "wait": tenacity.wait.wait_random_exponential(multiplier=0.01, exp_base=2),
    "stop": tenacity.stop.stop_after_attempt(12),
}


class MaximumRequestsError(Exception):
    """Exceeds maximum get requests."""


def yield_html(url, **kwargs):
    """Yields HTML content(s) to caller."""
    try:
        # Single request: a url string
        if isinstance(url, str):
            yield get_html(get_request(url, **parse_kwargs(kwargs)).content)
        # Single request: a single url in a list or tuple
        elif isinstance(url, (list, tuple)) and len(url) == 1:
            yield get_html(get_request(url[0], **parse_kwargs(kwargs)).content)
        # Multiple requests
        else:
            yield from map(
                get_html,
                (
                    response.content
                    for response in threaded_get_request(url, **parse_kwargs(kwargs))
                ),
            )
    except tenacity.RetryError:
        raise MaximumRequestsError("Maximum requests attempted - check network connection.")


def get_html(content):
    """Gets bs4.BeautifulSoup object from response content."""
    return BeautifulSoup(content, "html.parser")


@tenacity.retry(**_RETRY_ARGS)
def get_request(url, params=None):
    """Gets requests.models.Response object using requests.get.
    Retry request if request fails, with number of attempts and
    wait time specified in _RETRY_ARGS."""
    if params is None:
        params = HEADERS
    # Don't add headers if params is {}
    elif params != {}:
        params.update(HEADERS)

    return requests.get(url, params=params, timeout=5)


def threaded_get_request(urls, **kwargs):
    """Yields requests from get_request concurrently."""
    yield from iter(
        concurrency(
            concurrent.futures.ThreadPoolExecutor, lambda args: get_request(*args), urls, **kwargs
        )
    )


def concurrency(PoolExecutor, map_func, *args, **kwargs):
    """General concurrency procedure for thread pools and process
    pools that submits map-able functions to arguments."""
    # Zip args and kwarg values to make tuple of args
    zipped_args = zip(*args, *kwargs.values())
    with PoolExecutor(max_workers=5) as executor:
        futures = {
            # Func must accept all positional arguments (kwargs assumed by args OK)
            executor.submit(map_func, arg_tuple)
            for arg_tuple in zipped_args
        }
        for future in concurrent.futures.as_completed(futures):
            yield future.result()


def parse_kwargs(kwargs):
    """Removes first kwarg value from list or tuple wrapper if wrapped and
    is the only value."""
    for key, value in kwargs.copy().items():
        if isinstance(value, (list, tuple)) and len(value) == 1:
            kwargs[key] = value[0]
    return kwargs
