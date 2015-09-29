import sys

class BrainFuck:
	def __init__(self, code, debug = False):
		self.vector = [0]
		self.pv = 0 # Puntero del vector
		self.contadorCodigo = 0
		self.posicionBucle = []
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

		if not debug:
			self.run()
		else:
			self.runDebug()

	def run(self):
		while self.contadorCodigo < len(self.code):
			if self.code[self.contadorCodigo] in self.instrucciones:
				self.instrucciones[self.code[self.contadorCodigo]]()
			self.contadorCodigo += 1

	def runDebug(self):
		while self.contadorCodigo < len(self.code):
			if self.code[self.contadorCodigo] in self.instrucciones:

				print "Codigo:     ", self.contadorCodigo
				print "Puntero:    ", self.pv
				print "Celda:      ", self.vector[self.pv]
				print "Bucle:      ", self.posicionBucle
				print "Instruccion:", self.code[self.contadorCodigo]
				raw_input("......")

				self.instrucciones[self.code[self.contadorCodigo]]()
			self.contadorCodigo += 1

	def incrementarPuntero(self):
		self.pv += 1
		if self.pv >= len(self.vector): self.vector.append(0)

	def decrementarPuntero(self):
		self.pv -= 1

	def incrementarByte(self):
		self.vector[self.pv] += 1

	def decrementarByte(self):
		self.vector[self.pv] -= 1 if self.vector[self.pv] > 0 else 0

	def escribir(self):
		print chr(self.vector[self.pv]),

	def leer(self):
		try:
			self.vector[self.pv] = ord(raw_input()[0])
		except:
			self.contadorCodigo -= 1

	def inicioBucle(self):
		self.posicionBucle.append(self.contadorCodigo)
		if self.vector[self.pv] == 0:
			self.posicionBucle.pop()
			self.contadorCodigo = self.corcheteCierre()

	def finalBucle(self):
		if self.vector[self.pv] != 0:
			self.contadorCodigo = self.posicionBucle[-1]
		else:
			self.posicionBucle.pop()

	def corcheteCierre(self): # busca el corchete de cierre de la posicion actual
		abierto = False
		for i in range(self.contadorCodigo + 1, len(self.code)):
			if self.code[i] == "[":
				abierto = True
			elif self.code[i] == "]" and abierto:
				abierto = False
			elif self.code[i] == "]" and not abierto:
				return i

def main():
	debug = False

	for arg in sys.argv:
		if arg == "-d":
			debug = True

	try:
		source = open(sys.argv[1], "r")
	except:
		print "Archivo fuente no encontrado."
		sys.exit()

	bf = BrainFuck(source.read(), debug = debug)

if __name__ == '__main__':
	main()