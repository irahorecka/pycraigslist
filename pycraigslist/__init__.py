"""
pycraigslist API library
~~~~~~~~~~~~~~~~~~~~~~~~

pycraigslist is a fast and expressive Craigslist API wrapper,
written in Python, for human beings.
"""

# fmt: off
from pycraigslist.api import (community, events, forsale, gigs,
                              housing, jobs, services, resumes)

__all__ = ["community", "events", "forsale", "gigs",
           "housing", "jobs", "services", "resumes"]
# fmt: on

__version__ = "0.6.2"
