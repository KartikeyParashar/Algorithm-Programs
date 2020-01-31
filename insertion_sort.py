def insertion_sort(unsorted_list):
    for i in range(1,len(unsorted_list)):
        temp = unsorted_list[i]
        j = i-1
        while j>=0 and unsorted_list[j]>temp:
            unsorted_list[j+1]=unsorted_list[j]
            j-=1
        unsorted_list[j+1] = temp
    return unsorted_list


print(insertion_sort([9,7,5,4,2,1]))