from Benchmark.compare_a_b import Compare

"""
The most basic of list comprehensions, transforming a formal "for" loop into a
one line comprehension.
"""


# Done with a formal for loop.
def for_loop():
    my_new_list_from_loop = []
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        my_new_list_from_loop.append(i)
    return my_new_list_from_loop


# Done with list comprehension
def list_comp():
    return [i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# Compare results

compare = Compare(for_loop, list_comp)
compare.print_results()
