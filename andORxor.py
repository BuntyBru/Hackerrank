# implementation of Stack
class Stack:
    def __init__(self):
         self.items = []

    def isEmpty(self):
         return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)

    def __str__(self):
        return str(self.items)


#the Calculating function
def tea(a,b):
    if a < b:
        m1 = a
        m2 = b
    if b < a:
        m1 = b
        m2 = a
    #return  (((m1 & m2) ^ (m1 | m2)) & (m1 ^ m2))
    return m1^m2

Stack2 = Stack()
Stack1 = Stack()



#Stack2function where the stack2 is loaded everytime with indexes
def stack2Function(length):
    for i in range(length):
        Stack2.push(i)
    return Stack2
    

#n = 10
#l = [76969694 ,71698884,32888447,31877010 ,65564584 ,87864180 ,7850891,1505323,17879621,15722446]
n=5
a = [5, 2, 1, 4, 3]
#n = 5
#l = [9,8,3,5,7]
#n=10
#l = [4547989, 39261040, 94929326, 38131456, 26174500, 7152864, 71295827, 77784626, 89898294, 68006331]
#n = 20000
#l =
#arr_rev =l[::-1]
#ans = []
#final = -1
#if Stack1.isEmpty():
#    item = arr_rev.pop()
#    Stack1.push(item)

#while len(arr_rev) > 0:
    #print("Entering into the loop")
#    ans.append(tea(Stack1.peek(), arr_rev[-1]))
#    if arr_rev[-1] < Stack1.peek():
#        Stack1.pop()
#        item1 = arr_rev.pop()
#        Stack1.push(item1)
#    else:
#        item1 = arr_rev.pop()
 #       Stack1.push(item1)

#print(max(ans))


s = [0]
maxi = 0

def cal(a, b):
    return a ^ b

for i in range(1, n):
    while len(s) > 0:
        print("The length of s is", len(s))
        print("The value of maxi before comparision ",maxi)
        print("The value of a[i] is ",a[i])
        print("The value of S =======>",s)
        print("The value of s[len(s) - 1] is ",s[len(s) - 1])
        print("The value of a[s[len(s) - 1]] is ",a[s[len(s) - 1]])
        maxi = max(maxi, cal(a[i], a[s[len(s) - 1]]))
        print("The value of maxi ------------------------------->",maxi)
       
        if a[s[len(s) - 1]] > a[i]:
            s.pop()
        else:
            break
        print("The contents of s after the loop",s)
        

    s.append(i)
    print("Value of S after appending ",s)
    print("===============================================================")

print (maxi)