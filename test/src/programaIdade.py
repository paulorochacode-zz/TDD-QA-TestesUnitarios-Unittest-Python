idadeUser = 0
maiorIdade = 18
def defineIdade(idadeUser):
    maiorIdadeUser = ""
    if idadeUser >= maiorIdade:
        maiorIdadeUser = 'Voce e maior de idade'
        if __name__ == '__main__' :
            print('Você é maior de idade')
        
    else:
        maiorIdadeUser = 'Voce e menor de idade'
        if __name__ == '__main__' :    
            print('Você é menor de idade')
    return maiorIdadeUser

def pedirIdadeUser():
    idadeUser = int(input("digite sua idade : "))
    idadeUser = defineIdade(idadeUser)

if __name__ == '__main__' :
    pedirIdadeUser()
