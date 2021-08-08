"""
pycraigslist.filters
~~~~~~~~~~~~~~~~~~~~

Stores Craigslist query filters and categories.
"""


class query:
    """Store query filters by broad category."""

    base = {
        "query": {"url_key": "query", "value": None},
        "search_titles": {"url_key": "srchType", "value": "T"},
        "has_image": {"url_key": "hasPic", "value": 1},
        "posted_today": {"url_key": "postedToday", "value": 1},
        "bundle_duplicates": {"url_key": "bundleDuplicates", "value": 1},
        "search_distance": {"url_key": "search_distance", "value": None},
        "zip_code": {"url_key": "postal", "value": None},
    }

    community = {
        **base,
        **{
            # No unique filters for community.
        },
    }

    events = {
        **base,
        **{
            # art/film
            "art": {"url_key": "event_art", "value": 1, "attr": "art/film"},
            "film": {"url_key": "event_art", "value": 1, "attr": "art/film"},
            # career
            "career": {"url_key": "event_career", "value": 1, "attr": "career"},
            # charitable
            "charitable": {"url_key": "event_fundraiser_vol", "value": 1, "attr": "charitable"},
            "fundraiser": {"url_key": "event_fundraiser_vol", "value": 1, "attr": "charitable"},
            # competiton
            "athletics": {"url_key": "event_athletics", "value": 1, "attr": "competition"},
            "competition": {"url_key": "event_athletics", "value": 1, "attr": "competition"},
            # dance
            "dance": {"url_key": "event_dance", "value": 1, "attr": "dance"},
            # fest/fair
            "festival": {"url_key": "event_festival", "value": 1, "attr": "fest/fair"},
            "fair": {"url_key": "event_festival", "value": 1, "attr": "fest/fair"},
            # fitness/health
            "fitness": {"url_key": "event_fitness_wellness", "value": 1, "attr": "fitness/health"},
            "health": {"url_key": "event_fitness_wellness", "value": 1, "attr": "fitness/health"},
            # food/drink
            "food": {"url_key": "event_food", "value": 1, "attr": "food/drink"},
            "drink": {"url_key": "event_food", "value": 1, "attr": "food/drink"},
            # free
            "free": {"url_key": "event_free", "value": 1, "attr": "free"},
            # kid friendly
            "kid_friendly": {"url_key": "event_kidfriendly", "value": 1, "attr": "kid friendly"},
            # literary
            "literary": {"url_key": "event_literary", "value": 1, "attr": "literary"},
            # music
            "music": {"url_key": "event_music", "value": 1, "attr": "music"},
            # outdoor
            "outdoor": {"url_key": "event_outdoor", "value": 1, "attr": "outdoor"},
            # sale
            "sale": {"url_key": "event_sale", "value": 1, "attr": "sale"},
            # singles
            "singles": {"url_key": "event_singles", "value": 1, "attr": "singles"},
            # tech
            "tech": {"url_key": "event_geek", "value": 1, "attr": "tech"},
        },
    }

    forsale = {
        **base,
        **{
            # price
            "min_price": {"url_key": "min_price", "value": None},
            "max_price": {"url_key": "max_price", "value": None},
            # make and model
            "make_model": {"url_key": "auto_make_model", "value": None},
            "min_year": {"url_key": "min_auto_year", "value": None},
            "max_year": {"url_key": "max_auto_year", "value": None},
            # odometer
            "min_miles": {"url_key": "min_auto_miles", "value": None},
            "max_miles": {"url_key": "max_auto_miles", "value": None},
            # engine displacement (cc)
            "min_engine_displacement": {"url_key": "min_engine_displacement_cc", "value": None},
            "max_engine_displacement": {"url_key": "max_engine_displacement_cc", "value": None},
        },
    }

    gigs = {
        **base,
        **{
            # paid/unpaid
            "is_paid": {"url_key": "is_paid", "value": 1},
        },
    }

    housing = {
        **base,
        **{
            # price
            "min_price": {"url_key": "min_price", "value": None},
            "max_price": {"url_key": "max_price", "value": None},
            # bedrooms
            "min_bedrooms": {"url_key": "min_bedrooms", "value": None},
            "max_bedrooms": {"url_key": "max_bedrooms", "value": None},
            # bathrooms
            "min_bathrooms": {"url_key": "min_bathrooms", "value": None},
            "max_bathrooms": {"url_key": "max_bathrooms", "value": None},
            # ft2
            "min_ft2": {"url_key": "minSqft", "value": None},
            "max_ft2": {"url_key": "maxSqft", "value": None},
            # private room
            "private_room": {"url_key": "private_room", "value": 1, "attr": "private room"},
            # private bath
            "private_bath": {"url_key": "private_bath", "value": 1, "attr": "private bath"},
            # cats ok
            "cats_ok": {"url_key": "pets_cat", "value": 1, "attr": "cats are ok - purrr"},
            # dogs ok
            "dogs_ok": {"url_key": "pets_dog", "value": 1, "attr": "dogs are ok - wooof"},
            # furnished
            "is_furnished": {"url_key": "is_furnished", "value": 1, "attr": "furnished"},
            # no smoking
            "no_smoking": {"url_key": "no_smoking", "value": 1, "attr": "no smoking"},
            # wheelchair access
            "wheelchair_acccess": {
                "url_key": "wheelchaccess",
                "value": 1,
                "attr": "wheelchair accessible",
            },
            # EV charging
            "ev_charging": {"url_key": "ev_charging", "value": 1, "attr": "ev charging"},
            # no appliation fee
            "no_application_fee": {"url_key": "application_fee", "value": 1},
            # no broker fee
            "no_broker_fee": {"url_key": "broker_fee", "value": 1},
        },
    }

    jobs = {
        **base,
        **{
            # internship
            "is_internship": {"url_key": "is_internship", "value": 1, "attr": "internship"},
            # non-profit
            "is_nonprofit": {
                "url_key": "is_nonprofit",
                "value": 1,
                "attr": "non-profit organization",
            },
            # telecommute
            "is_telecommuting": {
                "url_key": "is_telecommuting",
                "value": 1,
                "attr": "telecommuting okay",
            },
        },
    }

    resumes = {
        **base,
        **{
            # TODO: Please create an issue or PR if interested in this category.
        },
    }

    services = {
        **base,
        **{
            # No unique filters for services.
        },
    }


class category:
    """Store niche category keys and descriptions within broad category."""

    @classmethod
    def get(cls, key):
        """Gets niche categories from broad category key."""
        index_table = {
            "community": cls.community,
            "events": cls.events,
            "forsale": cls.forsale,
            "gigs": cls.gigs,
            "housing": cls.housing,
            "jobs": cls.jobs,
            "resumes": cls.resumes,
            "services": cls.services,
        }
        return index_table[key]

    community = {
        "act": "activity partners",
        "ats": "artists",
        "kid": "childcare",
        "com": "general community",
        "grp": "groups",
        "vnn": "local news and views",
        "laf": "lost & found",
        "mis": "missed connections",
        "muc": "musicians",
        "pet": "pets",
        "pol": "politics",
        "rnr": "rants & raves",
        "rid": "rideshare",
        "vol": "volunteers",
    }

    events = {}

    forsale = {
        "ata": "antiques",
        "ppa": "appliances",
        "ppd": "appliances - by dealer",
        "app": "appliances - by owner",
        "ara": "arts & crafts",
        "ard": "arts & crafts - by dealer",
        "art": "arts & crafts - by owner",
        "sna": "atvs, utvs, snowmobiles",
        "snd": "atvs, utvs, snowmobiles - by dealer",
        "snw": "atvs, utvs, snowmobiles - by owner",
        "pta": "auto parts",
        "ptd": "auto parts - by dealer",
        "pts": "auto parts - by owner",
        "wta": "auto wheels & tires",
        "wtd": "auto wheels & tires - by dealer",
        "wto": "auto wheels & tires - by owner",
        "ava": "aviation",
        "avd": "aviation - by dealer",
        "avo": "aviation - by owner",
        "baa": "baby & kid stuff",
        "bad": "baby & kid stuff - by dealer",
        "bab": "baby & kid stuff - by owner",
        "bar": "barter",
        "bip": "bicycle parts",
        "bdp": "bicycle parts - by dealer",
        "bop": "bicycle parts - by owner",
        "bia": "bicycles",
        "bid": "bicycles - by dealer",
        "bik": "bicycles - by owner",
        "bpa": "boat parts & accessories",
        "bpd": "boat parts & accessories - by dealer",
        "bpo": "boat parts & accessories - by owner",
        "boo": "boats",
        "bod": "boats - by dealer",
        "boa": "boats - by owner",
        "bka": "books & magazines",
        "bkd": "books & magazines - by dealer",
        "bks": "books & magazines - by owner",
        "bfa": "business",
        "bfd": "business - by dealer",
        "bfs": "business - by owner",
        "cta": "cars & trucks",
        "ctd": "cars & trucks - by dealer",
        "cto": "cars & trucks - by owner",
        "ema": "cds / dvds / vhs",
        "emq": "cds / dvds / vhs - by dealer",
        "emd": "cds / dvds / vhs - by owner",
        "moa": "cell phones",
        "mod": "cell phones - by dealer",
        "mob": "cell phones - by owner",
        "cla": "clothing & accessories",
        "cld": "clothing & accessories - by dealer",
        "clo": "clothing & accessories - by owner",
        "cba": "collectibles",
        "cbd": "collectibles - by dealer",
        "clt": "collectibles - by owner",
        "syp": "computer parts",
        "sdp": "computer parts - by dealer",
        "sop": "computer parts - by owner",
        "sya": "computers",
        "syd": "computers - by dealer",
        "sys": "computers - by owner",
        "ela": "electronics",
        "eld": "electronics - by dealer",
        "ele": "electronics - by owner",
        "gra": "farm & garden",
        "zip": "free stuff",
        "fua": "furniture",
        "gms": "garage & moving sales",
        "foa": "general for sale",
        "fod": "general for sale - by dealer",
        "fur": "general for sale - by owner",
        "haa": "health and beauty",
        "had": "health and beauty - by dealer",
        "hab": "health and beauty - by owner",
        "hva": "heavy equipment",
        "hvd": "heavy equipment - by dealer",
        "hvo": "heavy equipment - by owner",
        "hsa": "household items",
        "hsd": "household items - by dealer",
        "hsh": "household items - by owner",
        "jwa": "jewelry",
        "jwd": "jewelry - by dealer",
        "jwl": "jewelry - by owner",
        "maa": "materials",
        "mad": "materials - by dealer",
        "mat": "materials - by owner",
        "mpa": "motorcycle parts & accessories",
        "mpd": "motorcycle parts & accessories - by dealer",
        "mpo": "motorcycle parts & accessories - by owner",
        "mca": "motorcycles/scooters",
        "mcd": "motorcycles/scooters - by dealer",
        "mcy": "motorcycles/scooters - by owner",
        "msa": "musical instruments",
        "msd": "musical instruments - by dealer",
        "msg": "musical instruments - by owner",
        "pha": "photo/video",
        "phd": "photo/video - by dealer",
        "pho": "photo/video - by owner",
        "rva": "recreational vehicles",
        "rvd": "recreational vehicles - by dealer",
        "rvs": "recreational vehicles - by owner",
        "sga": "sporting goods",
        "sgd": "sporting goods - by dealer",
        "spo": "sporting goods - by owner",
        "tia": "tickets",
        "tid": "tickets - by dealer",
        "tix": "tickets - by owner",
        "tla": "tools",
        "taa": "toys & games",
        "tad": "toys & games - by dealer",
        "tag": "toys & games - by owner",
        "tra": "trailers",
        "trb": "trailers - by dealer",
        "tro": "trailers - by owner",
        "vga": "video gaming",
        "vgd": "video gaming - by dealer",
        "vgm": "video gaming - by owner",
        "waa": "wanted",
        "wad": "wanted - by dealer",
        "wan": "wanted - by owner",
    }

    gigs = {
        "cpg": "computer gigs",
        "crg": "creative gigs",
        "cwg": "crew gigs",
        "dmg": "domestic gigs",
        "evg": "event gigs",
        "lbg": "labor gigs",
        "tlg": "talent gigs",
        "wrg": "writing gigs",
    }

    housing = {
        "apa": "apartments / housing for rent",
        "swp": "housing swap",
        "off": "office & commercial",
        "prk": "parking & storage",
        "rea": "real estate",
        "reb": "real estate - by dealer",
        "reo": "real estate - by owner",
        "roo": "rooms & shares",
        "sub": "sublets & temporary",
        "vac": "vacation rentals",
        "hou": "wanted: apts",
        "rew": "wanted: real estate",
        "sha": "wanted: room/share",
        "sbw": "wanted: sublet/temp",
    }

    jobs = {
        "acc": "accounting/finance",
        "ofc": "admin/office",
        "egr": "architect/engineer/cad",
        "med": "art/media/design",
        "bus": "business/mgmt",
        "csr": "customer service",
        "edu": "education/teaching",
        "etc": "et cetera",
        "fbh": "food/beverage/hospitality",
        "lab": "general labor",
        "gov": "government",
        "hea": "healthcare",
        "hum": "human resource",
        "lgl": "legal/paralegal",
        "mnu": "manufacturing",
        "mar": "marketing/advertising/pr",
        "npo": "nonprofit",
        "rej": "real estate",
        "ret": "retail/wholesale",
        "sls": "sales",
        "spa": "salon/spa/fitness",
        "sci": "science/biotech",
        "sec": "security",
        "trd": "skilled trades/artisan",
        "sof": "software/qa/dba/etc",
        "sad": "systems/networking",
        "tch": "technical support",
        "trp": "transportation",
        "tfr": "tv/film/video/radio",
        "web": "web/html/info design",
        "wri": "writing/editing",
    }

    resumes = {}

    services = {
        "aos": "automotive services",
        "bts": "beauty services",
        "cms": "cell phone / mobile services",
        "cps": "computer services",
        "crs": "creative services",
        "cys": "cycle services",
        "evs": "event services",
        "fgs": "farm & garden services",
        "fns": "financial services",
        "hss": "household services",
        "lbs": "labor / hauling / moving",
        "lgs": "legal services",
        "lss": "lessons & tutoring",
        "mas": "marine services",
        "pas": "pet services",
        "rts": "real estate services",
        "sks": "skilled trade services",
        "biz": "small biz ads",
        "trv": "travel/vacation services",
        "wet": "writing / editing / translation",
    }


class region:
    """Store valid Craigslist site and area keys. Last updated: 2021-08-08."""

    areas = {
        "atlanta": {"nat", "wat", "eat", "sat", "atl"},
        "boston": {"gbs", "bmw", "sob", "nos", "nwb"},
        "chicago": {"chc", "nwc", "nch", "sox", "nwi", "wcl"},
        "dallas": {"dal", "sdf", "mdf", "ndf", "ftw"},
        "detroit": {"wyn", "mcb", "okl"},
        "fortlauderdale": {"brw", "mdc", "pbc"},
        "fortmyers": {"col", "lee", "chl"},
        "losangeles": {"ant", "sgv", "lac", "lgb", "sfv", "wst"},
        "miami": {"brw", "mdc"},
        "minneapolis": {"wsh", "ank", "hnp", "csw", "dak", "ram"},
        "newyork": {"brk", "mnh", "stn", "wch", "lgi", "fct", "brx", "jsy", "que"},
        "phoenix": {"evl", "nph", "wvl", "cph"},
        "portland": {"mlt", "clc", "yam", "nco", "clk", "grg", "wsc"},
        "sandiego": {"ssd", "csd", "esd", "nsd"},
        "seattle": {"sno", "oly", "see", "kit", "skc", "est", "tac"},
        "sfbay": {"eby", "scz", "pen", "sby", "sfc", "nby"},
        "tampa": {"psc", "hil", "pnl", "hdo"},
        "toronto": {"mss", "yrk", "drh", "oak", "bra", "tor"},
        "vancouver": {"nvn", "pml", "van", "rch", "bnc", "rds"},
    }

    # fmt: off
    sites = {
        'abbotsford', 'aberdeen', 'abilene', 'acapulco', 'accra', 'addisababa',
        'adelaide', 'ahmedabad', 'akroncanton', 'albany', 'albanyga', 'albuquerque',
        'alicante', 'allentown', 'altoona', 'amarillo', 'ames', 'amsterdam',
        'anchorage', 'annapolis', 'annarbor', 'appleton', 'asheville', 'ashtabula',
        'athens', 'athensga', 'athensohio', 'atlanta', 'auburn', 'auckland',
        'austin', 'bacolod', 'baghdad', 'bajasur', 'bakersfield', 'baleares',
        'baltimore', 'bangalore', 'bangkok', 'bangladesh', 'barcelona', 'barrie',
        'basel', 'bath', 'batonrouge', 'battlecreek', 'beaumont', 'beijing',
        'beirut', 'belfast', 'belleville', 'bellingham', 'belohorizonte', 'bemidji',
        'bend', 'berlin', 'bern', 'bgky', 'bham', 'bhubaneswar',
        'bigbend', 'bilbao', 'billings', 'binghamton', 'birmingham', 'bismarck',
        'blacksburg', 'bloomington', 'bn', 'boise', 'bologna', 'boone',
        'bordeaux', 'boston', 'boulder', 'bozeman', 'brainerd', 'brantford',
        'brasilia', 'bremen', 'brighton', 'brisbane', 'bristol', 'brownsville',
        'brunswick', 'brussels', 'bucharest', 'budapest', 'buenosaires', 'buffalo',
        'bulgaria', 'butte', 'cadiz', 'cairns', 'cairo', 'calgary',
        'cambridge', 'canarias', 'canberra', 'capetown', 'caracas', 'carbondale',
        'cardiff', 'cariboo', 'casablanca', 'catskills', 'cdo', 'cebu',
        'cedarrapids', 'cenla', 'centralmich', 'cfl', 'chambana', 'chambersburg',
        'chandigarh', 'charleston', 'charlestonwv', 'charlotte', 'charlottesville', 'chatham',
        'chattanooga', 'chautauqua', 'chengdu', 'chennai', 'chicago', 'chico',
        'chihuahua', 'chillicothe', 'chongqing', 'christchurch', 'cincinnati', 'clarksville',
        'cleveland', 'clovis', 'cnj', 'collegestation', 'cologne', 'colombia',
        'columbia', 'columbiamo', 'columbus', 'columbusga', 'comoxvalley', 'cookeville',
        'copenhagen', 'cornwall', 'corpuschristi', 'corvallis', 'cosprings', 'costarica',
        'cotedazur', 'coventry', 'csd', 'curitiba', 'dalian', 'dallas',
        'danville', 'darwin', 'davaocity', 'dayton', 'daytona', 'delaware',
        'delhi', 'denver', 'derby', 'desmoines', 'detroit', 'devon',
        'dothan', 'dresden', 'dubai', 'dublin', 'dubuque', 'duluth',
        'dundee', 'dunedin', 'durban', 'dusseldorf', 'eastco', 'easternshore',
        'eastidaho', 'eastky', 'eastmids', 'eastnc', 'eastoregon', 'easttexas',
        'eauclaire', 'edinburgh', 'edmonton', 'elko', 'elmira', 'elpaso',
        'elsalvador', 'enid', 'erie', 'essen', 'essex', 'eugene',
        'evansville', 'fairbanks', 'fargo', 'farmington', 'faro', 'fayar',
        'fayetteville', 'fingerlakes', 'flagstaff', 'florence', 'florencesc', 'fortaleza',
        'fortcollins', 'fortdodge', 'fortlauderdale', 'fortmyers', 'fortsmith', 'fortwayne',
        'frankfurt', 'frederick', 'fredericksburg', 'fresno', 'ftmcmurray', 'fukuoka',
        'gadsden', 'galveston', 'geneva', 'genoa', 'glasgow', 'glensfalls',
        'goa', 'goldcoast', 'goldcountry', 'granada', 'grandforks', 'grandisland',
        'grandrapids', 'greatfalls', 'greenbay', 'greensboro', 'greenville', 'grenoble',
        'guadalajara', 'guanajuato', 'guangzhou', 'guatemala', 'guelph', 'gulfport',
        'haifa', 'halifax', 'hamburg', 'hamilton', 'hampshire', 'hanford',
        'hangzhou', 'hannover', 'harrisburg', 'harrisonburg', 'hartford', 'hat',
        'hattiesburg', 'heidelberg', 'helena', 'helsinki', 'hermosillo', 'hickory',
        'hiltonhead', 'hiroshima', 'hobart', 'holland', 'hongkong', 'honolulu',
        'houma', 'houston', 'hudsonvalley', 'humboldt', 'huntington', 'huntsville',
        'hyderabad', 'iloilo', 'imperial', 'indianapolis', 'indore', 'inlandempire',
        'iowacity', 'istanbul', 'ithaca', 'jackson', 'jacksontn', 'jacksonville',
        'jaipur', 'jakarta', 'janesville', 'jerseyshore', 'jerusalem', 'johannesburg',
        'jonesboro', 'joplin', 'juarez', 'juneau', 'jxn', 'kaiserslautern',
        'kalamazoo', 'kalispell', 'kamloops', 'kansascity', 'kelowna', 'kenai',
        'kent', 'kenya', 'kerala', 'keys', 'killeen', 'kingston',
        'kirksville', 'kitchener', 'klamath', 'knoxville', 'kokomo', 'kolkata',
        'kootenays', 'kpr', 'ksu', 'kuwait', 'lacrosse', 'lafayette',
        'lakecharles', 'lakecity', 'lakeland', 'lancaster', 'lansing', 'lapaz',
        'laredo', 'lasalle', 'lascruces', 'lasvegas', 'lausanne', 'lawrence',
        'lawton', 'leeds', 'leipzig', 'lethbridge', 'lewiston', 'lexington',
        'lille', 'lima', 'limaohio', 'lincoln', 'lisbon', 'littlerock',
        'liverpool', 'logan', 'loire', 'london', 'londonon', 'longisland',
        'losangeles', 'louisville', 'loz', 'lubbock', 'lucknow', 'luxembourg',
        'lynchburg', 'lyon', 'macon', 'madison', 'madrid', 'maine',
        'malaga', 'malaysia', 'managua', 'manchester', 'manila', 'mankato',
        'mansfield', 'marseilles', 'marshall', 'martinsburg', 'masoncity', 'mattoon',
        'mazatlan', 'mcallen', 'meadville', 'medford', 'melbourne', 'memphis',
        'merced', 'meridian', 'mexicocity', 'miami', 'micronesia', 'milan',
        'milwaukee', 'minneapolis', 'missoula', 'mobile', 'modesto', 'mohave',
        'monroe', 'monroemi', 'montana', 'monterey', 'monterrey', 'montevideo',
        'montgomery', 'montpellier', 'montreal', 'morgantown', 'moscow', 'moseslake',
        'mumbai', 'muncie', 'munich', 'muskegon', 'myrtlebeach', 'nacogdoches',
        'naga', 'nagoya', 'nanaimo', 'nanjing', 'naples', 'nashville',
        'natchez', 'nd', 'nesd', 'newbrunswick', 'newcastle', 'newfoundland',
        'newhaven', 'newjersey', 'newlondon', 'neworleans', 'newyork', 'nh',
        'niagara', 'nmi', 'norfolk', 'northernwi', 'northmiss', 'northplatte',
        'norwich', 'nottingham', 'ntl', 'nuremberg', 'nwct', 'nwga',
        'nwks', 'oaxaca', 'odessa', 'ogden', 'okaloosa', 'okinawa',
        'oklahomacity', 'olympic', 'omaha', 'onslow', 'orangecounty', 'oregoncoast',
        'orlando', 'osaka', 'oslo', 'ottawa', 'ottumwa', 'outerbanks',
        'owensboro', 'owensound', 'oxford', 'pakistan', 'palmsprings', 'pampanga',
        'panama', 'panamacity', 'paris', 'parkersburg', 'peace', 'pei',
        'pennstate', 'pensacola', 'peoria', 'perth', 'perugia', 'peterborough',
        'philadelphia', 'phoenix', 'pittsburgh', 'plattsburgh', 'poconos', 'porthuron',
        'portland', 'porto', 'portoalegre', 'potsdam', 'prague', 'pretoria',
        'princegeorge', 'providence', 'provo', 'puebla', 'pueblo', 'puertorico',
        'pullman', 'pune', 'pv', 'quadcities', 'quebec', 'quincy',
        'quito', 'racine', 'raleigh', 'ramallah', 'rapidcity', 'reading',
        'recife', 'reddeer', 'redding', 'regina', 'rennes', 'reno',
        'reykjavik', 'richmond', 'richmondin', 'rio', 'roanoke', 'rochester',
        'rockford', 'rockies', 'rome', 'roswell', 'rouen', 'sacramento',
        'saginaw', 'saguenay', 'salem', 'salina', 'saltlakecity', 'salvador',
        'sanangelo', 'sanantonio', 'sandiego', 'sandusky', 'sanmarcos', 'santafe',
        'santamaria', 'santiago', 'santodomingo', 'saopaulo', 'sapporo', 'sarasota',
        'sardinia', 'sarnia', 'saskatoon', 'savannah', 'scottsbluff', 'scranton',
        'sd', 'seattle', 'seks', 'semo', 'sendai', 'seoul',
        'sevilla', 'sfbay', 'shanghai', 'sheboygan', 'sheffield', 'shenyang',
        'shenzhen', 'sherbrooke', 'shoals', 'showlow', 'shreveport', 'sicily',
        'sierravista', 'singapore', 'siouxcity', 'siouxfalls', 'skeena', 'slo',
        'smd', 'soo', 'southbend', 'southcoast', 'southjersey', 'spacecoast',
        'spokane', 'springfield', 'springfieldil', 'statesboro', 'staugustine', 'stcloud',
        'stgeorge', 'stillwater', 'stjoseph', 'stlouis', 'stockholm', 'stockton',
        'stpetersburg', 'strasbourg', 'stuttgart', 'sudbury', 'sunshine', 'surat',
        'susanville', 'swks', 'swmi', 'swv', 'swva', 'sydney',
        'syracuse', 'taipei', 'tallahassee', 'tampa', 'tehran', 'telaviv',
        'terrehaute', 'territories', 'texarkana', 'texoma', 'thumb', 'thunderbay',
        'tijuana', 'tippecanoe', 'tokyo', 'toledo', 'topeka', 'torino',
        'toronto', 'toulouse', 'tricities', 'troisrivieres', 'tucson', 'tulsa',
        'tunis', 'tuscaloosa', 'tuscarawas', 'twinfalls', 'twintiers', 'ukraine',
        'up', 'utica', 'valdosta', 'valencia', 'vancouver', 'venice',
        'ventura', 'veracruz', 'vermont', 'victoriatx', 'vienna', 'vietnam',
        'virgin', 'visalia', 'waco', 'warsaw', 'washingtondc', 'waterloo',
        'watertown', 'wausau', 'wellington', 'wenatchee', 'westernmass', 'westky',
        'westmd', 'westslope', 'wheeling', 'whistler', 'whitehorse', 'wichita',
        'wichitafalls', 'williamsport', 'wilmington', 'winchester', 'winnipeg', 'winstonsalem',
        'wollongong', 'worcester', 'wuhan', 'wv', 'wyoming', 'xian',
        'yakima', 'yellowknife', 'york', 'youngstown', 'yubasutter', 'yucatan',
    }
    # fmt: on
