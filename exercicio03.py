i = 0 
listaNome = []
listaCPF = []
listaSenha = []
listaDoador = []

idade = int(input("Insira sua idade: "))
peso = int(input("Insira seu peso: "))
horarioSono = int(input("Insira quantas horas dormiu hoje (ultimas 24 horas): "))


def verificacaoDoador(idade1, peso1, horarioSono1):
    if idade1 < 16 or idade1 > 69:
        return False
    if peso1 > 50:
        return False  
    if horarioSono1 < 6:
        return False
    else:
        return True 

retornoVerificador = verificacaoDoador(idade, peso, horarioSono)

if retornoVerificador == True:
    print("Você esta apto para se tornar um doador de sangue, parabéns!")
else:
    print("Você não esta apto para ser um doador")



#Parte 2 do exercicio 
oferta = input("Você gostaria de se cadastrar? ")
def ofertaCadastro(oferta):
    if oferta.lower() == "sim":
        return True
    else:
        return False 

retornoCadastro = ofertaCadastro(oferta)


if retornoCadastro == True:
    for i in range(5): 
        nomeCompleto = input("Cadastre seu nome completo: ")
        listaNome.append(nomeCompleto)
        cpf = int(input("Cadastre seu CPF: "))
        listaCPF.append(cpf)
        senha = input("Cadastre sua senha: ")
        listaSenha.append(senha)
        doador = input("Você esta apto para ser um doador? ")
        listaDoador.append(doador)
else:
    (print("Voltar outra hora"))


def listasCadastro(lista):
    for i in lista:
        print(i)

listasCadastro(listaNome)
listasCadastro(listaCPF)
listasCadastro(listaSenha)
listasCadastro(listaDoador)

