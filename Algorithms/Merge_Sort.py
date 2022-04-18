from pip import main


class MergeSort():

    """ 
    Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.
    
    Using the Divide and Conquer technique, we divide a problem into subproblems. When the solution to each subproblem is ready, 
    we 'combine' the results from the subproblems to solve the main problem.

    Args:
        None
    Attributes:
        None
    Notes:
        Time Complexity

        Best Case Complexity: O(n*log n)
        Worst Case Complexity: O(n*log n)
        Average Case Complexity: O(n*log n)

        Space Complexity
        The space complexity of merge sort is O(n).
    """

    def __init__(self) -> None:
        pass
    

    def merge(self,list1,list2):
        """
        Merge method is used to merge two given arrays lists in an order

        Arguments:
            list1: Pass any list as an argument
            list2: Pass any list as an argument
        Returns:
            The sorted elements of the given list
        """


        merged_list = []
        i = 0
        j = 0

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i +=1
            else:
                merged_list.append(list2[j])
                j +=1

        while i < len(list1):
            merged_list.append(list1[i])
            i += 1

        while j < len(list2):
            merged_list.append(list2[j])
            j += 1

        return merged_list


    def sort(self,list):

        """
        The base idea of sort method is to divide (sub)arrays into halves and sort them recursively. 
        We want to keep doing this as much as possible, i.e. until we end up with subarrays that have only one element:

        Arguments:
            list1: Pass any list as an argument
            list2: Pass any list as an argument
        Returns:
           Split the each list element into single elements 
        """

        if len(list) == 1:
            return list
        mid = len(list)//2

        left_arr = list[:mid]
        right_arr = list[mid:]
        print(left_arr)
        print(right_arr)

        final_list = self.merge(self.sort(left_arr), self.sort(right_arr))
        print(final_list)
        return final_list


if __name__ == '__main__':
    # input string
    list =[23,345,7,16,82,5,5,23]
    
    # Initialise the object
    merge_sort = MergeSort()        
    print(merge_sort.__doc__)

    # Call merge sort method
    merge_sort.sort(list)




















