def spreadsheetToJson(path, outPath):
    sheetFile = open(path)
    sheetRaw = sheetFile.read().split("\n")
    #print(sheetRaw)
    outSheet = "\t"
    for line in sheetRaw:
        jsonOut = "{"
        lineSplit = line.split("\t")
        print(lineSplit)
        center = lineSplit[1]
        walls = [True, True, True, True, True, True]
        openings = lineSplit[2]
        splitOpenings = openings.split(",")
        for digit in splitOpenings:
            val = int(digit)
            walls[val-1] = False
        jsonOut = jsonOut + "\"walls\":"+str(walls).lower()
        jsonOut = jsonOut + ",\"center\":\""+center[0]+"\""
        jsonOut = jsonOut + ",\"nodes\":["
        for i in range(6):
            nodeStr = "["
            for nodeChar in lineSplit[i+3]:
                nodeStr = nodeStr + "\"" + nodeChar + "\","
            nodeStr = nodeStr[:-1] + "]"
            if i<5:
                nodeStr = nodeStr + ","
            jsonOut = jsonOut + nodeStr
        jsonOut = jsonOut + "]}"
        outSheet = outSheet + jsonOut +"\t\t\tVerified\n\t"
    outFile = open(outPath, mode='w')
    outFile.write(outSheet)
    outFile.close()
    sheetFile.close()
                
        
        
