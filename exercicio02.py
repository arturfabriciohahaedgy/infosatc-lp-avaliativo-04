palavraNormal = input("Insira uma palavra: ")
palavraInvertida = input("Insira o inverso da palavra anterior: ")

#optei por usar um input pra deixar o programa mais correto...
#a palavra inversa não precisa ser necessariamente a segunda como mostra o "Def" abaixo, coloquei desse jeito puramente para deixar mais claro a instrução do programa...

def parametroInvertido(palavra1, palavra2):
    if palavra2 == palavra1[::-1] or palavra1 == palavra2[::-1]:
        return True 
    else:
        return False 
    

retornoInverido = parametroInvertido(palavraNormal, palavraInvertida)

if retornoInverido == True:
    print("Uma palavra é a inversão de outra.")
else:
    print("Uma palavra não é a inversão de outra, favor reinicar o programa.")