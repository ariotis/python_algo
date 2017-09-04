from Benchmark.compare_a_b import Compare

"""
Loop through a list and return only elements we're interested in, for example
even numbers.
"""


# Done with a formal for loop.
def for_loop():
    my_new_list_from_loop = []
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if not i % 2:
            my_new_list_from_loop.append(i)
    return my_new_list_from_loop


# Done with list comprehension
def list_comp():
    return [i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9] if not i % 2]

# Compare results

compare = Compare(for_loop, list_comp)
compare.print_results()
