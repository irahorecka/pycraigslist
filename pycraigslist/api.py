"""
pycraigslist.api
~~~~~~~~~~~~~~~~

This module provides a suite of pycraigslist objects to construct a
Craigslist search.
"""

from .base import BaseAPI, ParentMethods
from . import filters


class community(BaseAPI, ParentMethods):
    """community"""

    category = "ccc"
    search_filters = filters.search.community

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class act(BaseAPI):
        """activity partners"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ats(BaseAPI):
        """artists"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class kid(BaseAPI):
        """childcare"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class com(BaseAPI):
        """general community"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class grp(BaseAPI):
        """groups"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vnn(BaseAPI):
        """local news and views"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class laf(BaseAPI):
        """lost & found"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mis(BaseAPI):
        """missed connections"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class muc(BaseAPI):
        """musicians"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pet(BaseAPI):
        """pets"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pol(BaseAPI):
        """politics"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rnr(BaseAPI):
        """rants & raves"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rid(BaseAPI):
        """rideshare"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vol(BaseAPI):
        """volunteers"""

        search_filters = filters.search.community

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class events(BaseAPI, ParentMethods):
    """events"""

    category = "eee"
    search_filters = filters.search.events

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class forsale(BaseAPI, ParentMethods):
    """for sale"""

    category = "sss"
    search_filters = filters.search.forsale

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class ata(BaseAPI):
        """antiques"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ppa(BaseAPI):
        """appliances"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ppd(BaseAPI):
        """appliances - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class app(BaseAPI):
        """appliances - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ara(BaseAPI):
        """arts & crafts"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ard(BaseAPI):
        """arts & crafts - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class art(BaseAPI):
        """arts & crafts - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sna(BaseAPI):
        """atvs, utvs, snowmobiles"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class snd(BaseAPI):
        """atvs, utvs, snowmobiles - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class snw(BaseAPI):
        """atvs, utvs, snowmobiles - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pta(BaseAPI):
        """auto parts"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ptd(BaseAPI):
        """auto parts - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pts(BaseAPI):
        """auto parts - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wta(BaseAPI):
        """auto wheels & tires"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wtd(BaseAPI):
        """auto wheels & tires - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wto(BaseAPI):
        """auto wheels & tires - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ava(BaseAPI):
        """aviation"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class avd(BaseAPI):
        """aviation - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class avo(BaseAPI):
        """aviation - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class baa(BaseAPI):
        """baby & kid stuff"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bad(BaseAPI):
        """baby & kid stuff - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bab(BaseAPI):
        """baby & kid stuff - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bar(BaseAPI):
        """barter"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bip(BaseAPI):
        """bicycle parts"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bdp(BaseAPI):
        """bicycle parts - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bop(BaseAPI):
        """bicycle parts - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bia(BaseAPI):
        """bicycles"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bid(BaseAPI):
        """bicycles - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bik(BaseAPI):
        """bicycles - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bpa(BaseAPI):
        """boat parts & accessories"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bpd(BaseAPI):
        """boat parts & accessories - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bpo(BaseAPI):
        """boat parts & accessories - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class boo(BaseAPI):
        """boats"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bod(BaseAPI):
        """boats - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class boa(BaseAPI):
        """boats - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bka(BaseAPI):
        """books & magazines"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bkd(BaseAPI):
        """books & magazines - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bks(BaseAPI):
        """books & magazines - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bfa(BaseAPI):
        """business"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bfd(BaseAPI):
        """business - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bfs(BaseAPI):
        """business - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cta(BaseAPI):
        """cars & trucks"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ctd(BaseAPI):
        """cars & trucks - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cto(BaseAPI):
        """cars & trucks - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ema(BaseAPI):
        """cds / dvds / vhs"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class emq(BaseAPI):
        """cds / dvds / vhs - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class emd(BaseAPI):
        """cds / dvds / vhs - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class moa(BaseAPI):
        """cell phones"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mod(BaseAPI):
        """cell phones - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mob(BaseAPI):
        """cell phones - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cla(BaseAPI):
        """clothing & accessories"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cld(BaseAPI):
        """clothing & accessories - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class clo(BaseAPI):
        """clothing & accessories - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cba(BaseAPI):
        """collectibles"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cbd(BaseAPI):
        """collectibles - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class clt(BaseAPI):
        """collectibles - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class syp(BaseAPI):
        """computer parts"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sdp(BaseAPI):
        """computer parts - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sop(BaseAPI):
        """computer parts - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sya(BaseAPI):
        """computers"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class syd(BaseAPI):
        """computers - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sys(BaseAPI):
        """computers - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ela(BaseAPI):
        """electronics"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class eld(BaseAPI):
        """electronics - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ele(BaseAPI):
        """electronics - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class gra(BaseAPI):
        """farm & garden"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class zip(BaseAPI):
        """free stuff"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fua(BaseAPI):
        """furniture"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class gms(BaseAPI):
        """garage & moving sales"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class foa(BaseAPI):
        """general for sale"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fod(BaseAPI):
        """general for sale - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fur(BaseAPI):
        """general for sale - by owner"""

        # an odd-ball - give 'for' alias 'fur'

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = "for"
            super().__init__(*args, **kwargs)

    class haa(BaseAPI):
        """health and beauty"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class had(BaseAPI):
        """health and beauty - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hab(BaseAPI):
        """health and beauty - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hva(BaseAPI):
        """heavy equipment"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hvd(BaseAPI):
        """heavy equipment - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hvo(BaseAPI):
        """heavy equipment - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hsa(BaseAPI):
        """household items"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hsd(BaseAPI):
        """household items - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hsh(BaseAPI):
        """household items - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class jwa(BaseAPI):
        """jewelry"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class jwd(BaseAPI):
        """jewelry - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class jwl(BaseAPI):
        """jewelry - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class maa(BaseAPI):
        """materials"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mad(BaseAPI):
        """materials - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mat(BaseAPI):
        """materials - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mpa(BaseAPI):
        """motorcycle parts & accessories"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mpd(BaseAPI):
        """motorcycle parts & accessories - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mpo(BaseAPI):
        """motorcycle parts & accessories - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mca(BaseAPI):
        """motorcycles/scooters"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mcd(BaseAPI):
        """motorcycles/scooters - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mcy(BaseAPI):
        """motorcycles/scooters - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class msa(BaseAPI):
        """musical instruments"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class msd(BaseAPI):
        """musical instruments - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class msg(BaseAPI):
        """musical instruments - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pha(BaseAPI):
        """photo/video"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class phd(BaseAPI):
        """photo/video - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pho(BaseAPI):
        """photo/video - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rva(BaseAPI):
        """recreational vehicles"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rvd(BaseAPI):
        """recreational vehicles - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rvs(BaseAPI):
        """recreational vehicles - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sga(BaseAPI):
        """sporting goods"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sgd(BaseAPI):
        """sporting goods - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class spo(BaseAPI):
        """sporting goods - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tia(BaseAPI):
        """tickets"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tid(BaseAPI):
        """tickets - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tix(BaseAPI):
        """tickets - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tla(BaseAPI):
        """tools"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class taa(BaseAPI):
        """toys & games"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tad(BaseAPI):
        """toys & games - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tag(BaseAPI):
        """toys & games - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tra(BaseAPI):
        """trailers"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trb(BaseAPI):
        """trailers - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tro(BaseAPI):
        """trailers - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vga(BaseAPI):
        """video gaming"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vgd(BaseAPI):
        """video gaming - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vgm(BaseAPI):
        """video gaming - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class waa(BaseAPI):
        """wanted"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wad(BaseAPI):
        """wanted - by dealer"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wan(BaseAPI):
        """wanted - by owner"""

        search_filters = filters.search.forsale

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class gigs(BaseAPI, ParentMethods):
    """gigs"""

    category = "ggg"
    search_filters = filters.search.gigs

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class cpg(BaseAPI):
        """computer gigs"""

        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class crg(BaseAPI):
        """creative gigs"""

        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cwg(BaseAPI):
        """crew gigs"""

        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class dmg(BaseAPI):
        """domestic gigs"""

        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class evg(BaseAPI):
        """event gigs"""

        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lbg(BaseAPI):
        """labor gigs"""

        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tlg(BaseAPI):
        """talent gigs"""

        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wrg(BaseAPI):
        """writing gigs"""

        search_filters = filters.search.gigs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class housing(BaseAPI, ParentMethods):
    """housing"""

    category = "hhh"
    search_filters = filters.search.housing

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class apa(BaseAPI):
        """apartments / housing for rent"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class swp(BaseAPI):
        """housing swap"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class off(BaseAPI):
        """office & commercial"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class prk(BaseAPI):
        """parking & storage"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rea(BaseAPI):
        """real estate"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class reb(BaseAPI):
        """real estate - by dealer"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class reo(BaseAPI):
        """real estate - by owner"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class roo(BaseAPI):
        """rooms & shares"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sub(BaseAPI):
        """sublets & temporary"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class vac(BaseAPI):
        """vacation rentals"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hou(BaseAPI):
        """wanted: apts"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rew(BaseAPI):
        """wanted: real estate"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sha(BaseAPI):
        """wanted: room/share"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sbw(BaseAPI):
        """wanted: sublet/temp"""

        search_filters = filters.search.housing

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class jobs(BaseAPI, ParentMethods):
    """jobs"""

    category = "jjj"
    search_filters = filters.search.jobs

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class acc(BaseAPI):
        """accounting/finance"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ofc(BaseAPI):
        """admin/office"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class egr(BaseAPI):
        """architect/engineer/cad"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class med(BaseAPI):
        """art/media/design"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bus(BaseAPI):
        """business/mgmt"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class csr(BaseAPI):
        """customer service"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class edu(BaseAPI):
        """education/teaching"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class etc(BaseAPI):
        """et cetera"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fbh(BaseAPI):
        """food/beverage/hospitality"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lab(BaseAPI):
        """general labor"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class gov(BaseAPI):
        """government"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hea(BaseAPI):
        """healthcare"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hum(BaseAPI):
        """human resource"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lgl(BaseAPI):
        """legal/paralegal"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mnu(BaseAPI):
        """manufacturing"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mar(BaseAPI):
        """marketing/advertising/pr"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class npo(BaseAPI):
        """nonprofit"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rej(BaseAPI):
        """real estate"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class ret(BaseAPI):
        """retail/wholesale"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sls(BaseAPI):
        """sales"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class spa(BaseAPI):
        """salon/spa/fitness"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sci(BaseAPI):
        """science/biotech"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sec(BaseAPI):
        """security"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trd(BaseAPI):
        """skilled trades/artisan"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sof(BaseAPI):
        """software/qa/dba/etc"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sad(BaseAPI):
        """systems/networking"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tch(BaseAPI):
        """technical support"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trp(BaseAPI):
        """transportation"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class tfr(BaseAPI):
        """tv/film/video/radio"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class web(BaseAPI):
        """web/html/info design"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wri(BaseAPI):
        """writing/editing"""

        search_filters = filters.search.jobs

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)


class resumes(BaseAPI, ParentMethods):
    """resumes"""

    category = "rrr"
    search_filters = filters.search.resumes

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class services(BaseAPI, ParentMethods):
    """services"""

    category = "bbb"
    search_filters = filters.search.services

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class aos(BaseAPI):
        """automotive services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class bts(BaseAPI):
        """beauty services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cms(BaseAPI):
        """cell phone / mobile services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cps(BaseAPI):
        """computer services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class crs(BaseAPI):
        """creative services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class cys(BaseAPI):
        """cycle services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class evs(BaseAPI):
        """event services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fgs(BaseAPI):
        """farm & garden services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class fns(BaseAPI):
        """financial services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class hss(BaseAPI):
        """household services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lbs(BaseAPI):
        """labor / hauling / moving"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lgs(BaseAPI):
        """legal services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class lss(BaseAPI):
        """lessons & tutoring"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class mas(BaseAPI):
        """marine services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class pas(BaseAPI):
        """pet services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class rts(BaseAPI):
        """real estate services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class sks(BaseAPI):
        """skilled trade services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class biz(BaseAPI):
        """small biz ads"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class trv(BaseAPI):
        """travel/vacation services"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)

    class wet(BaseAPI):
        """writing / editing / translation"""

        search_filters = filters.search.services

        def __init__(self, *args, **kwargs):
            self.category = self.__class__.__name__
            super().__init__(*args, **kwargs)
