def calc(arr):
	i=0
	while i < len(arr)-1:
		if arr[i] < arr[i+1]:
			print("comparision between {} < {}".format(arr[i],arr[i+1]))
			arr.pop(i+1)
			i=i+1
			
			print("Value of i inside the loop---------->",i)
		else:
			i=i+1
			print("value of i in the else condition===",i)
	print("Value of i after the function ----------------->",i)
	print("The array after the function call and length ",arr,len(arr))

	return arr



n = 7
arr=[6,5,8,4,7,10,9]
#n= 5
#arr=[3,6,2,7,5]
#n=4
#arr=[3,2,5,4]
k =1
t=0
print(arr)
while k >0:
	len1 = len(arr)
	print("========================================================================")
	print("The array before the function call ",arr)
	arr = calc(arr)
	if len1 == len(arr):
		
		break
	
	t=t+1
print(t)
