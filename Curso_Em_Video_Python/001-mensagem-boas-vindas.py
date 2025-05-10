# Crie um script em Python que leia o nome de uma pessoa
# e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

#Leitura de dados + Verificação de possíveis erros
while True:
    print('-------------------')
    nome = input('Digite o seu nome: ').strip().capitalize()
    print('-------------------')
    if nome.replace(' ', '').isalpha(): # Retira todos os espaços e verifica se há apenas letras.
        break # Se é valido sai do looping.
    print("Por favor! Digite apenas letras!")

# Exibição de resultados
print(f'Bem-Vindo(a)\033[33m {nome}\033[m, é um prazer imenso conhecê-lo(a).')
