import timeit



code1 = '''
def is_prime(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

q = [is_prime(i) for i in range(5000)]
'''


code2 = '''
def is_prime_fast(x):
  for i in range(2, int(x**0.5)+1):
    if x % i == 0:
      return False
  return True

p = [is_prime_fast(i) for i in range(5000)]
'''


print(timeit.timeit(code1))