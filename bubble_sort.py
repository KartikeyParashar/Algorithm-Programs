def bubble_sort(unsorted_list):
    for i in range(0,len(unsorted_list)):
        for j in range(0,len(unsorted_list)-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = temp
    return unsorted_list

print(bubble_sort([9,7,6,4,1]))