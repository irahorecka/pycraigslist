"""
pycraigslist.tests.specs.static
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stores static information for testing.
"""

import pycraigslist


class content:
    """Suite of post content templates expected from search and search_detail methods."""

    # Attributes that are guaranteed to exist in standard posts.
    post_content_std = {
        "country": "",
        "region": "",
        "site": "",
        "area": "",
        "category": "",
        "id": "",
        "repost_of": "",
        "last_updated": "",
        "title": "",
        "neighborhood": "",
        "price": "",
        "url": "",
    }

    # Attributes that are guaranteed to exist in detailed posts WITHOUT body.
    post_content_detail = {
        "country": "",
        "region": "",
        "site": "",
        "area": "",
        "category": "",
        "id": "",
        "repost_of": "",
        "last_updated": "",
        "title": "",
        "neighborhood": "",
        "price": "",
        "url": "",
        "lat": "",
        "lon": "",
        "address": "",
        "misc": [],
    }

    # Attributes that are guaranteed to exist in detailed posts WITH body.
    post_content_detail_body = {
        "country": "",
        "region": "",
        "site": "",
        "area": "",
        "category": "",
        "id": "",
        "repost_of": "",
        "last_updated": "",
        "title": "",
        "neighborhood": "",
        "price": "",
        "url": "",
        "lat": "",
        "lon": "",
        "address": "",
        "misc": [],
        "body": "",
    }


class filters:
    """Suite of filters (organized by category) for the `filters` parameter in
    pycraigslist classes."""

    community = (
        {
            "query": "community",
            "posted_today": 1,
        },
        {
            "posted_today": False,
            "bundle_duplicates": 0,
        },
        {
            "search_distance": 10,
            "zip_code": 94538,
        },
    )

    events = (
        {
            "has_image": 1,
            "bundle_duplicates": 1,
        },
        {
            "query": "food",
        },
        {
            "music": 1,
        },
    )

    forsale = (
        {
            "make_model": "toyota",
            "min_price": 3000,
        },
        {
            "min_price": 1000,
            "max_price": 5000,
            "bundle_duplicates": True,
        },
        {
            "zip_code": 94536,
            "has_image": 1,
        },
    )

    gigs = (
        {
            "query": "gardening",
            "posted_today": 1,
            "search_titles": True,
        },
        {
            "search_titles": True,
            "bundle_duplicates": 1,
            "posted_today": 0,
        },
        {
            "has_image": True,
            "posted_today": 0,
            "is_paid": True,
        },
    )

    housing = (
        {
            "min_bedrooms": 1,
            "max_price": 2000,
            "cats_ok": 1,
        },
        {
            "max_price": 1000,
            "dogs_ok": True,
            "has_image": True,
        },
        {
            "min_price": 1200,
            "parking": ["carport", "street parking"],
            "posted_today": True,
        },
    )

    jobs = (
        {
            "query": "software",
            "posted_today": 1,
            "employment_type": ["full-time", "contract"],
        },
        {
            "is_internship": True,
            "posted_today": 0,
        },
        {
            "search_titles": True,
            "bundle_duplicates": 1,
            "query": "restaurant food",
            "employment_type": "part-time",
        },
    )

    resumes = (
        {
            "query": "business",
            "education_level_completed": "high school/GED",
        },
        {
            "has_image": 1,
            "zip_code": 94538,
            "search_distance": 30,
        },
        {
            "posted_today": 1,
            "bundle_duplicates": 1,
        },
    )

    services = (
        {
            "query": "gardening",
            "has_image": True,
        },
        {
            "zip_code": 95060,
            "search_distance": 40,
            "bundle_duplicates": 1,
            "query": "car",
        },
        {
            "has_image": 1,
            "posted_today": 0,
            "bundle_duplicates": 1,
        },
    )

    all_ = (community, events, forsale, gigs, housing, jobs, resumes, services)


class kwargs:
    """Suite of keyword arguments to test intantiation of pycraigslist.api.* object."""

    valid = (
        {"site": "monterey"},
        {"site": "sfbay", "area": "eby"},
        # Use a filter query that is applicable to all queries.
        {"site": "sandiego", "area": "csd", "has_image": True},
        {"site": "sandiego", "area": "csd", "filters": {"has_image": True}},
    )
    invalid = (
        # Invalid site and area
        {"site": "bad_site"},
        {"site": "sfbay", "area": "bad_area"},
        # Invalid filter keys
        {"site": "sandiego", "area": "esd", "bad_filter": "bad_value"},
        {"site": "sandiego", "area": "esd", "filters": {"bad_filter": "bad_value"}},
    )


class limits:
    """Suite of limits for the `limit` parameter in .search and .search_detail methods."""

    std = (2983, 1121, 38, 1928)
    std_fringe = (1, 120, 121, 240, 241)
    detail = (83, 125, 3, 34)
    detail_fringe = (1, 120, 121, 240, 241)


class obj:
    """Suite of pycraigslist objects."""

    pycraigslist_parents = [
        pycraigslist.community,
        pycraigslist.events,
        pycraigslist.forsale,
        pycraigslist.gigs,
        pycraigslist.housing,
        pycraigslist.jobs,
        pycraigslist.resumes,
        pycraigslist.services,
    ]
