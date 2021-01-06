# number of months elapsed
n = 35
# number of pairs in each generation
k = 5
"""
# using object oriented programming
# Considering it takes one month to reach a reproductive age
class Rabbit:
	def __init__(self, time = 0 , offspring = k):
		self.age = 0
		self.time = time
		self.offspring = offspring
		
	def reproduce(self):
		if self.age > 0:
			return self.offspring
		else:
			self.age = 1
			return 0


population = [Rabbit()]
month = 1		 
while month < n:
	offspring = [i.reproduce() for i in population]
	for i in range(sum(offspring )):
		population.append(Rabbit())
	print(len(population))
	month += 1

print("The population after " + str(n) + " months and " + str(k) + " Offsprings later is " + str(len(population)))
"""
# using procedural programming
def f_n(k, fn1, fn2):
	return fn1 + k*fn2

month = 3
fn1 = 1
fn2 = 1
while month <= n :
	fn = f_n(k, fn1, fn2)
	fn2 = fn1
	fn1 = fn
	print(month, fn)
	month += 1
print("The population after " + str(n) + " months and " + str(k) + " Offsprings later is " + str(fn))