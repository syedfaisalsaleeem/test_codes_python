
def f1():
	print("Called f1")

def f2(f):
	f()

f2(f1)


def f1(func):
	def wrapper(*args,**kwargs):
		print("Started")
		val = func(*args,**kwargs)
		print("Ended")
		return val

	return wrapper

@f1
def f(a):
 	print(a)

# f = f1(f)
# print(f)
# f()
@f1
def add(x,y):
	return x+y
f("Hi")
print(add(1,5))