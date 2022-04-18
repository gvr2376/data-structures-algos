# bubble sort algorithm
def bubble_sort(list):
    """
    Bubble Sort Algorithm

    This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order.
    This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items.

    Time Complextity: Ο(n2)

    Arguments:
        list: Pass any list as an argument
    Returns:
        The sorted elements of the given list
    """


    for i in range(0,len(list)):
        for j in range(0,len(list)-1-i):
            print('before swap --> ', list)
            if list[j] > list[j+1]:
                var_tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = var_tmp
                print('after swap --> ', list)
    return list


# Define a list
my_list = [2,4,1,7,3]

# Pass the list to function bubble sort
bubble_sort(list=my_list)
print(bubble_sort.__doc__)