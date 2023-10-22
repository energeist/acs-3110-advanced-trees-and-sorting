#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    
    Time complexity is O(n) under all conditions as the function must iterate over a full list
     
    TODO: Memory usage: ??? Why and under what conditions?
    
    Space complexity is O(1), no values are stored or mutated
    """

    # TODO: Check that all adjacent items are in order, return early if so
    
    if len(items) in [0,1]: # early return because 0 & 1 item lists are trivially sorted
        return True
    
    for i in range(len(items)-1): 
        if items[i] > items[i+1]: 
            return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    
    The time complexity of bubble sort is:
    Worst case - O(n^2) because there are two loops to iterate through
    Average case - same as above
    Best case - O(n) if the list is already sorted
    
    TODO: Memory usage: ??? Why and under what conditions?
    
    Space complexity is always O(1) as this is an in-place sorting algorithm and does not need to store
    additional information to sort.  Some small variables are held for tracking but there are no lists
    or dictionaries used.
    """
    
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    
    if len(items) in [0,1]: # early return for sorted cases
        return items
    
    for i in range(len(items)):
        sorted_order = True
        
        for j in range(len(items)-i-1):
            previous_item = items[j]
            current_item = items[j+1]
            
            if current_item < previous_item: # not in order
                items[j+1], items[j] = items[j], items[j+1] # swap values
                sorted_order = False # swap has occurred
                
        if sorted_order:
            return items                

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    
    Time complexity:
    Worst case - O(n^2) - algorithm has to iterate over a double loop
    Average case - O(n^2) - same a above
    Best case - O(n^2) - algorithm must complete nested loop traversal regardless of whether the list
    is sorted or not, since we are picking a minimum and comparing to each following value, then moving
    to the next in the list and performing the same action until all values are compared. 
    
    TODO: Memory usage: ??? Why and under what conditions?
    
    Space complexity is always O(1), there are only small tracking variables stored.
    """
    
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    if len(items) in [0,1]: # early return for sorted cases
        return items
    
    for i in range(len(items)): # iterate over the list of items
        min_index = i # initially assume the minimum value for the iteration is the first item chosen 
        
        for j in range(i+1, len(items)): # iterate over the remaining items
        
            if items[j] < items[min_index]: # if a smaller value is found
                min_index = j # set that value to the minimum
        
        items[min_index], items[i] = items[i], items[min_index] 
        # swap the smallest value found with the starting position of this iteration
    
    return items
    
def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    
    Time complexity is:
    worst case - O(n^2) because the algorithm must always iterate through two loops.
    average case - O(n^2), as above
    best case - O(n) if the list is already sorted 
    
    TODO: Memory usage: ??? Why and under what conditions?
    
    Space complexity is always O(1), single values are stored in a few variables for tracking, otherwise
    the list is sorted in place.
    """
    
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    
    if len(items) in [0,1]: # early return for sorted cases
        return items
    
    for i in range(1, len(items)): # start counting from the second item in the list
        key = items[i] # pick a pivot point that is being sorted on
        j = i - 1 # start comparing against the previous item
        
        while j >= 0 and key < items[j]: # if the pivot is smaller than the previous item then it must swap
            items[j + 1], items[j] = items[j], items[j + 1] # swap
            j -= 1 # move backwards through list to keep checking whether pivot item is in the right place
    return items
            
    
