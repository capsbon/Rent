def double_nine():
    result =[]
    for i in range(1,10):
        temp = []
        for j in range(1,i):
            k = i*j
            #temp.append(k)
            result.append(k)
       # result.append(temp)
    result = list(set(result))
    print(result)
    #zipR = zip(*result)
   # print(list(zipR))
# #double_nine()
def duplicated_list(listR):

    lenlist = len(listR)
    result  =[]
    numlist =[]
    for i in range(lenlist):
        numlist.append(i)
    #print(numlist)
    temp = numlist
    for i in range(lenlist):
        numlist.remove(i)
        #print(numlist)
        for j in numlist:
            if listR[i] == listR[j]:
                result.append(listR[i])
        numlist.append(i)
    print(result)



    #print(result)

listR = [1,2,3,2,1,5,5]
duplicated_list(listR)
