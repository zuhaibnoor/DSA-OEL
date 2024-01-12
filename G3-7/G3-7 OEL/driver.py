from LRUcache import *

# #GLOBAL VARIABLE
# NO_OF_REFERENCE = 50 # Because a/c to constraint the maximum length of LRU cache must be 50
# NUMBER_OF_ODD_NUMBER = 50 # Total odd numbers beteween 1 to 100
# NUMBER_OF_PRIME_NUMBER = 25 # Total prime numbers beteween 1 to 100
# TOTAL = 125

# def ListOfKeys():
#     return [i for i in range(1,51)]

# def PrimeNumber():
#      return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# #COMPULSORY MISS
# def Compulsory_Miss(length):
#     MISS = length
#     rate = (MISS/NO_OF_REFERENCE)*100
#     return rate


# #ODD NUMBER MISS
# def Odd_Number_Miss(lru, noOdd):
#      dic = lru.dic
#      count = 0
#      for key, values in dic.items():
#           #lru.get(key)
#           if key % 2 != 0:
#                count += 1
#      MISS = noOdd - count
#      return (MISS/noOdd)*100

# # def Odd_Number_Miss(lru, noOdd):
# #      count = 0
# #      for key in range(1, 51):



# #PRIME NUMBER MISS
# def Prime_Number_Miss(lru):
#      dic = lru.dic
#      primes_List = PrimeNumber()
#      Already_Used = []
#      for key, values in dic.items():
          
#           if key in primes_List:
#                #lru.get(key)
#                Already_Used.append(key)
#      Not_Used = list(set(primes_List) - set(Already_Used))
#      Not_Used.reverse()
#      MISS = len(Not_Used)
#      for k in Not_Used:
#           lru.put(k, k)
#      return (MISS/25)*100

# def Miss_Rate(miss):
#      return round(miss/3,2)




# length = 50
# lru = LRU(length)
# for j in ListOfKeys():
#         lru.put(j, j)



# m1 = Compulsory_Miss(length)
# m2 = Odd_Number_Miss(lru, NUMBER_OF_ODD_NUMBER)
# m3 = Prime_Number_Miss(lru)

# print(Miss_Rate(m1+m2+m3))




lru = LRU(50)

PRIME_LIST = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

ACCESS = 0
TOTAL_MISS = 0

ODD_COUNT = 0
PRIME_COUNT = 0

for i in range(1, 51):
        TOTAL_MISS += 1
        ACCESS += 1
        lru.put(i, i)

for i in range(1, 101, 2):
        i = lru.get(i)
        ACCESS += 1
        if i == -1:
            TOTAL_MISS += 1

for i in range(0, len(PRIME_LIST)-1):

        ACCESS += 1
        val = lru.get(PRIME_LIST[i])

        if val == -1:
            lru.put(PRIME_LIST[i], PRIME_LIST[i])
            TOTAL_MISS += 1

lru.tra()

print(f"Miss Rate : {round(TOTAL_MISS/ACCESS, 2)*100}")