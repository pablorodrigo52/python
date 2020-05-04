import math
import statistics

numbers = [54.54, 54.545, 354, 332, 784, 154, 4.87, 0.45, -457]
average = 142.38
summation = 0

for i in numbers:
    summation = summation + i
average = summation / len(numbers)
summation = 0
for i in numbers:
    summation = summation + ((i - average)**2)
summation = summation / (len(numbers) - 1)

print('Média: ', average)
print('Desvio padrão calculado: ', math.sqrt(summation))
print('Desvio padrão da lib statistics: ',statistics.stdev(numbers))