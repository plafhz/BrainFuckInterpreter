class BrainFuck:
	def __init__(self, code, tam = 300000):
		self.vector = [0] * tam
		self.pv = 0 # Puntero del vector
		self.contadorCodigo = 0
		self.posicionBucle = 0
		self.posicionFinalBucle = 0
		self.code = code

		self.instrucciones = {
			">" : self.incrementarPuntero,
			"<" : self.decrementarPuntero,
			"+" : self.incrementarByte,
			"-" : self.decrementarByte,
			"." : self.escribir,
			"," : self.leer,
			"[" : self.inicioBucle,
			"]" : self.finalBucle
		}

		self.run()

	def run(self):
		while self.contadorCodigo < len(self.code):
			if self.code[self.contadorCodigo] in self.instrucciones:
				self.instrucciones[self.code[self.contadorCodigo]]()
			self.contadorCodigo += 1

	def incrementarPuntero(self):
		self.pv += 1

	def decrementarPuntero(self):
		self.pv -= 1

	def incrementarByte(self):
		self.vector[self.pv] += 1

	def decrementarByte(self):
		self.vector[self.pv] -= 1

	def escribir(self):
		print chr(self.vector[self.pv]),

	def leer(self):
		self.vector[self.pv] = raw_input()[0]

	def inicioBucle(self):
		self.posicionBucle = self.contadorCodigo
		if self.vector[self.pv] == 0:
			self.contadorCodigo = self.posicionFinalBucle

	def finalBucle(self):
		self.posicionFinalBucle = self.contadorCodigo
		if self.vector[self.pv] != 0:
			self.contadorCodigo = self.posicionBucle

def main():
	while True:
		source = open(raw_input("Src: "), "r")
		bf = BrainFuck(source.read())

if __name__ == '__main__':
	main()