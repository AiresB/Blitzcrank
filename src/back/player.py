class Player:
    def __init__(self, riot_res):
        self.update(riot_res)
        self.tag = ""
        self.ranking = ""
        self.ranking_int = 0


    def update(self, riot_res):
        self.id = riot_res["id"]
        self.acc_id = riot_res["accountId"]
        self.puuid = riot_res["puuid"]
        self.pseudo = riot_res["name"]
        self.pp_id = riot_res["profileIconId"]
        self.lvl = riot_res["summonerLevel"]


    ## GETTERS
    def get_pseudo(self):
        return self.pseudo

    def get_id(self):
        return self.id

    def get_tag(self):
        return self.tag

    def get_ranking(self):
        return self.ranking

    def get_ranking_int(self):
        return self.ranking_int

    def get_acc_id(self):
        return self.acc_id

    def get_puuid(self):
        return self.puuid

    def get_pp_id(self):
        return self.pp_id

    def get_lvl(self):
        return self.lvl


    ## SETTERS
    def set_pseudo(self,pseudo):
        self.pseudo = pseudo

    def set_id(self,id):
        self.id = id

    def set_tag(self,tag):
        self.tag = tag

    def set_ranking(self,ranking):
        self.ranking = ranking

    def set_ranking_int(self,ranking_int):
        self.ranking_int = ranking_int

    def set_acc_id(self,acc_id):
        self.acc_id = acc_id

    def set_puuid(self, puuid):
        self.puuid = puuid

    def set_pp_id(self,pp_id):
        self.pp_id = pp_id

    def set_lvl(self,lvl):
        self.lvl = lvl