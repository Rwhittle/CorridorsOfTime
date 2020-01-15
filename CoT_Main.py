from MapNode import MapNode

#a function to convert a tab delimited spreadsheet file into an array of the different pieces
def import_data(path,include_noref = False):
    databaseRaw = open(path)
    mapNodes = {}
    index = 0
    for line in databaseRaw:
        newNode = MapNode(line)
        duplicateNode = False
        for i in range(index):
            if(isDuplicate(newNode, mapNodes[i])):
                duplicateNode = True
        if not duplicateNode:
            mapNodes[index] = newNode
            index = index + 1
    return mapNodes

#find which other nodes a node links to
def findLinks(index, nodes):
    print(f"finding links for node {index}")
    currentNode = nodes[index]
    for j in range(len(nodes)):
        print(f"Testing node {j}")
        node = nodes[j]
        if node != currentNode:
            for i in range(6):
                currentEdge = currentNode.getEdge(i)
                if(currentNode.getLink(i) == -1 and currentEdge != "BBBBBBB"):
                    potentialEdge = node.getEdge((i+3)%6)
                    #print(f"vs {potentialEdge}")
                    if currentEdge == potentialEdge:
                        print(f"{currentEdge} matches {potentialEdge}")
                        currentNode.setLink(i,j)
                        node.setLink((i+3)%6,index)
                    #else:
                    #    print(f"{currentEdge} does not match {potentialEdge}")

def findAllLinks(nodes):
    for index in range(len(nodes)):
        findLinks(index, nodes)

def isDuplicate(node1, node2):
    if(node1.center != node2.center or node1.openings != node2.openings):
        return False
    for i in range(6):
        if(node1.edges[i] != node2.edges[i]):
           return False
    return True

def outputToFile(nodes, fileName):
    output = open(fileName, mode='w')
    output.write("index,data\n")
    for i in range(len(nodes)):
        output.write(str(i)+","+nodes[i].toString()+"\n")
    output.close()
    return

def solve(path):
    data = import_data(path)
    findAllLinks(data)
    outputToFile(data, "solution.txt")
