import json

class MapNode:
    def genFromJSON(self, line, requireVerified = True):
        rawLine = line.split('\t')
        #print(rawLine[4])
        if rawLine[4][0:8] != "Verified" and requireVerified:
            #print(f"line not verified")
            return False
        try:
            rawJson = json.loads(rawLine[1])
            self.imgURL = rawLine[2]
            self.center = rawJson["center"]
            self.walls = rawJson["walls"]
            self.edges = []
            unprocessedEdges = rawJson["nodes"]
            self.links = [None,None,None,None,None,None]
            for uEdge in unprocessedEdges:
                pEdge = ""
                for letter in uEdge:
                    pEdge = pEdge + letter
                self.edges.append(pEdge)
            

        except ValueError as e:
            print("json error")
            return False
        except TypeError as e:
            print("type error")
            return False
        return True
            
        
    def genFromTSV(self, line):
        splitLine = line.split('\t')
        self.imgURL = splitLine[0]
        self.center = splitLine[1]
        self.edges = splitLine[3:9]
        self.links = [None,None,None,None,None,None]

    def getEdge(self, edgeNum):
        return self.edges[edgeNum]

    def getEdges(self):
        return self.edges

    def getEdgeRot(self, edgeNum):
        edge = self.edges[edgeNum]
        rotEdge = ""
        for symbol in edge:
            rotEdge = str(symbol) + rotEdge
        return rotEdge
    
    def getCenter(self):
        return self.center

    def getWalls(self):
        return self.walls

    def getWall(self, index):
        return self.walls[index]

    def getLink(self, index):
        return self.links[index]
    
    def setLink(self,index,linkIndex):
        self.links[index] = linkIndex

    def equals(self, otherNode):
        if(self.center != otherNode.center):
            return False
        for i in range(6):
            if(self.edges[i] != otherNode.edges[i]):
               return False
        return True

    def toString(self):
        return f"URL:{self.imgURL},center:{self.center},edges:{self.edges}"
