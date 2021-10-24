#### Prime Finding
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


#coderun1 = timeit.timeit(stmt=code1, number=10)
#print(coderun1)


#coderun2 = timeit.timeit(stmt=code2, number=10)
#print(coderun2)


# list_21000 = sum(list(map(int, str(2 ** 1000))))
# print(list_21000)


########  CompleTimexity:

## Considering the worst case scenario of an algorithm


########### Brute Force Solution
# O(n ** 2)


def twoSum(nums, k):
  d = {} # To Store values/indices

  for idx, elem in enumerate(nums):

    # Check  k - current number is in d
    if k - elem in d:
      # If it is, then return and stop!
      return [idx,  d[k - elem]]
    else:
      # Or we add the current element and its index
      d[elem] = idx


nums = [2,5,1,8,10]
k = 13

#print(twoSum(nums, k))


#################################

### Frequency table

## {'a' : 3, 'e' : 2, 'i' : 2}
vowels = 'aaeeiiuoua'

freq = {}


for i in vowels:
  if i not in freq:
    freq[i] = 1
  else:
    freq[i] += 1


#print(freq)

#######

# .get()
# .setdefault()


places = {'London': 1, 'Manchester': 2, 'Liverpool' : 3}
keys = list(places.keys())[0]



#print(places.get('Manchestr', 'Key not present'))
#print(places.get('Manchestr', places[keys]))

print(places)

places.setdefault('Leeds', 20)

print(places)


#########
# https://leetcode.com/problems/jewels-and-stones/
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
