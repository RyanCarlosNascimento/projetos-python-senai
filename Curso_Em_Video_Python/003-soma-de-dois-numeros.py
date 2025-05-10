# Crie um script Python que leia dois números
# e tente mostrar a soma entre eles.
print('DIGITE DOIS NÚMEROS PARA CALCULAR A SUA SOMA!')
soma = 0

#Leitura de dados + Verificação de possíveis erros
for _ in range (2):
    while True:
        try:
            numero = int(input('Digite um número para o cálculo da adição: '))
            soma += numero
            break
        except ValueError:  # Nesse caso se não digitar valores inteiros, pede-se ao usuário que digite de novo.
            print('Valor inválido! Digite apenas números inteiros.')

# Exibição de resultados
print(f'O valor da soma dos números digitados é:\033[33m {soma}')