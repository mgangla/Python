
def linear_search(arr ,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

my_list= [29, 87, 89, 21, 23, 17, 11, 10, 14]
my_target = 17

result = linear_search(my_list,my_target)

if result != -1:
    print (f"Target {my_target} found at index {result} ")

else :
    print (f"Target {my_target} not found in the list   ")
