#!python
import random

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    
    => The running time complexity of counting sort is O(n+k) where n is the number of items
    being sorted and k is the range item values, which also represents the length
    of the counting array.
    
    TODO: Memory usage: ??? Why and under what conditions?
    
    => For an in-place sorting case where the original array is mutated, the memory usage is O(k).
    If the original array is preserved and an auxiliary output list is used, then the memory 
    usage is O(n+k).
    """
    
    """
    FIXME: In the future, this should be improved to take any input type if possible.
    All of the integer tests pass as required, but none of the string cases pass in the test file
    """
    
    if len(numbers) <= 1:
        return numbers
    
    """
    This code generates a second output list rather than mutating the original list.
    """
    
    # # TODO: Find range of given numbers (minimum and maximum integer values)
    
    # # Assume that we are not provided the minimum and maximum values of data, so we
    # # must iterate over the list to find them.
    
    # min = numbers[0]
    # max = numbers[0]
    # output_list = [] # generate placeholder output list for sorted items
    
    # for number in numbers:
    #     # output_list.append(0)
    #     if number < min:
    #         min = number
    #     if number > max:
    #         max = number
        
    # count_list = []
    # for i in range(min, max + 1):
    #     count_list.append(0)
    
    # # TODO: Loop over given numbers and increment each number's count
    # for number in numbers:
    #     count_list[number - min] += 1

    # # TODO: Loop over counts and append that many numbers into output list
    # for i in range(len(count_list)):
    #     for j in range(count_list[i]):
    #         output_list.append(i + min)

    # return output_list
    
    # FIXME: Improve this to mutate input instead of creating new output list
    
    """
    This code mutates the input list rather than generating a second output list.
    """

    # TODO: Find range of given numbers (minimum and maximum integer values)
    
    min = numbers[0]
    max = numbers[0]
    
    # Assume that we are not provided the minimum and maximum values of data, so we
    # must iterate over the list to find them.
    
    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number
            
    count_list = []
    for i in range(min, max + 1):
        count_list.append(0)
    
    # TODO: Create list of counts with a slot for each number in input range
    
    for number in numbers:
        count_list[number - min] += 1
    
    # TODO: Loop over counts and append that many numbers into output list
    
    index = 0
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            numbers[index] = i + min
            index += 1
            
    return numbers
    
def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

# if __name__ == '__main__':
    # test_items_a = ['A']
    # test_items_b = [5, 3]
    # test_items_c = ['B', 'C', 'A']
    # test_items_d = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
    # test_items_e = 'one fish two fish red fish blue fish'.split()
    # test_items_f = random.choices(range(10), k=15)
    # test_items_f = [1,3,7,5,2,3,1,1,8,5,6,2,4,5,6,2,5,7,3,2]
    
    # print(merge_sort(test_items_a))
    # print(merge_sort(test_items_b))
    # print(merge_sort(test_items_c))
    # print(merge_sort(test_items_d))
    # print(counting_sort(test_items_e))
    # print(test_items_f)
    # print(sorted(test_items_f))
    # print(counting_sort(test_items_f))
    # assert counting_sort(test_items_f) == sorted(test_items_f)