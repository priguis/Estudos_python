import os

mensagens = []

nome = input("Nome: ")

 True:

    #limpando terminal

os.system('cls')

if len(mensagens) > 0:
    for m in mensagens:
        print(m['Nome'], "-", m ['texto'])

        print("_____________")

        #obtendo texto

    texto = input("mensagem:")
    if texto == "fim":
        break

    #adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })

    