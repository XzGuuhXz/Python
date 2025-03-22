def dic(k):
    dicionario = {}

    for i in range(1, k + 1):
        dicionario[i] = i ** 2

    return dicionario

k = 15

print(dic(k))
