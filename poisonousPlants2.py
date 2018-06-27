def calc(arr):
    st =[]
    second=[]
    st.append(arr[0])
    key=0
    for i in range(1,len(arr)):
        if st[-1] >= arr[i] and key != 1:
            print("The array when {} is greater than {} =====>".format(st[-1],arr[i]),arr)
            print("The stack st before any append---> ",st)
            st.append(arr[i])
            print("The stack st after append---> ",st)
        if arr[i] > st[-1] and key != 1:
            print("The stack second before any append---> ",second)
            second.append(arr[i])
            print("The stack second after append---> ",second)
            key = 1
        if key == 1:
            if second[-1] > arr[i]:
                st.append(arr[i])
                key=0
            if second[-1] < arr[i]:
                second.append(arr[i])
        

    return st
        


#n  = int(input())
#arr = list(map(int, input().rstrip().split()))
#n=5
#arr= [1,1,1,1,1]
#n=7
#arr=[6,5,8,4,7,10,9]

#Answer is 4
#n = 17
#arr = [20 ,5, 6, 15, 2, 2, 17, 2, 11, 5, 14, 5, 10, 9, 19, 12, 5]


# answer is 5
n=14
arr= [11, 7, 19, 6, 12, 12, 8, 8, 7, 1, 10, 15, 5, 12]
t=0
while True:
    len1 = len(arr)
    print("Array before entering the function",arr)
    arr = calc(arr)
    print("Array as a result of the function",arr)
    print("------------------------------------------------------------------------------")
    len2 = len(arr)
    if len1 ==len2:
        break
    if len1 != len2:
        t = t+1
print(t) 
            