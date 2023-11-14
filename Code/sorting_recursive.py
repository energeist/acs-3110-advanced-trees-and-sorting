#!python
import random

from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    
    TODO: Running time: ??? Why and under what conditions?
    
    => running time complexity of the merge function is O(n) because it has to iterate over the length of both lists.
    
    TODO: Memory usage: ??? Why and under what conditions?
    => memorty usage of the merge function is O(n) because it creates a new list of items with length n to return.
    """
    
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    
    new_list = []
    
    while len(items1) > 0 and len(items2) > 0:
        
        if items1[0] <= items2[0]:
            new_list.append(items1.pop(0))
        else:
            new_list.append(items2.pop(0))
    
    if len(items1) == 0:
        new_list.extend(items2)
    elif len(items2) == 0:
        new_list.extend(items1)
        
    return new_list

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    
    TODO: Running time: ??? Why and under what conditions?
    
    => The running time of this iterative split_sort_merge is dependent on the sorting algorithm used.  With insertion sort, the worst and average cases are O(n^2) and the best case is O(n).
    
    TODO: Memory usage: ??? Why and under what conditions?
    
    => The memory usage of this iterative split_sort_merge is O(n) because the function creates a new list of items with length n to return.
    
    """
    
    # TODO: Split items list into approximately equal halves
    
    middle = len(items) // 2
    half_one = items[:middle]
    half_two = items[middle:]
    
    # TODO: Sort each half using any other sorting algorithm
    
    # sort with insertion sort
    half_one = insertion_sort(half_one)
    half_two = insertion_sort(half_two)
    
    # TODO: Merge sorted halves into one list in sorted order
    
    return merge(half_one, half_two) 
    
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    
    TODO: Running time: ??? Why and under what conditions?
    
    => The time complexity of merge sort is O(n log n) because the function calls recursively on split lists until the base case is reached (log n time) and each recursive call runs in O(n) time as it iterates over the length of a list of items, which yields O(n log n) time complexity.
    
    TODO: Memory usage: ??? Why and under what conditions?
    
    => Memory usage of merge sort is generally O(n) because the function calls recursively on split lists and is ~typically~ not an in-place sorting algorithm, so it uses memory to store the split lists instead of directly mutating the original list.  Several more complicated algorithms have been proposed to reduce the memory requirements of merge sort, but they have various complicated conditions and tradeoffs, and are not commonly used.
    """
    
    # TODO: Check if list is so small it's already sorted (base case)
    
    if len(items) <= 1:
        return items # base case, return early
    
    # TODO: Split items list into approximately equal halves
    
    middle = len(items) // 2
        
    # TODO: Sort each half by recursively calling merge sort
        
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    
    # TODO: Merge sorted halves into one list in sorted order
    
    # clear the original array and return the sorted version of it for tests
    
    items.clear()
    items.extend(merge(left, right))    
      
    return items # use the merge helper method we wrote earlier      

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    
    => Running time for the partition helper function is O(n) because it has to iterate through the entire list once.
    
    TODO: Memory usage: ??? Why and under what conditions?
    
    => Memory usage for the partition helper function is O(1) because it only uses a constant 
    amount of memory for temp/counter variables (i, j, and pivot)
    """
    
    # TODO: Choose a pivot any way and document your method in docstring above
    
    """
    => Originally I had started by choosing the pivot as the middle element in the list but this had issues when testing with duplicate values.
    After some research, I found that the Hoare partitioning scheme is a simple and effective way to choose a pivot that deals with duplicates well.
    The Hoare partitioning scheme chooses the pivot as the first element in the list, and then swaps elements on the left and right sides of the list.
    The left side of the list contains elements that are smaller than the pivot, and the right side of the list contains elements that are larger than the pivot.
    """
    
    pivot = items[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while items[i] < pivot:
            i += 1

        j -= 1
        while items[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Swap elements at indices i and j.
        items[i], items[j] = items[j], items[i]
            
def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    
    TODO: Best case running time: ??? Why and under what conditions?
    
    => The best case running time complexity of quick sort is O(n log n) because the function
    calls recursively on split lists until the base case is reached (log n time) and each recursive
    call runs in O(n) time as it iterates over the length of a list of items, which yields
    O(n log n) time complexity.
    
    TODO: Worst case running time: ??? Why and under what conditions?
    
    => The worst case running time complexity of quick sort is O(n^2) when the list is sorted or
    nearly sorted, or the pivot choice is poor.  If the pivot choice is poor then the recursive
    splitting of the list of items approximately O(n) time, and iterating over the list of items
    is also O(n) time.  This yields (O (n) * (n)) = O(n^2) time complexity -> think area of a n * n square.
     
    TODO: Memory usage: ??? Why and under what conditions?
    
    => Memory usage is on the order of O(log n) because the function calls recursively on split lists,
    which adds call frames to the call stack.
    """
    
    # TODO: Check if high and low range bounds have default values (not given)
    
    if low is None:
        low = 0
        
    if high is None:
        high = len(items) - 1
        
    if low < high:
        # Find the pivot index such that elements smaller than pivot are on the left,
        # and elements greater than pivot are on the right.
        pivot_index = partition(items, low, high)

        # Recursively sort the sublists on both sides of the pivot.
        quick_sort(items, low, pivot_index)
        quick_sort(items, pivot_index + 1, high)
        
    return items
    
if __name__ == '__main__':
    pass
    #  merge sort test cases
    # items1 = [1, 3, 5]
    # items2 = [2, 4, 6, 7]
    # items3 = [2, 4, 6, 7]
    # items4 = [1, 3, 5]
    # items5 = ["a", "b", "e"]
    # items6 = ["b", "c", "d", "f"]
    # print(merge(items1, items2))
    # print(merge(items3, items4))
    # print(merge(items5, items6))
    
    test_list = [1, 5, 3, 2, 7, 6, 4] # odd number
    print("split_sort_merge")
    print(split_sort_merge(test_list))
    print("merge_sort")
    print(merge_sort(test_list))
    test_list2 = [1, 5, 3, 2, 7, 6, 8, 4] # even number
    print("split_sort_merge")
    print(split_sort_merge(test_list2))
    print("merge_sort")
    print(merge_sort(test_list2))
    test_list3 = ["a", "e", "c", "b", "d", "f"]
    print("split_sort_merge")
    print(split_sort_merge(test_list3))
    print("merge_sort")
    print(merge_sort(test_list3))
    test_items_a = ['A']
    test_items_b = [5, 3]
    test_items_c = ['B', 'C', 'A']
    test_items_d = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
    test_items_e = 'one fish two fish red fish blue fish'.split()
    test_items_f = random.choices(range(10), k=10)
    
    print(merge_sort(test_items_a))
    print(merge_sort(test_items_b))
    print(merge_sort(test_items_c))
    print(merge_sort(test_items_d))
    print(merge_sort(test_items_e))
    print(merge_sort(test_items_f))