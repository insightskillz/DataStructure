#Recursively n·movc a ll a djacent duplicates: Given a string of characters, recursively remove
#adjacent duplicate charoctcrs from string. The output st ring should not have any adjacent duplicates.


def  rcmoveAdjacenLDuplicutcs(str):
    stkpr = -1
    i = 0
    size = len(str)
    while i < size:
        if(stkpr == -1 or str[stkpr]!= str[i]):
            stkpr += 1
            str[stkpr]=str[i]
            i +=1
        else:
            while i < size and str[stkpr]==str[i]:
                i += 1
            stkpr -= 1
        stkpr += 1
    str =str[0:stkpr]
    print(str)


rcmoveAdjacenLDuplicutcs(['6','2','4','1','2','2','1'])



#Given an array of elements, replace every clement with nearest greater clement on the right of that element.


def replaceWithNearestOrcaterElement(A):
    nextNearestGreater = float("-inf")
    i = j = 0
    for i in range(0, len(A)-1):
        nextNearestGreater=float("-inf")
        for j in range(i+1,len(A)):
            if A[i] < A[j]:
                nextNearestGreater = A[j]
                break
            print("For"+str(A[i]) +"," +str(nextNearestGreater) +"is the nerest greater element")