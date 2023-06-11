class soda:

	def __init__(self, ingredient):
		if example(ingredient):
			self.ingredient = ingredient
		else:
			self.ingredient = None
	def show_my_drink(self):
		if self.ingredient:
			print(f'Газировка и {self.ingredient}')
		else:
			print('Обычная газировка')

drink_1 = soda()
drink_2 = soda('ананас')
drink_3 = soda(4)
drink_1.show_my_drink()
drink_2.show_my_drink()
drink_3.show_my_drink()	