import redis

globalUrlsStore = redis.Redis(host='localhost', port=6379, db=1)

with open("/home/optix/Documents/python/leadsprospecting/states.txt") as file:
    stateList=[]
    for line in file:
        stateDict={}
        line =line.rstrip().split("|")
        allcities=line[2].split(", ")
        # print(line[0])
        # print(allcities)
        stateDict['state']=line[0]
        stateDict['cities']=allcities
        for cit in allcities:
            print(line[0]+" | "+cit)
            # globalUrlsStore.sadd("states",line[0]+"|"+cit)        
            globalUrlsStore.sadd(line[0],cit)        
        stateList.append(stateDict)
# print(stateList)


