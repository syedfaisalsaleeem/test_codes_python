def foo(required,*args,**kwargs):
	print(required,"required")
	if(args):
		new_args = args + ('extra',)
		print(args,"args",new_args)
	if (kwargs):
		print(kwargs,"kwargs")

x = foo("asds","c",d="d")
