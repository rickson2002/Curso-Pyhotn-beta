# Python programa simples de caluladora

#Função para somar dois números
def adicao(num1, num2):
	return num1 + num2

#Função para subtrair dois números
def subtracao(num1, num2):
	return num1 - num2

#Função para multiplicar dois números
def multiplicacao(num1, num2):
	return num1 * num2

#Função para dividir dois números
def divisao(num1, num2):
	return num1 / num2

print("Selecione a operação: -\n" \
		"1. Adicção\n" \
		"2. subtração\n" \
		"3. Multiplicação\n" \
		"4. Divisão\n")


# Receba a opinião do usuário
select = int(input("Selecione a operação que voce deseja:\n1(Adição)\n2(Subtração)\n3(Multiplicação)\n4(Divisão)\nOperação Digitado: "))

number_1 = int(input("Digite o primeiro número: "))

number_2 = int(input("Digite o segundo número: "))

if select == 1:
	print(number_1, "+", number_2, "=",
	
	adicao(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
	
	subtracao(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",

	multiplicacao(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
	
	divisao(number_1, number_2))
else:
	print("Invalido valor, por favor digite novamente!")
