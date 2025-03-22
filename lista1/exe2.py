def cumsum(t):
    list = []
    aux = 0
    for el in t:
        aux += el
        list.append(aux)
    return list

t = [1, 2, 3]

p1 = cumsum(t)
print("A soma é:",p1)
