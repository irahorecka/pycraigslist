from .base import BaseAPI, ParentMethods
from . import filters


class community(BaseAPI, ParentMethods):
    """Craigslist community API wrapper."""

    category = "ccc"
    search_filters = filters.search.community

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class act(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ats(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class kid(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class com(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class grp(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vnn(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class laf(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mis(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class muc(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pet(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pol(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rid(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vol(BaseAPI):
        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class events(BaseAPI, ParentMethods):
    """Craigslist events API wrapper."""

    category = "eee"
    search_filters = filters.search.events


class forsale(BaseAPI, ParentMethods):
    """Craigslist for sale API wrapper."""

    category = "sss"
    search_filters = filters.search.forsale

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class ata(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ppa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ara(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sna(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pta(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wta(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ava(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class baa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bar(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bip(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bia(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bpa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class boo(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bka(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bfa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cta(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ema(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class moa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cla(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cba(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class syp(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sya(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ela(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class gra(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class zip(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fua(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class gms(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class foa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class haa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hva(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hsa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class jwa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class maa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mpa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mca(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class msa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pha(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rva(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sga(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tia(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tla(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class taa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tra(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vga(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class waa(BaseAPI):
        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class gigs(BaseAPI, ParentMethods):

    category = "ggg"
    search_filters = filters.search.gigs

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class cpg(BaseAPI):
        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class crg(BaseAPI):
        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cwg(BaseAPI):
        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class dmg(BaseAPI):
        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class evg(BaseAPI):
        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lbg(BaseAPI):
        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tlg(BaseAPI):
        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wrg(BaseAPI):
        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class housing(BaseAPI, ParentMethods):
    """Craigslist housing API wrapper."""

    category = "hhh"
    search_filters = filters.search.housing

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class apa(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class off(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class swp(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class prk(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rea(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class roo(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sub(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vac(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hou(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rew(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sha(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sbw(BaseAPI):
        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class jobs(BaseAPI, ParentMethods):
    """Craigslist jobs API wrapper."""

    category = "jjj"
    search_filters = filters.search.jobs

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class acc(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ofc(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class egr(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class med(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bus(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class csr(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class edu(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class etc(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fbh(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lab(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class gov(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hea(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hum(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lgl(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mnu(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mar(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class npo(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rej(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ret(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sls(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class spa(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sci(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sec(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trd(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sof(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sad(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tch(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trp(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tfr(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class web(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wri(BaseAPI):
        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class resumes(BaseAPI, ParentMethods):
    """Craigslist resumes API wrapper."""

    category = "rrr"
    search_filters = filters.search.resumes

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class services(BaseAPI, ParentMethods):
    """Craigslist services API wrapper."""

    category = "bbb"
    search_filters = filters.search.services

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class aos(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bts(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cms(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cps(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class crs(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cys(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class evs(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fgs(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fns(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hss(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lbs(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lgs(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lss(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mas(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pas(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rts(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sks(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class biz(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trv(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wet(BaseAPI):
        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)
