def cartesian_product(sets):
    result = [[]]
    for inputSet in sets:
        new_result = []
        for resultSet in result:
            for number in inputSet:
                new_result.append(resultSet + [number])
        result = new_result
    return result