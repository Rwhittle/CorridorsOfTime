

class Searcher:
    def __init__(self, database):
        self._database = database
        return

    def DepthFirstSearch(self, root, target, visited = []):
        visited.append(root)
        path = ""
        if(root.equals(target)):
            path = root.getCenter
        else:
            for i in range(6):
                #if there is an open wall link from the root that we haven't yet visited
                if((not root.getWall(i) and root.getLink(i) != None) and (not root.getLink(i) in visited)):
                    path = path + DepthFirstSearch(root.getLink(i))

        return path
            

    
