# -*- coding: utf-8 -*-

class Subtracao(object):
	def __init__(self, expressao_esquerda, expressao_direita):
		self.__expressao_esquerda = expressao_esquerda
		self.__expressao_direita = expressao_direita

	@property
	def expressao_esquerda(self):
		return self.__expressao_esquerda

	@property
	def expressao_direita(self):
		return self.__expressao_direita

	def aceita(self, visitor):
		visitor.visita_subtracao(self)	

	def avalia(self):
		return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()


class Soma(object):
	def __init__(self, expressao_esquerda, expressao_direita):
		self.__expressao_esquerda = expressao_esquerda
		self.__expressao_direita = expressao_direita

	@property
	def expressao_esquerda(self):
		return self.__expressao_esquerda

	@property
	def expressao_direita(self):
		return self.__expressao_direita

	def aceita(self, visitor):
		visitor.visita_soma(self)

	def avalia(self):
		return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()


class Numero(object):
	def __init__(self, numero):
		self.__numero = numero

	def aceita(self, visitor):
		visitor.visita_numero(self)

	def avalia(self):
		return self.__numero


if __name__ == "__main__":
	from impressao import Impressao

	expressao_esquerda = Soma(Numero(10), Numero(20))
	expressao_direita = Soma(Numero(5), Numero(2))
	expressao_conta = Soma(expressao_esquerda, expressao_direita)
	print expressao_conta.avalia()

	impressao = Impressao()
	expressao_conta.aceita(impressao)
	print
	
	expressao_esquerda = Subtracao(Numero(100), Numero(20))
	expressao_direita = Soma(Numero(5), Numero(5))
	expressao_conta = Soma(expressao_esquerda, expressao_direita)
	expressao_conta.aceita(impressao)