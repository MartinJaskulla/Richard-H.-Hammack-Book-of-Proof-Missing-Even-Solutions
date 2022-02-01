def power_set(set):
    subsets = [[]]
    for element in set:
        for i in range(len(subsets)):
            subset = subsets[i]
            subsets.append(subset + [element])

    return subsets