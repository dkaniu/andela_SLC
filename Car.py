__author__ = 'kaniu'
class Car():
	car_doors = 4
	num_of_wheels = 4
	type = 'saloon'
	parked_speed = 0
	moving_speed = 77


	def __init__(self, name = 'General', model = 'GM', type = 'type'):
		self.model = model
		self.name = name
		self.type = type

		self.car_wheels = Car.car_wheels
		self.parked_speed = Car.parked_speed

	def car_doors(self):
		if Car.model == 'Porshe' or Car.model == 'Koenigsegg':
			self.car_doors = 2
		else:
			self.car_doors = 4

	def car_wheels(self):
		if Car.type == 'trailer':
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4

	def car_type(self):
		if Car.model == 'Koenigsegg':
			Car.type = 'trailer'

	def drive(self, speed):
		self.moving_speed = speed
	


