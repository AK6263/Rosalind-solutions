# number of total pairs of rabbits 
n = 6
# life  span of a rabbit pair
m = 3

# using procedural programming
# The list will store the population
population = []

def f_n(k, fn1, fn2,fnk):
    return fn1 + fn2 - fnk 

month = 3
fn1 = 1
fn2 = 1
population.append(fn1)
population.append(fn2)
print(population)
while month <= n:
    #print(population)
    if month <= m:
        fn = fn1 + fn2
    else:
        fn = f_n(month, population[-1], population[-2],population[month-m+1])
        print(population[-m])
    fn1 = fn2
    fn2 = fn
    population.append(fn)
    print(month, fn)
    month += 1

print("The population after " + str(n) + " months and " + str(m) + " Offsprings later is " + str(population[-1]))
print(population)