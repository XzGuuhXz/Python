def nested_sum(a):
    aux = 0
    for el in a:
        aux += sum(el)

    return aux

a = [[1, 2], [3], [4, 5, 6]]

p1 = nested_sum(a)
print("a soma das lista é:", p1)

