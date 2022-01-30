class Player:
    def __init__(self, pseudo, id, tag, ranked):
        self.pseudo = pseudo
        self.id = id
        self.tag = tag
        self.ranked = ranked
    
    def getPseudo(self): 
        return self.pseudo
    
    def getId(self): 
        return self.id
    
    def getTag(self): 
        return self.tag
    
    def getRanked(self): 
        return self.ranked

    def setPseudo(self,pseudo):
        self.pseudo = pseudo

    def setId(self,id):
        self.id = id
    
    def setTag(self,tag):
        self.tag = tag

    def setRanked(self,ranked):
        self.ranked = ranked
    
    
    