from django.test import TestCase

# Create your tests here.


def a(func):
	def b(*a, **c):
		print(a)
		print(c)
		a = (2,5)
		return func(*a, **c)
	return b

@a
def d( n ,m):
	print(n,m)

d(1,2)