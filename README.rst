pycraigslist
============

|PyPI version fury.io| |PyPI pyversions|

.. |PyPI version fury.io| image:: https://badge.fury.io/py/pycraigslist.svg
    :target: https://pypi.python.org/pypi/pycraigslist
.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/pycraigslist.svg
    :target: https://pypi.python.org/pypi/pycraigslist/


A fast and expressive `Craigslist <https://www.craigslist.org/about/sites>`__ API wrapper.

Disclaimer
----------

* I do not work or have an affiliation with Craigslist.
* This library is intended for educational purposes. It is not advised to crawl and download data from Craigslist.

Installation
------------

::

    pip install pycraigslist

Quick Start
-----------

Find cars & trucks for sale with keyword "Mazda Miata" in the East Bay Area, California:

.. code:: python

    import pycraigslist

    miatas = pycraigslist.forsale.cta(site="sfbay", area="eby", query="Mazda Miata")
    for miata in miatas.search():
        print(miata)

    >>> {'country': 'US',
        'region': 'CA',
        'site': 'sfbay',
        'area': 'eby',
        'category': 'cto',
        'id': '7291715564',
        'repost_of': '',
        'last_updated': '2021-03-15 09:06',
        'title': '1990 Mazda Miata',
        'neighborhood': 'oakland lake merritt / grand',
        'price': '$5,000',
        'url': 'https://sfbay.craigslist.org/eby/cto/d/oakland-1990-mazda-miata/7291715564.html'}
        # ...

Background
----------

This library is intended to be expressive and easy to use.


pycraigslist classes
********************

.. |nbsp|   unicode:: U+00A0 .. NO-BREAK SPACE

* ``pycraigslist.community`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > community)
* ``pycraigslist.events`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > event calendar)
* ``pycraigslist.forsale`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > for sale)
* ``pycraigslist.gigs`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > gigs)
* ``pycraigslist.housing`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > housing)
* ``pycraigslist.jobs`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > jobs)
* ``pycraigslist.resumes`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > resumes)
* ``pycraigslist.services`` |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > services)

We can search for posts in parent classes. For example, finding paid gigs in Portland, Oregon:

.. code:: python

    import pycraigslist

    paid_gigs = pycraigslist.gigs(site="portland", is_paid=True)
    for gig in paid_gigs.search():
        print(gig)

    >>> {'country': 'US',
        'region': 'OR',
        'site': 'portland',
        'area': 'mlt',
        'category': 'lbg',
        'id': '7295392821',
        'repost_of': '7292985211',
        'last_updated': '2021-03-22 13:00',
        'title': 'Packing and moving',
        'neighborhood': 'SE Portland',
        'price': '',
        'url': 'https://portland.craigslist.org/mlt/lbg/d/portland-packing-and-moving/7295392821.html'}
        # ...

pycraigslist subclasses
***********************

Most pycraigslist classes have subclasses to allow for categorical searches. For example:

* ``pycraigslist.forsale.bia`` |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > for sale > bikes)
* ``pycraigslist.forsale.cta`` |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > for sale > cars & trucks)
* ``pycraigslist.housing.apa`` |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > housing > apartments / housing for rent)
* ``pycraigslist.housing.roo`` |nbsp| |nbsp| |nbsp| |nbsp| (craigslist.org > housing > apartments / rooms & shares)

Finding pycraigslist subclasses
*******************************

Use class method ``.get_categories()`` to search for subclasses. The resulting keys are the subclass names.

.. code:: python

    import pycraigslist

    print(pycraigslist.housing.get_categories())

    >>> {'apa': 'apartments / housing for rent',
        'swp': 'housing swap',
        'off': 'office & commercial',
        'prk': 'parking & storage',
        'rea': 'real estate',
        'reb': 'real estate - by dealer',
        'reo': 'real estate - by owner',
        'roo': 'rooms & shares',
        'sub': 'sublets & temporary',
        'vac': 'vacation rentals',
        'hou': 'wanted: apts',
        'rew': 'wanted: real estate',
        'sha': 'wanted: room/share',
        'sbw': 'wanted: sublet/temp'}

We'd choose ``pycraigslist.housing.vac`` if we're interested in searching for vacation rentals.

Finding and using filters
*************************
We can apply filters to our search.
Use ``.get_filters()`` to find valid filters for a class or subclass instance.

.. code:: python

    import pycraigslist

    tokyo_autos = pycraigslist.forsale.cta(site="tokyo")
    print(tokyo_autos.get_filters())

    >>> {'query': '...', 'search_titles': 'True/False', 'has_image': 'True/False',
        'posted_today': 'True/False', 'bundle_duplicates': 'True/False',
        'search_distance': '...', 'zip_code': '...', 'min_price': '...', 'max_price': '...',
        'make_model': '...', 'min_year': '...', 'max_year': '...', 'min_miles': '...',
        'max_miles': '...', 'min_engine_displacement': '...', 'max_engine_displacement': '...',
        'condition': ['新品', 'ほぼ新品', '美品', '良品', '使用に問題なし', 'サルベージ'],
        'auto_cylinders': ['3気筒', '4気筒', '5気筒', '6気筒', '8気筒', '10気筒', '12気筒', 'その他'],
        'auto_drivetrain': ['前輪', '後輪', '4WD'],
        'auto_fuel_type': ['ガソリン', 'ディーゼル', 'ハイブリッド', '電気', 'その他'],
        'auto_paint': ['ブラック', 'ブルー', 'ブラウン', 'グリーン', 'グレー', 'オレンジ', 'パープル',
                       'レッド', 'シルバー', 'ホワイト', 'イエロー', 'カスタム'],
        'auto_size': ['コンパクト', 'フルサイズ', '中型', 'サブコンパクト'],
        'auto_title_status': ['クリーン', 'サルベージ', '再生', '部品のみ', '先取特権', '不明'],
        'auto_transmission': ['MT', 'AT', 'その他'],
        'auto_bodytype': ['バス', 'コンバーチブル', 'クーペ', 'ハッチバック', 'ミニバン', 'オフロード',
                          'ピックアップ', 'セダン', 'トラック', 'SUV', 'ワゴン', 'バン', 'その他'],
        'language': ['afrikaans', 'català', 'dansk', 'deutsch', 'english', 'español', 'suomi',
                     'français', 'italiano', 'nederlands', 'norsk', 'português', 'svenska',
                     'filipino', 'türkçe', '中文', 'العربية', '日本語', '한국말', 'русский',
                     'tiếng việt']}

Using this information, we can find cars & trucks with clean (クリーン) titles in Tokyo, Japan:

.. code:: python

    import pycraigslist

    tokyo_autos = pycraigslist.forsale.cta(site="tokyo", auto_title_status="クリーン")
    for auto in tokyo_autos.search():
        print(auto)

    >>> {'country': 'JP',
        'region': '',
        'site': 'tokyo',
        'area': '',
        'category': 'cto',
        'id': '7301105503',
        'repost_of': '',
        'last_updated': '2021-04-03 14:04',
        'title': 'Suzuki Jimny 660 XG 4WD Keyless Entry Aluminum Wheel Non-Smoking Car',
        'neighborhood': 'Chiba Ken, Noda shi, Funakata 1630-1',
        'price': '¥650,000',
        'url': 'https://tokyo.craigslist.org/cto/d/suzuki-jimny-660-xg-4wd-keyless-entry/7301105503.html'}
        # ...

When applying many filters, pass a dictionary of filters into the ``filters`` keyword parameter.
Note: keyword argument filters will override ``filters`` if there are conflicting keys. For example:

.. code:: python

    import pycraigslist

    bike_filters = {
        "bicycle_frame_material": "steel",
        # array of filter values are accepted
        "bicycle_wheel_size": ["650C", "700C"],
        "bicycle_type": "road",
    }
    # we'd still get titanium road bikes with size 650C or 700C wheels
    titanium_bikes = pycraigslist.forsale.bia(
        site="sfbay", area="sfc", bicycle_frame_material="titanium", filters=bike_filters
    )

Searching for posts
-------------------

General search
**************

To search for Craigslist posts, use ``.search()``.
``.search()`` will return a dictionary of post attributes (type ``str``) and will search for every post by default.
Use the ``limit`` keyword parameter to add a stop limit to a query. For example, use ``limit=50`` to get 50 posts.
There is a maximum of 3000 posts per query.

Find the first 20 posts for farming and gardening services in Denver, Colorado:

.. code:: python

    import pycraigslist

    gardening_services = pycraigslist.services.fgs(site="denver")
    for service in gardening_services.search(limit=20):
        print(service)

    >>> {'country': 'US',
        'region': 'CO',
        'site': 'denver',
        'area': '',
        'category': 'fgs',
        'id': '7301324564',
        'repost_of': '6974119634',
        'last_updated': '2021-04-03 11:47',
        'title': '🌲 Tree Removal/Trimming, Stump Grind: LICENSED/INSURED! 720-605-1584',
        'neighborhood': 'All Areas',
        'price': '',
        'url': 'https://denver.craigslist.org/fgs/d/littleton-tree-removal-trimming-stump/7301324564.html'}
        # ...

Detailed search
***************

Use ``.search_detail()`` to get detailed Craigslist posts.
The ``limit`` keyword parameter in ``.search`` also applies to ``.search_detail``.
Set ``include_body=True`` to include the post's body in the output. By default, ``include_body=False``.
Disclaimer: ``.search_detail`` is more time consuming than ``.search``.

Get detailed posts with the post body for all cars & trucks for sale in Abilene, Texas:

.. code:: python

    import pycraigslist

    all_autos = pycraigslist.forsale.cta(site="abilene")
    for auto in all_autos.search_detail(include_body=True):
        print(auto)

    >>> {'country': 'US',
        'region': 'TX',
        'site': 'abilene',
        'area': '',
        'category': 'cto',
        'id': '7309894792',
        'repost_of': '',
        'last_updated': '2021-04-20 12:17',
        'title': '2009 Mercedes GL-320',
        'neighborhood': 'Brownwood',
        'price': '$12,000',
        'url': 'https://abilene.craigslist.org/cto/d/brownwood-2009-mercedes-gl-320/7309894792.html',
        'lat': '31.729000',
        'lon': '-99.019000',
        'address': '',
        'misc': ['2009 mercedes-benz gl-class'],
        'condition': 'excellent',
        'drive': 'fwd',
        'fuel': 'diesel',
        'odometer': '100700',
        'paint_color': 'black',
        'title_status': 'clean',
        'transmission': 'automatic',
        'body': 'BEAUTIFUL car inside and out!! Diesel with only 100k, mechanic says its in great condition.'}
        # ...

Additional attributes
---------------------

* ``__doc__``: Gets category name.
* ``url``: Gets full URL.
* ``count``: Gets number of posts.

.. code:: python

    import pycraigslist

    east_bay_apa = pycraigslist.housing.apa(site="sfbay", area="eby", max_price=800)

    # 1
    print(east_bay_apa.__doc__)
    >>> 'apartments / housing for rent'

    # 2
    print(east_bay_apa.url)
    >>> 'https://sfbay.craigslist.org/search/eby/apa?searchNearby=1&s=0&max_price=800'

    # 3
    print(east_bay_apa.count)
    >>> 56

Exceptions
----------

pycraigslist has the following exceptions:

* ``MaximumRequestsError`` : exceeds maximum retries for a query

To use pycraigslist exceptions, import / import from ``pycraigslist.exceptions``. For example:

.. code:: python

    import pycraigslist
    from pycraigslist.exceptions import MaximumRequestsError

    try:
        sf_bikes = pycraigslist.forsale.bia(site="sfbay", area="sfc", min_price=50)
        for bike in sf_bikes.search():
            print(bike)
    except MaximumRequestsError:
        print("Yikes! Something's up with the network.")

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
