from memory_profiler import profile

@profile
def my_function():
    a = [1] * 1000000  # Create a list with a million elements
    b = [2] * 2000000  # Create another list with two million elements
    del b  # Delete the second list

if __name__ == "__main__":
    my_function()