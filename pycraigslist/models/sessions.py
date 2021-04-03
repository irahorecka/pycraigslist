import concurrent.futures
import tenacity
import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0"
# Retry 10 times, starting with 0.01 second and doubling the delay every time
_RETRY_ARGS = {
    "wait": tenacity.wait.wait_random_exponential(multiplier=0.01, exp_base=2),
    "stop": tenacity.stop.stop_after_attempt(12),
}


class MaximumRequestsError(Exception):
    """Exceed maximum get requests."""


def yield_html(url, **kwargs):
    """Yield HTML doc(s) to caller."""
    try:
        # single request: a url string
        if isinstance(url, str):
            yield get_html(get_request(url, **parse_kwargs(kwargs)).content)
        # single request: a single url in a list or tuple
        elif isinstance(url, (list, tuple)) and len(url) == 1:
            yield get_html(get_request(url[0], **parse_kwargs(kwargs)).content)
        # multiple requests
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
    """Get HTML document from response content."""
    return BeautifulSoup(content, "html.parser")


@tenacity.retry(**_RETRY_ARGS)
def get_request(url, params=None):
    """Gets requests.models.Response object using requests.get.
    Retry request if request fails, with number of attepmpts and
    wait time specified in _RETRY_ARGS."""
    params = {} if params is None else params
    params.setdefault("headers", {}).setdefault("User-Agent", USER_AGENT)
    return requests.get(url, params=params, timeout=5)


def threaded_get_request(urls, **kwargs):
    """Yields requests from get_request concurrently."""
    yield from iter(
        concurrency(
            concurrent.futures.ThreadPoolExecutor, lambda args: get_request(*args), urls, **kwargs
        )
    )


def concurrency(PoolExecutor, map_func, *args, **kwargs):
    """General concurrency procedure to submit map-able
    functions to arguments."""
    # this procedure is designed to handle process pools and thread pools
    zipped_args = zip(*args, *kwargs.values())
    with PoolExecutor(max_workers=5) as executor:
        futures = {
            # func must accept all positional arguments
            executor.submit(map_func, arg_tuple)
            for arg_tuple in zipped_args
        }
        for future in concurrent.futures.as_completed(futures):
            yield future.result()


def parse_kwargs(kwargs):
    """Remove first kwarg value from list or tuple wrapper if wrapped and
    is len of 1."""
    for key, value in kwargs.copy().items():
        if isinstance(value, (list, tuple)) and len(value) == 1:
            kwargs[key] = value[0]
    return kwargs
