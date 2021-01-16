
class Car():
	def __init__(self,color,mileage):
		self.color = color
		self.mileage = mileage


class AlwaysBlueCar(Car):
	def __init__(self,*args,**kwargs):
		super().__init__(*args, **kwargs)
		if(args):
			new_args = args + ('extra',)
			print(args,"args",new_args)
		if (kwargs):
			print(kwargs,"kwargs")
			print(self.color,self.mileage)


x = AlwaysBlueCar("blue", mileage="sda")