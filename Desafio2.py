        
caract = ['!','@','#','$','%','^','&','*','(',')','-','+']
cont = 0

while True:
    senha = input("Digite sua senha: ")
    list(senha)
    qunt = 0

    for i in range(0, len(senha)):
        if(senha[i] != ""):
            cont += 1

    if cont < 6:
        qunt = 6 - cont
        print("Está faltando",qunt, "caracteres para sua senha!")
    elif not any(i.isdigit() for i in senha):
        print("Falta um número")
    elif not any(i.islower() for i in senha):
        print("Falta um caractere minusculo")
    elif not any(i.isupper() for i in senha):
        print("Falta um caractere Maisculo")
    elif not set(caract) & set(senha):
        print("Falta um caractere especial")
    else:
        break       
print("Senha salva com sucesso!")