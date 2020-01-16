from MapNode import MapNode

class MapDatabase:
    def __init__(self):
        #a MapDatabase is a class which contains a list of MapNodes
        self._data = []
        return
    

    #a function to convert a tab delimited spreadsheet file into an array of the different pieces
    def import_data(self,path):
        try:
            databaseRaw = open(path)
            mapNodes = []
            for line in databaseRaw:
                node = MapNode()
                if(node.genFromJSON(line)):
                    mapNodes.append(node)
                    #print(f"imported node {index}")
        except Error as e:
            print("Error in loading data")
            print(e)
            return False

        self._data = mapNodes
        return True

    #find which other nodes a node links to
    def findLinks(self,node):
        for potentialNode in self._data:
            if potentialNode != node:
                for i in range(6):
                    currentEdge = node.getEdge(i)
                    if(node.getLink(i) == None and currentEdge != "BBBBBBB"):
                        potentialEdge = potentialNode.getEdge((i+3)%6)
                        #print(f"vs {potentialEdge}")
                        if currentEdge == potentialEdge:
                            print(f"{currentEdge} matches {potentialEdge}")
                            node.setLink(i,potentialNode)
                            potentialNode.setLink((i+3)%6,node)
                        #else:
                        #    print(f"{currentEdge} does not match {potentialEdge}")

    def linkAll(self):
        for node in self._data:
            findLinks(nodes,node)

    def outputToFile(nodes, fileName):
        output = open(fileName, mode='w')
        for node in nodes:
            output.write(node.toString()+"\n")
        output.close()
        return

    def getLinked(self):
        filteredData = []
        for node in self._data:
            for j in range(6):
                if node.getLink(j) != None:
                    filteredData.append(node)
                    break
        return filteredData
    #method to return a list of all unique nodes
    def getUnique(self):
        filteredData = []
        for node in self._data:
            hasDuplicate = False
            for otherNode in filteredData:
                if(node.equals(otherNode)):
                   hasDuplicate = True
            if(not hasDuplicate):
                   filteredData.append(node)
        return filteredData

    #method to find nodes that are on the edge of the puzzle
    def getEdgeNodes(self):
        filteredData = []
        for node in self._data:
            hasEdge = False
            for edge in node.getEdges():
                if(edge == "BBBBBBB"):
                    hasEdge = True
            if(hasEdge):
                filteredData.append(node)
        return filteredData
    
    #method which finds edge pieces with an open wall along the edge of the puzzle
    def getEndpoints(self):
        filteredData = []
        for node in self.getEdgeNodes():
            isEndpoint = False
            nodeWalls = node.getWalls()
            for i in range(6):
                if(not nodeWalls[i] and node.getEdge(i) == "BBBBBBB"):
                    isEndpoint = True

            if(isEndpoint):
                filteredData.append(node)  
        return filteredData
        

        
#def removeNoCenters(nodes):
