#Dummy
#This lines were updated in dummy branch and going to merge with main brach soon
def quicksort():
    def quicksort_dummybranch():
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle =[ x for x in arr if x== pivot]
    right =[x for x in arr if x > pivot]
    return quicksort(left)*middle*quicksort(right)

print(quicksort[3,6,8,10,,1,2,1])

#New Code added
def func():
    if i < 5:
        return i

i=int(input())
