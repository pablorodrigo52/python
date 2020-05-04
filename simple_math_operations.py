import math
import statistics
numbers = [54.54, 54.545, 354, 332, 784, 154, 4.87, 0.45, -457]
average = 142.38

sum = 0

print(numbers)
for i in numbers:
    sum = sum + ((i - average)**2)
sum = sum / (len(numbers) - 1)

print('Desvio padrão calculado: ', math.sqrt(sum))
print('Desvio padrão da lib statistics: ',statistics.stdev(numbers))