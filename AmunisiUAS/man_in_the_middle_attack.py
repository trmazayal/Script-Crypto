import random

# public keys are taken
# p is a prime number
# g is a primitive root of p
p = 83
g = 5


class A:
	def __init__(self, X):
		# Generating a random private number selected by alice
		self.X = X

	def publish(self):
		# generating public values
		return (g**self.X)%p

	def compute_secret(self, Yb):
		# computing secret key
		return (Yb**self.X)%p


class B:
	def __init__(self,a,b):
		# Generating a random private number selected for alice
		self.a = a
		# Generating a random private number selected for bob
		self.b = b
		self.arr = [self.a,self.b]

	def publish(self, i):
		# generating public values
		return (g**self.arr[i])%p

	def compute_secret(self, Ya, i):
		# computing secret key
		return (Ya**self.arr[i])%p


alice = A(6)
bob = A(10)
dart = B(7,8)

# Printing out the private selected number by Alice and Bob
print(f'Alice selected (Xa) : {alice.X}')
print(f'Bob selected (Xb) : {bob.X}')
print(f'Dart selected private number for Alice (c) : {dart.a}')
print(f'Dart selected private number for Bob (d) : {dart.b}')
print()
# Generating public key values
Ya = alice.publish()
Yb = bob.publish()

YD1 = dart.publish(0)
YD2 = dart.publish(1)
print(f'Alice published (Ya): {Ya}')
print(f'Bob published (Yb): {Yb}')
print()
print(f'Dart published value for Alice (YD1): {YD1}')
print(f'Dart published value for Bob (YD2): {YD2}')
print()

# Computing the secret key
sa = alice.compute_secret(YD1)
sea = dart.compute_secret(Ya,0)
sb = bob.compute_secret(YD2)
seb = dart.compute_secret(Yb,1)
print(f'Alice computed (S1) : {sa}')
print(f'Dart computed key for Alice (S1) : {sea}')
print()
print(f'Bob computed (S2) : {sb}')
print(f'Dart computed key for Bob (S2) : {seb}')
