import concurrent.futures
import tenacity
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from .exceptions import MaximumRequestsError

USER_AGENT = "Mozilla/5.0"
# Retry 10 times, starting with 0.01 second and doubling the delay every time
_RETRY_ARGS = {
    "wait": tenacity.wait.wait_random_exponential(multiplier=0.01, exp_base=2),
    "stop": tenacity.stop.stop_after_attempt(8),
}


def yield_html(url, threaded=False, **kwargs):
    """Yields HTML documents from requests content with asynchronous
    option."""
    # if not threaded, url is a list of strings, else a string
    bs4 = lambda content: BeautifulSoup(content, "html.parser")
    try:
        if threaded not in (True, 1):
            yield bs4(get_request(url).content)
        else:
            yield from (bs4(response.content) for response in thread_get_request(url, **kwargs))
    except tenacity.RetryError:
        raise MaximumRequestsError("Maximum requests attempted - check network connection.")


@tenacity.retry(**_RETRY_ARGS)
def get_request(url, params={}):
    """Gets requests.models.Response object using requests.get.
    Retry request if request fails, with number of attepmpts and
    wait time specified in _RETRY_ARGS."""
    params.setdefault("headers", {}).setdefault("User-Agent", USER_AGENT)
    return requests.get(url, params=params, timeout=5)


def thread_get_request(urls, **kwargs):
    """Creates thread pool to asyhchronously execute get requests."""
    # params is a list of URL parameters
    params = kwargs["params"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {
            executor.submit(lambda p: get_request(*p), (url, params[idx]))
            for idx, url in enumerate(urls)
        }
        for future in concurrent.futures.as_completed(future_to_url):
            yield future.result()
