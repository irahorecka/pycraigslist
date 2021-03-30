from .base import BaseAPI, ParentMethods
from . import filters


class community(BaseAPI, ParentMethods):
    """ Craigslist community API wrapper. """

    category = "ccc"
    filters = filters.query.community

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class act(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ats(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class kid(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class com(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class grp(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vnn(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class laf(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mis(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class muc(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pet(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pol(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rid(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vol(BaseAPI):
        filters = filters.query.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class events(BaseAPI, ParentMethods):
    """ Craigslist events API wrapper. """

    category = "eee"
    filters = filters.query.events


class forsale(BaseAPI, ParentMethods):
    """ Craigslist for sale API wrapper. """

    category = "sss"
    filters = filters.query.forsale

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class ata(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ppa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ara(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sna(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pta(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wta(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ava(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class baa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bar(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bip(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bia(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bpa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class boo(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bka(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bfa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cta(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ema(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class moa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cla(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cba(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class syp(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sya(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ela(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class gra(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class zip(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fua(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class gms(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class foa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class haa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hva(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hsa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class jwa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class maa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mpa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mca(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class msa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pha(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rva(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sga(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tia(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tla(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class taa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tra(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vga(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class waa(BaseAPI):
        filters = filters.query.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class gigs(BaseAPI, ParentMethods):

    category = "ggg"
    filters = filters.query.gigs

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class cpg(BaseAPI):
        filters = filters.query.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class crg(BaseAPI):
        filters = filters.query.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cwg(BaseAPI):
        filters = filters.query.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class dmg(BaseAPI):
        filters = filters.query.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class evg(BaseAPI):
        filters = filters.query.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lbg(BaseAPI):
        filters = filters.query.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tlg(BaseAPI):
        filters = filters.query.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wrg(BaseAPI):
        filters = filters.query.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class housing(BaseAPI, ParentMethods):
    """ Craigslist housing API wrapper. """

    category = "hhh"
    filters = filters.query.housing

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class apa(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class off(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class swp(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class prk(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rea(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class roo(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sub(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vac(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hou(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rew(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sha(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sbw(BaseAPI):
        filters = filters.query.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class jobs(BaseAPI, ParentMethods):
    """ Craigslist jobs API wrapper. """

    category = "jjj"
    filters = filters.query.jobs

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class acc(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ofc(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class egr(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class med(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bus(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class csr(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class edu(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class etc(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fbh(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lab(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class gov(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hea(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hum(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lgl(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mnu(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mar(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class npo(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rej(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ret(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sls(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class spa(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sci(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sec(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trd(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sof(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sad(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tch(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trp(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tfr(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class web(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wri(BaseAPI):
        filters = filters.query.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class resumes(BaseAPI, ParentMethods):
    """ Craigslist resumes API wrapper. """

    category = "rrr"
    filters = filters.query.resumes

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class services(BaseAPI, ParentMethods):
    """ Craigslist services API wrapper. """

    category = "bbb"
    filters = filters.query.services

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class aos(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bts(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cms(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cps(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class crs(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cys(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class evs(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fgs(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fns(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hss(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lbs(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lgs(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lss(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mas(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pas(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rts(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sks(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class biz(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trv(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wet(BaseAPI):
        filters = filters.query.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)
