pycraigslist
============

A simple and expressive `Craigslist <https://www.craigslist.org/about/sites>`__ API wrapper.

Disclaimer
----------

* I do not work or have an affiliation with Craigslist.
* This library is intended for educational purposes. It is not advised to crawl and download data from Craigslist.

Installation
------------

::

    pip install pycraigslist

Jump Start
----------

Let's find cars & trucks in the East Bay Area, California that are silver and have less than 60,000 miles:

.. code:: python

    import pycraigslist

    silver_autos = pycraigslist.forsale.cta(
        site="sfbay", area="eby", auto_paint="silver", max_miles=60000
    )
    for auto in silver_autos.search():
        print(auto)

    >>> {'area': 'eby',
        'category': 'cto',
        'id': '7298808707',
        'last_updated': '2021-03-29 10:24',
        'neighborhood': 'concord / pleasant hill / martinez',
        'price': '$5,000',
        'repost_of': None,
        'site': 'sfbay',
        'title': '2001 Ford Ranger XLT',
        'url': 'https://sfbay.craigslist.org/eby/cto/d/oakland-2001-ford-ranger-xlt/7298808707.html'}
        # ...    

Background
----------

This library is intended to be expressive and easy to use.


pycraigslist classes
********************

.. |nbsp|   unicode:: U+00A0 .. NO-BREAK SPACE

* ``pycraigslist.community`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > community)
* ``pycraigslist.events`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > event calendar)
* ``pycraigslist.community`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > community)
* ``pycraigslist.events`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > event calendar)
* ``pycraigslist.forsale`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > for sale)
* ``pycraigslist.gigs`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > gigs)
* ``pycraigslist.housing`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > housing)
* ``pycraigslist.jobs`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > jobs)
* ``pycraigslist.services`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > services)
* ``pycraigslist.resumes`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > resumes)

pycraigslist subclasses
***********************

Most pycraigslist classes have subclasses to allow for categorical searches. For example:

* ``pycraigslist.forsale.bia`` |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > for sale > bikes)
* ``pycraigslist.forsale.cta`` |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > for sale > cars & trucks)
* ``pycraigslist.housing.apa`` |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > housing > apartments / housing for rent)
* ``pycraigslist.housing.roo`` |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > housing > apartments / rooms & shares)

Finding pycraigslist subclasses
*******************************

To search for subclasses, use ``.get_categories()``. The resulting keys are the subclass names.

.. code:: python

    import pycraigslist

    print(pycraigslist.housing.get_categories())

    >>> {'apa': 'apartments / housing for rent',
        'swp': 'housing swap',
        'off': 'office & commercial',
        'prk': 'parking & storage',
        'rea': 'real estate',
        'roo': 'rooms & shares',
        'sub': 'sublets & temporary',
        'vac': 'vacation rentals',
        'hou': 'wanted: apts',
        'rew': 'wanted: real estate',
        'sha': 'wanted: room/share',
        'sbw': 'wanted: sublet/temp'}

For example, if I'm interested in searching for vacation rentals, I'd use the subclass ``pycraigslist.housing.vac``.

Finding and using filters
*************************
As demonstrated in the jump-start example, we can pass filters when constructing our Craigslist search.
To find valid filters for a class or subclass, use ``.get_filters()``.

.. code:: python

    import pycraigslist

    print(pycraigslist.housing.apa.get_filters())

    >>> {'query': '...', 'search_titles': 'True/False', 'has_image': 'True/False',
        'posted_today': 'True/False', 'bundle_duplicates': 'True/False', 'search_distance': '...',
        'zip_code': '...', 'min_price': '...', 'max_price': '...',
        'min_bedrooms': '...', 'max_bedrooms': '...', 'min_bathrooms': '...',
        'max_bathrooms': '...', 'min_ft2': '...', 'max_ft2': '...',
        'private_room': 'True/False', 'private_bath': 'True/False', 'cats_ok': 'True/False',
        'dogs_ok': 'True/False', 'is_furnished': 'True/False', 'no_smoking': 'True/False',
        'wheelchair_acccess': 'True/False', 'ev_charging': 'True/False', 'no_application_fee': 'True/False',
        'no_broker_fee': 'True/False',
        'housing_type': ['apartment', 'condo', 'cottage/cabin', 'duplex', 'flat',
                         'house', 'in-law', 'loft', 'townhouse', 'manufactured',
                         'assisted living', 'land'],
        'laundry': ['w/d in unit', 'w/d hookups', 'laundry in bldg', 'laundry on site', 'no laundry on site'],
        'parking': ['carport', 'attached garage', 'detached garage', 'off-street parking', 'street parking',
                    'valet parking', 'no parking']}

Using this information, let's search for apartments / housing for rent in Eugene, Oregon that have at least 1 bedroom and a carport.

.. code:: python

    import pycraigslist

    one_bedrooms = pycraigslist.housing.apa(site="eugene", min_bedrooms=1, parking="carport")
    for room in one_bedrooms.search():
        print(room)

    >>> {'area': '',
        'area-ft2': 1000,
        'bedrooms': 2,
        'category': 'apa',
        'id': '7267556874',
        'last_updated': '2021-02-24 08:55',
        'neighborhood': 'Eugene',
        'price': '$1,550',
        'repost_of': None,
        'site': 'eugene',
        'title': 'High End, Spacious Top Floor Two Bedroom!',
        'url': 'https://eugene.craigslist.org/apa/d/springfield-high-end-spacious-top-floor/7267556874.html'}
        # ...

If we want to apply a bunch of filters, pass a dictionary of filters into the ``filters`` keyword parameter.
Note: keyword argument filters will override ``filters`` if there are conflicting keys. For example:

.. code:: python

    import pycraigslist

    bike_filters = {
    "bicycle_frame_material": "steel",
    "bicycle_wheel_size": "700C",
    "bicycle_type": "road",
    }
    # we'd still get titanium bikes
    titanium_bikes = pycraigslist.forsale.bia(
        site="sfbay", area="sfc", bicycle_frame_material="titanium", filters=bike_filters
    )

    # Although we have a conflicting filter (i.e. bicycle_frame_material), the bicycle_frame_material
    # keyword argument will take precedence over bicycle_frame_material in bike_filters.
    # Therefore, we'd still search for titanium road bikes with size 700C wheels.

Searching for posts
*******************

To search for Craigslist posts, use the ``.search()`` method. ``.search()`` will get every post by default. 
Use the ``limit`` keyword parameter to add a stop limit to your query. For example, use ``limit=50`` if you want 50 posts.
There is a maximum of 3000 posts per query.


Let's find the first 20 posts for farming and gardening services in Denver, Colorado.

.. code:: python
    
    import pycraigslist

    gardening_services = pycraigslist.services.fgs(site="denver")
    for service in gardening_services.search(limit=20):
        print(service)

    >>> {'area': '',
        'category': 'fgs',
        'id': '7298949409',
        'last_updated': '2021-03-29 15:15',
        'neighborhood': 'all areas',
        'price': '',
        'repost_of': None,
        'site': 'denver',
        'title': '🌲Mendez tree removal tree trimming stump grinding fully insured 🌲',
        'url': 'https://denver.craigslist.org/fgs/d/aurora-mendez-tree-removal-tree/7298949409.html'}
        # ...

Contribute
----------

- `Issue Tracker <https://github.com/irahorecka/pycraigslist/issues>`__
- `Source Code <https://github.com/irahorecka/pycraigslist/tree/master/pycraigslist>`__

Support
-------

If you are having issues or would like to propose a new feature, please use the `issues tracker <https://github.com/irahorecka/pycraigslist/issues>`__.

License
-------

The project is licensed under the MIT license.
