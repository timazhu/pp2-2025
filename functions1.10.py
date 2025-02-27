#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set

def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

print(unique_elements([2, 3, 3, 4, 5, 4, 4, 6, 7, 7, 8, 9]))  #[2, 3, 4, 5, 6, 7, 8, 9]