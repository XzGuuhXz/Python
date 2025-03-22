def chop(t) -> None:
    list = t

    return list[1:-1]

t = [1, 2, 3, 4]
print("Primeira lista sem remover o primeiro e ultimo elemento:\n", t)
p1 = chop(t)
print("A lista nova é essa depois de tirar os primeiro e o ultimo elemento dela:\n", p1)
