import random
list_of_number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number1 = random.choice(list_of_number) #число в первом поле

print('число:', number1)

n = number1
comb1 = list(range(1, n))
comb2 = list(range(1, n))
result = ''

for i in comb1:
    for j in comb2:
        n1 = i
        n2 = j
        if n1 >= n2:
            continue
        else:
            b = n % (n1 + n2)
            if b == 0:
                result = result + str(n1) + str(n2)
print('подбор пароля:', result)