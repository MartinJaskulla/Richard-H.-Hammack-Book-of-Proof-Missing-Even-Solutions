from python.cartesian_product import cartesian_product

A = [0, 1]
B = [1]

result = cartesian_product([A, A, A, A])
print('\{' + ",".join(map(str, result)).replace("[", "(").replace("]", ")").replace("'", "") + '\}')
