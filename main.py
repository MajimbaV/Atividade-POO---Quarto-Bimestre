from classes import *
	
print("Cadastro do Professor:")
user = Professor(input("Nome: "), input("Matrícula: "))

while True:
	print(f'''
 {"-"*20}Agenda de Atividades{"-"*20}
	[1] - Cadastrar Disciplina
	[2] - Cadastrar Atividade
	[3] - Listar Atividades
	[4] - Marcar Atividade Como Concluida
	[5] - Sair
	 ''')
	opção = int(input('''Digite a opção desejada: '''))
	
	if opção == 1:
		user.adcionar_disciplina(input("Nome: "))
	elif opção == 2:
		user.adcionar_atividade(input("Disciplina: "), input("Nome: "), input("Data: "))
	elif opção == 3:
		while True:
			print ('''
	[1] - Atividades Pendentes
	[2] - Atividade Concluidas 
		''')
			listatipo = int(input("Listar: "))
			if listatipo == 1:
				user.listar_abertas()
				break
			elif listatipo == 2:
				user.listar_concluidas()
				break
			else: 
				print ("ERRO: Escolha uma Opção Valida")
	elif opção == 4:
		user.concluir_atividade(input("Disciplina: "),input("Atividade: "))
		
	elif opção == 5:
		break
	else:
		print("Escolha uma opção válida")

print("Fim do Progama")