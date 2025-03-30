from os import system, name  #Funções usadas para limpar a tela do terminal.

def limpaTela(): 
	"""
	Função responsável por limpar o terminal.

	Retorno:
		Função não retorna nada.
	"""
	if name == 'nt':
		system('cls')
	else:
		system('clear')

def telaAbertura():
	"""
	Função responsável por exibir uma "tela" de boas-vindas aos usuários.

	Retorno:
		Função não retorna nada.
	"""
	RST     = '\033[00m'
	RED     = '\033[31m'
	BLUE    = '\033[34m'
	limpaTela()
	print(BLUE)
	print("Seja Bem Vindo à Padaria da Ufes!")
	print()
	print(RED)
	_ = input("--> Enter para continuar...")
	print(RST)

def maquina(p1, p2, p3, p4, p5):
	"""
	Função responsável por exibir as opções disponíveis ao usuário.

	Parâmetros:
		p1 = Produto 1;
		p2 = Produto 2;
		p3 = Produto 3;
		p4 = Produto 4;
		p5 = Produto 5.
	
	Retorno:
		Função não retorna nada.
	"""
	RST     = '\033[00m'
	CYAN    = '\033[36m'
	RED     = '\033[31m'
	print(CYAN) 
	print("+" + "-"*50 + "+")
	print("|                  PADARIA UFES                    |")
	print("+" + "-"*50 + "+")
	print("|" + " "*50 + "|")
	if p1 > 0:
		print("| 1 - Pão de sal(unid)......................R$1,10 |")
	else:
		print("| 1 - Pão de sal(unid)................Indisponivel |")
	if p2 > 0:
		print("| 2 - Pão de queijo(unid)...................R$3,50 |")
	else:
		print("| 2 - Pão de queijo(unid).............Indisponivel |")
	if p3 > 0:
		print("| 3 - Café expresso(180mL)..................R$1,50 |")
	else:
		print("| 3 - Café expresso(180mL)............Indisponivel |")
	if p4 > 0:
		print("| 4 - Capuccino(250mL)......................R$2,50 |")
	else:
		print("| 4 - Capuccino(250mL)................indisponivel |")
	if p5 > 0:
		print("| 5 - Suco(500mL)...........................R$4,99 |")
	else:
		print("| 5 - Suco(500mL).....................indisponivel |")
	print("|" + " "*50 + "|")
	print("+" + "-"*50 + "+")
	print("| 6 - Informações internas                         |")
	print("| 7 - Finalizar                                    |")
	print("+" + "-"*50 + "+")
	print(RST)
	compra(p1, p2, p3, p4, p5)

def compra(p1, p2, p3, p4, p5):
	"""
	- Função responsável por gerenciar a escolha do usuário diante das opções oferecidas pela função Maquina.
	Se todos os produtos estiverem indisponiveis, será impresso uma mensagem informando a indisponibilidade de protutos
	e o programa será fechado.

	- Se a opção selecionada estiver em estoque, o programa realizará as etapas de recebimento do dinheiro e devolução do troco,
	o estoque diminui e é executado a função continuar_compra. Porém se a opção selecionada estiver sem estoque, 
	será impresso uma mensagem informando a indisponibilidade deste produto e será executado a função continuar_compra.

	- Se a opção 6 for selecionada, será impresso as informações internas da máquina.
	
	- Se a opção 7 for selecionada, será finalizado o programa.

	Parâmetros:
		p1 = Produto 1;
		p2 = Produto 2;
		p3 = Produto 3;
		p4 = Produto 4;
		p5 = Produto 5.
	
	Retorno:
		Função não retorna nada.
	"""
	RST     = '\033[00m'
	YELLOW  = '\033[1;93m'
	GREEN = '\033[32m'
	BLACK = '\033[3;30m'
	BLUE    = '\033[34m'
	RED    = '\033[31m'
	print(YELLOW)
	if p1 == 0 and p2 == 0 and p3 == 0 and p4 == 0 and p5 == 0:
		print(f"{BLACK}Sinto muito, mas estamos sem estoque no momento :/")
		print("Volte mais tarde")
		infoInternas(p1, p2, p3, p4, p5)
		exit()
	else:
		x = leValor(int, "Escolha a opção: ")
		if x == 1:
			if p1 > 0:
				print(f"{BLUE}Você escolheu 'Pão de sal'")
				print(f"Preço: R$1,10{YELLOW}")
				print()
				troco(1.10, pagamento(1.10))
				p1-=1
				continuar_compra(p1, p2, p3, p4, p5)
			else:
				print(f"{BLACK}Infelizmente o Pão de sal acabou.")
				continuar_compra(p1, p2, p3, p4, p5)
		elif x == 2:
			if p2 > 0:
				print(f"{BLUE}Você escolheu 'Pão de queijo'")
				print(f"Preço: R$3,50{YELLOW}")
				print()
				troco(3.50, pagamento(3.50))
				p2-=1
				continuar_compra(p1, p2, p3, p4, p5)
			else:
				print(f"{BLACK}Infelizmente o Pão de queijo acabou.")
				continuar_compra(p1, p2, p3, p4, p5)
		elif x == 3:
			if p3 > 0:
				print(f"{BLUE}Você escolheu 'Café expresso(180mL)'")
				print(f"Preço: R$1,50{YELLOW}")
				print()
				troco(1.50, pagamento(1.50))
				p3-=1
				continuar_compra(p1, p2, p3, p4, p5)
			else:
				print(f"{BLACK}Infelizmente o Café acabou.")
				continuar_compra(p1, p2, p3, p4, p5)
		elif x == 4:
			if p4 > 0:
				print(f"{BLUE}Você escolheu 'Capuccino(250mL)'")
				print(f"Preço: R$2,50{YELLOW}")
				print()
				troco(2.50, pagamento(2.50))
				p4-=1
				continuar_compra(p1, p2, p3, p4, p5)
			else:
				print(f"{BLACK}Infelizmente o Capuccino acabou.")
				continuar_compra(p1, p2, p3, p4, p5)
		elif x == 5:
			if p5 > 0:
				print(f"{BLUE}Você escolheu 'Suco'")
				print(f"Preço: R$4,99{YELLOW}")
				print()
				troco(4.99, pagamento(4.99))
				p5-=1
				continuar_compra(p1, p2, p3, p4, p5)
			else:
				print(f"{BLACK}Infelizmente o Suco acabou.")
				continuar_compra(p1, p2, p3, p4, p5)
		elif x == 6:
			infoInternas(p1, p2, p3, p4, p5)
			_ = input(f"{RED}--> Enter para continuar...{RST}")
			limpaTela()
			maquina(p1, p2, p3, p4, p5)
		elif x == 7:
			infoInternas(p1, p2, p3, p4, p5)
			print(f"{GREEN}Volte sempre!")
			print(RST)
			exit()
		else:
			print(f"{RED}Digite uma opção válida{RST}")
			compra(p1, p2, p3, p4, p5)
	

def faturamento(p1, p2, p3, p4, p5):
	"""
	Função responsável por calcular o faturamento da máquina de acordo com o estoque dos produtos disponiveis.

	Parâmetros:
		p1 = Produto 1;
		p2 = Produto 2;
		p3 = Produto 3;
		p4 = Produto 4;
		p5 = Produto 5.

	Retorno:
		Retorna o faturamento total da máquina.
	"""
	fp1 = (5 - p1)*1.10
	fp2 = (5 - p2)*3.50
	fp3 = (5 - p3)*1.50
	fp4 = (5 - p4)*2.50
	fp5 = (5 - p5)*4.99
	ftotal = fp1 + fp2 + fp3 + fp4 + fp5
	return ftotal

def continuar_compra(p1, p2, p3, p4, p5):
	"""
	Função responsável por perguntar ao cliente se ele quer realizar uma nova operação ou finalizar a compra.

	Parâmetros:
		p1 = Produto 1;
		p2 = Produto 2;
		p3 = Produto 3;
		p4 = Produto 4;
		p5 = Produto 5.

	Retorno:
		Função não retorna nada.
	"""
	RST   = '\033[00m'
	GREEN = '\033[32m'
	RED   = '\033[31m'
	VIOLET  = '\033[35m'
	print(RST)
	x = leValor(str, f"{VIOLET}Deseja continuar comprando?(S/N) ")
	if x == "S" or x == "s":
		limpaTela()
		maquina(p1, p2, p3, p4, p5)
	elif x == "N" or x == "n":
		infoInternas(p1, p2, p3, p4, p5)
		print(f"{GREEN}Volte sempre!")
		print(RST)
		exit()
	else:
		print(RED)
		print(f"Valor invalido{RST}")
		continuar_compra(p1, p2, p3, p4, p5)

def infoInternas(p1, p2, p3, p4, p5):
	"""
	Função responsável por exibir as informações internas da máquina(estoque de produtos e faturamento total).

	Parâmetros:
		p1 = Produto 1;
		p2 = Produto 2;
		p3 = Produto 3;
		p4 = Produto 4;
		p5 = Produto 5.
	
	Retorno:
		Função não retorna nada.
	"""
	PURPLE = '\033[95m'
	BLUE   = "\033[34m"
	RST    = '\033[00m'
	print(BLUE)
	print("-"*15, "Informações Internas", "-"*15)
	print(f"Pão de sal: {p1}")
	print(f"Pão de queijo: {p2}")
	print(f"Café expresso: {p3}")
	print(f"Capuccino: {p4}")
	print(f"Suco: {p5}")
	print("-"*52)
	print(f"{PURPLE}Faturamento: R${faturamento(p1, p2, p3, p4, p5):.2f}{BLUE}")
	print("-"*52)
	print(RST)


def pagamento(preço, soma = 0):
	"""
	Função responsável por verificar o pagamento.
	Se o pagamento realizado for abaixo do preço do produto, a função solicitará um novo pagamento,
	até que o valor inserido seja maior ou igual ao preço do produto escolhido.

	Parâmetros:
		preço = preço do produto;
		soma  = parâmetro opcional, armazena a soma do valor inserido pelo cliente.
	
	Retorno:
		Retorna o valor inserido pelo cliente na máquina.
	"""
	RED   = '\033[31m'
	GREEN = '\033[32m'
	YELLOW  = '\033[1;93m'
	valor = leValor(int and float, "Digite o valor inserido: ")
	if valor < 0:
		print(f"{RED}Valor invalido{YELLOW}")
		return pagamento(preço, soma)
	elif valor >= 10000:
		print(f"{RED}A máquina é incapaz de receber valores acima de R$10.000,00!")
		print(YELLOW)
		return pagamento(preço, soma)
	elif valor+soma < preço:
		return pagamento(preço, round(soma+valor,2))
	else:
		print(GREEN)
		print(f"Você depositou {soma+valor:.2f} reais.")
		return soma+valor

def troco(preço, v_inserido):
	"""
	Função responsável por determinar o valor do troco que será retornado ao cliente.

	Parâmetros:
		preço = preço do produto;
		v_inserido = valor total inserido pelo cliente na máquina.
	
	Retorno:
		Função não retorna nada.
	"""
	VIOLET  = '\033[35m'
	v_troco = v_inserido - preço
	if v_troco >= 0:
		print(f"O seu troco é de {v_troco:.2f} reais")
		print(VIOLET)
		if v_troco > 0:
			print("Pegue o seu troco: ")
			geraTroco(round(v_troco,2))
		

def printNotas(valortroco, nota):
	"""
	Função responsável por imprimir cada nota ou moeda separadamente no terminal, até que todo o troco tenha sido impresso.

	Parâmetros:
		valortroco = valor total do troco;
		nota = nota ou moeda correspondente ao troco.
	
	Retorno:
		Função não retorna nada.
	"""
	if valortroco >= nota:
		print(f"R${nota:.2f}")
		geraTroco(round(valortroco-nota,2))

def geraTroco(troco):
	"""
	Função responsável por dividir o valor total do troco em notas e moedas.

	Parâmetro:
		troco = valor total do troco.
	
	Retorno:
		Função não retorna nada.
	"""
	if troco-100 >= 0:
		printNotas(troco, 100)
	elif troco-50 >= 0:
		printNotas(troco, 50)
	elif troco-20 >= 0:
		printNotas(troco, 20)
	elif troco-10 >= 0:
		printNotas(troco, 10)
	elif troco-5 >= 0:
		printNotas(troco, 5)
	elif troco-2 >= 0:
		printNotas(troco, 2)
	elif troco-1 >= 0:
		printNotas(troco, 1)
	elif troco-0.5 >= 0:
		printNotas(troco, 0.5)
	elif troco-0.25 >= 0:
		printNotas(troco, 0.25)
	elif troco-0.10 >= 0:
		printNotas(troco, 0.10)
	elif troco-0.05 >= 0:
		printNotas(troco, 0.05)
	elif troco-0.01 >= 0:
		printNotas(troco, 0.01)

def leValor(funcaoConv, msg = ""):
	"""
	Função responsável por verificar o tipo de variável que será lido pelo programa.

	Parâmetros:
		funcaoConv = tipo de variável(int, float, str);
		msg = mensagem vazia.

	Retorno:
		Retorna a mensagem digitada quando o tipo de variável digitado for igual ao funcaoConv.
		Quando funcaoConv for diferente do tipo de variável digitado,
		será impresso uma mensagem de erro e retornará a própria função leValor.
	"""
	RED = '\033[31m'
	YELLOW  = '\033[1;93m'
	try:
		return funcaoConv(input(msg))
	except:
		print(f"{RED}ERRO: Tipo inválido")
		print(YELLOW)
		return leValor(funcaoConv, msg)

def main ():
	"""
	Função responsável por dar inicio ao programa. Chama a função de Boas Vindas(telaAbertura) e a função Maquina,
	passando o valor do estoque dos produtos como parâmetros.

	Retorno:
		Função não retorna nada.
	"""
	telaAbertura()
	limpaTela()
	maquina(5, 5, 5, 5, 5)

main()