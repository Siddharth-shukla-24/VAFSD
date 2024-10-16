def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index]==target:
            return index
arr=[20,54,15,55,47]
target = input()
result = linear_search(arr,target)
if result==1: 
    print(f"Element found at : {result}")
else:
    print("not found")