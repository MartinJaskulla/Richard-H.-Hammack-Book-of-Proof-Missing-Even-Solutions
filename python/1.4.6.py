from power_set import power_set
from cartesian_product import cartesian_product

A = power_set([1,2])
B = power_set([3])

result = cartesian_product([A,B])
formatted = '\{' + ",".join(map(str, result)).replace("[", "\{").replace("]", "\}").replace("'", "") + '\}'

print(result)
print(formatted)