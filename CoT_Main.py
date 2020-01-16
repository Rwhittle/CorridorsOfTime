from MapNode import MapNode


#a function to convert a tab delimited spreadsheet file into an array of the different pieces
def import_data(path):
    databaseRaw = open(path)
    mapNodes = []
    index = 0
    for line in databaseRaw:
        node = MapNode()
        if(node.genFromJSON(line)):
            mapNodes.append(node)
            #print(f"imported node {index}")

    removeDuplicates(mapNodes)
    return mapNodes

#find which other nodes a node links to
def findLinks(nodes,node):
    for potentialNode in nodes:
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

def findAllLinks(nodes):
    for node in nodes:
        findLinks(nodes,node)

def isDuplicate(node1, node2):
    if(node1.center != node2.center):
        return False
    for i in range(6):
        if(node1.edges[i] != node2.edges[i]):
           return False
    return True

def outputToFile(nodes, fileName):
    output = open(fileName, mode='w')
    for node in nodes:
        output.write(node.toString()+"\n")
    output.close()
    return

def solve(path):
    data = import_data(path)
    findAllLinks(data)
    filteredData = removeUnlinked(data)
    outputToFile(filteredData, "solution.txt")

def removeUnlinked(nodes):
    filteredData = []
    for node in nodes:
        for j in range(6):
            if node.getLink(j) != None:
                filteredData.append(node)
                break
    return filteredData

def removeDuplicates(nodes):
    filteredData = []
    for node in nodes:
        hasDuplicate = False
        for otherNode in filteredData:
            if(isDuplicate(node, otherNode)):
               hasDuplicate = True
        if(not hasDuplicate):
               filteredData.append(node)
    return filteredData

        
#def removeNoCenters(nodes):
#    for node in nodes:
#        if
