""" A simple and expressive Craigslist API wrapper. """

# fmt: off
from .api import (community, events, forsale, gigs,
                  housing, jobs, services, resumes)

__all__ = ["community", "events", "forsale", "gigs",
           "housing", "jobs", "services", "resumes"]
# fmt: on

__version__ = "0.3.4"
