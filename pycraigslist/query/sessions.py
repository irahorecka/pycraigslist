import time
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0"


def get_html(*args, **kwargs):
    """ Gets HTML document from requests content. """
    content = get_request(*args, **kwargs).content
    return BeautifulSoup(content, "html.parser")


def get_request(*args, max_retry=10, **kwargs):
    """ Gets requests.models.Response object using requests.get.
    Retry request if request fails, with number of iteration specified
    by max_retry. """
    kwargs.setdefault("headers", {}).setdefault("User-Agent", USER_AGENT)

    def recurse_get_request(*args, retries=0, wait=0.005, **kwargs):
        try:
            return requests.get(*args, **kwargs)
        except RequestException as exc:
            if retries > max_retry:
                raise RequestException from exc

            print("Request failed: (%s). Retrying after %s seconds ..." % (exc, "%.2f" % wait))
            time.sleep(wait)
            # double the wait time after every iteration
            wait *= 2
            retries += 1
            return recurse_get_request(*args, retries=retries, wait=wait, **kwargs)

    return recurse_get_request(*args, **kwargs)
