import timeit




code1 = '''
print('Hello World')
'''


code2 = '''
import math as ma
x = [ma.factorial(i) for i in range(100,200)]
'''

# run1 = timeit.timeit(stmt=code1, number=1000)
# print(run1)


run2 = timeit.timeit(stmt=code2, number=1000)
print(run2)