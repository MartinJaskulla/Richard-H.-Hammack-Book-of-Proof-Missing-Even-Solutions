import math

A = ["pi", "e", 0]
B = [0, 1]


def cartesian_product(sets):
    result = [[]]
    for inputSet in sets:
        new_result = []
        for resultSet in result:
            for number in inputSet:
                new_result.append(resultSet + [number])
        result = new_result
    return result

result = cartesian_product([A, B, B])
print('\{' + ",".join(map(str, result)).replace("[", "(").replace("]", ")").replace("'", "") + '\}')
