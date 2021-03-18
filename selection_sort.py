def selectionSort(some_list):
    for j in range(len(some_list)):
        for i in range(len(some_list) - 1, 0 + j, -1): #count down until i = 0, 0 is exclusive. Will not work if i = 1. 
            if some_list[i] < some_list[i-1]:
                some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
    return some_list
num_list = [3,6,7,9,2,1,4,8,5,0]
print(selectionSort(num_list))