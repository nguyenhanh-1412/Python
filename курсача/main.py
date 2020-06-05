from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
import matplotlib.pyplot as plt


#Input equation-(Ex: "y = a * x + b")
text = input("calc > ")
# list values
list_x, list_y = [], []
# quantity_point
n = int(input('Quantity point = '))
for i in range(n):
	value_x = input('x = ')
	lexer = Lexer(text, value_x)
	list_x.append(float(value_x))
	tokens = lexer.generate_tokens()
	parser = Parser(tokens)
	tree = parser.parse()
	interpreter = Interpreter()
	value1 = interpreter.visit(tree)
	list_y.append(value1.value)
	print('y = ', value1)
plt.plot(list_x, list_y, "ro-")
plt.show()

