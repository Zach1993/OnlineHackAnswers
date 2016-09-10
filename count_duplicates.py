list1 = [1,2,3,4,5,5,6,6,7,8,9,9]


def count_dups(lists):

    set1 = set(lists)
    l1 = list(set1)
    for x in l1:
        lists.remove(x)
    return lists


print(count_dups(list1))


