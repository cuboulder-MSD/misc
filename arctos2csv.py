import csv, sys

#CLI syntax is 'python arctosStartingRange arctosStopingRange'

arctosStart = sys.argv[1]
arctosStop = sys.argv[2]

myDict = {}
counter = 1

with open(str(arctosStart)+'-'+str(arctosStop)+'.csv', 'w' ) as csvFile:
    
    for i in range(int(arctosStart), int(arctosStop)+1):
      myDict['ARCTOS GUID #'+str(counter)] = 'UCM:Herp:'+str(i)
      myDict['ARCTOS LINK #'+str(counter)] = 'https://arctos.database.museum/guid/UCM:Herp:'+str(i)
      counter += 1
    w = csv.DictWriter(csvFile, myDict.keys())
    w.writeheader()
    w.writerow(myDict)

