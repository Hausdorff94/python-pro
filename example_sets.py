def remove_duplicates(lst):
    """
    Remove duplicates from a list.
    """
    without_duplicates = []
    for e in lst:
        if e not in without_duplicates:
            without_duplicates.append(e)
    return without_duplicates

def remove_duplicates_using_set(lst):
    """
    Remove duplicates from a list using set.
    """
    return list(set(lst))

def run():
    """
    Run the example.
    """
    lst = [1, 1, 9, 4, 5, 10, 7, 8, 9, 10]
    print(lst)
    print(remove_duplicates(lst))
    print(remove_duplicates_using_set(lst))


if __name__ == '__main__':
    run()
