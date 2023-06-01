from glob import glob

totalData = {}
path = "/home/gabriel/mestrado/resultados/grafico_rdf_python/"
outRdf = glob(path + "*.out"); outNames = [name.split("/")[-1] for name in outRdf]
csvRdf = glob(path + "*.csv"); csvNames = [name.split("/")[-1] for name in csvRdf]

# Codigo dos rdfs do lammps
for outFile in range(len(outNames)):
    floatRdf=[]
    with open(outRdf[outFile], "r") as file:
        lines = file.readlines()
        last_lines = lines[-150:]
        strData = [num.split() for num in last_lines] 
        file.close()

    for strList in strData:
        templist = []
        for strNum in strList:
            templist.append(float(strNum))
            #print(templist)
        floatRdf.append(templist)
        templist=[]
    totalData[outNames[outFile]]=floatRdf

# Codigo dos rdfs do travis
for csvFile in range(len(csvNames)):
    angDist = []
    gR=[]
    csvData=[]
    with open(csvRdf[csvFile], "r") as file:
        allLines = file.readlines()
        lines = allLines[1:]
        strData = [num.split(";") for num in lines]
        file.close()
    
    for strList in strData:
        templist = []
        for strNum in strList:
            templist.append(float(strNum))
        #print(templist)
        splitedDist = templist[:1]
        splitedRest = templist[1:]
        gR.append(splitedRest)
        angDist.append(splitedDist)
