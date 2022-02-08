class Player:
    def __init__(self, pseudo, id):
        self.pseudo = pseudo
        self.id = id
        self.tag = ""
        self.ranking = ""
        self.ranking_int = 0

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