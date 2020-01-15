class MapNode:
    def __init__(self, line):
        splitLine = line.split('\t')
        self.imgURL = splitLine[0]
        self.center = splitLine[1]
        self.openings = splitLine[2]
        self.edges = splitLine[3:9]
        self.links = [-1,-1,-1,-1,-1,-1]

    def getEdge(self, edgeNum):
        return self.edges[edgeNum]

    def getEdgeRot(self, edgeNum):
        edge = self.edges[edgeNum]
        rotEdge = ""
        for symbol in edge:
            rotEdge = str(symbol) + rotEdge
        return rotEdge
    
    def getCenter(self):
        return self.center

    def getLink(self, index):
        return self.links[index]
    
    def setLink(self,index,linkIndex):
        self.links[index] = linkIndex

    def toString(self):
        return f"URL:{self.imgURL},center:{self.center},openings:{self.openings},edges:{self.edges},links:{self.links}"
