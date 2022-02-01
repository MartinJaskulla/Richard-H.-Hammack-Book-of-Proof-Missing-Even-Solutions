from power_set import power_set
from cartesian_product import cartesian_product

cp = cartesian_product([[1,2], [3]])
result = power_set(cp)
formatted = '\{' + ",".join(map(str, result)).replace("[", "\{").replace("]", "\}").replace("'", "") + '\}'

print(result)
print(formatted)