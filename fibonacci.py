atual = 0
anterior = 1

for i in range(10):
    print(atual)
    atual, anterior= anterior, atual + anterior