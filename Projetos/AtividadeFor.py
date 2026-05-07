frutas = ["maçã", "banana", "laranja", "uva", "morango"]

fruta_favorita = input("Qual é a sua fruta favorita?:")

if fruta_favorita not in frutas:
    print("Desculpe, essa fruta não está na lista.")
    print("Adicionando...")
    frutas.append(fruta_favorita)
    exit()
for posicao, frutas in enumerate(frutas):
    if frutas == fruta_favorita:

        posicao_fruta_favorita = posicao
        break
    
print(f"A posição da sua fruta favorita é: {posicao_fruta_favorita}")