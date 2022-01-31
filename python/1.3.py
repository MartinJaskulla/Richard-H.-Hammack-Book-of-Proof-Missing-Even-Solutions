def power_set(set):
    subsets = [[]]
    for element in set:
        for i in range(len(subsets)):
            subset = subsets[i]
            subsets.append(subset + [element])

    return subsets

result = power_set([[0,1], [0,1,[2]], [0]])
print(result)
formatted = '\{' + ",".join(map(str, result)).replace("[", "\{").replace("]", "\}").replace("'", "") + '\}'
print(formatted)