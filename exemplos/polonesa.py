

class Calculator:
	stack = []

	def run(self,raw):
		words = raw.split(' ')
		print(words)
		for word in words:
			if word == "+":
				self.sum()
			elif word == "-":
				self.sub()
			elif word == "*":
				self.mul()
			elif word == "/":
				self.div()
			else:
				val = int(word)
				self.push(val)
		print( self.pop() )

	def sum(self):
		b = self.pop()
		a = self.pop()
		self.push( a + b )
		print( "{} {} +".format(a,b) )

	def sub(self):
		b = self.pop()
		a = self.pop()
		self.push( a - b )
		print( "{} {} -".format(a,b) )

	def mul(self):
		b = self.pop()
		a = self.pop()
		self.push( a * b )
		print( "{} {} *".format(a,b) )

	def div(self):
		b = self.pop()
		a = self.pop()
		self.push( a / b )
		print( "{} {} /".format(a,b) )

	def push(self,val):
		self.stack.insert(0,val)

	def pop(self):
		return self.stack.pop(0);


def main():
	calculator = Calculator()
	try:
		calculator.run("10 20 + 10 2 / * +")
	except:
		print("error")


main()
