def extract(sample_dict, keys):
    nova_lista = {}

    for chave in keys:
        if chave in sample_dict:
            nova_lista[chave] = sample_dict[chave]

    return nova_lista

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
keys = ["name", "salary"]

extr = extract(sample_dict, keys)
print(extr)
