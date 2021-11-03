from src.programaIdade import *

#teste simples python puro s/ Framework
#testa se menor de idade
def test_idade():
    try:
        #print(defineIdade(12))
        result = defineIdade(12)
        assert result == "Voce e menor de idade"
        print('programaIdade rodou com sucesso em defineIdade')
    except:
        print('programaIdade ERRO em defineIdade')

#Teste s/Framework com formatação:
#testa se maior de idade
assert defineIdade(19) == "Voce e maior de idade", 'Erro no resultado de defineIdade: {}'.format(defineIdade(19))

test_idade()