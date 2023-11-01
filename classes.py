listadisciplina = {}
listaatividadesabertas = {}
listaatividadesconcluidas = {}

class Disciplina:
	def __init__(self, nome, professor):
		self._nome = nome
		self._professor = professor


class Atividade(Disciplina):
	def __init__(self, disciplina, nome, data):
		self.disciplina = disciplina
		self.nome = nome
		self.data = data

class Professor():
	def __init__ (self, nome, matricula):
		self._nome = nome
		self._matricula = matricula

	def adcionar_disciplina(self, nome):
		if len(listadisciplina) > 0:
			for disciplina in listadisciplina:
				if nome == disciplina.nome:
					return print("Essa disciplina já existe")
				else:
					listadisciplina[nome] = Disciplina(nome, self)
					print("Disciplina Registrada com Sucesso!")
		else:
				listadisciplina[nome] = Disciplina(nome, self)
				print("Disciplina Registrada com Sucesso!")

	def adcionar_atividade(self, disciplina, nome, data):
		if disciplina in listadisciplina:
				if len(listaatividadesabertas) > 0:
					atividades_abertas = list(listaatividadesabertas.values())
					for atv in atividades_abertas:
						if data == atv.data and disciplina == atv.disciplina:
							return print("Já há uma atividade desta disciplina marcada para esta data!")
						else:
							listaatividadesabertas[nome] = Atividade(disciplina, nome, data)
							print("Atividade Registrada com Sucesso!")
				else:
					listaatividadesabertas[nome] = Atividade(disciplina, nome, data)
					print("Atividade Registrada com Sucesso!")
		else:
			print("ERRO: Essa Disciplina Não Existe")
	def concluir_atividade(self, disciplina, atividade):
		if atividade in listaatividadesabertas and listaatividadesabertas[atividade].disciplina == disciplina:
			listaatividadesconcluidas[listaatividadesabertas[atividade].nome] = listaatividadesabertas[atividade]
			listaatividadesabertas.pop(atividade)
			print("Atividade Marcada como Concluida")
		else:
			print("ERRO: Atividade Não Existe")

	def listar_abertas(self):
		atividades_abertas = list(listaatividadesabertas.values())
		print("-"*20, "Atividades Pendentes", "-"*20)
		for atv in atividades_abertas:
			print("-"*60)
			print(f"Disciplina: {atv.disciplina}")
			print(f"Nome: {atv.nome}")
			print(f"Data: {atv.data}")
		print("-"*60)
	def listar_concluidas(self):
		atividades_concluidas = list(listaatividadesconcluidas.values())
		print("-"*18, "Atividades Concluidas", "-"*19)
		for atv in atividades_concluidas:
			print("-"*60)
			print(f"Disciplina: {atv.disciplina}")
			print(f"Nome: {atv.nome}")
			print(f"Data: {atv.data}")
		print("-"*60)


