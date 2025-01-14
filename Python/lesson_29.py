# fruits =['apple,"orange","banana"]
#
#   print(fruits)
#
# fruits = ["apple", "banana", "cherry"]
# print(fruits[1])
# print(fruits)


# fruits[1] = "blueberry"
# fruits.append('date')
# fruits.remove('blueberry')
# print(fruits)
# print(len(fruits[0]))
# print(len(fruits))
# if len(fruits) == 3:
#     print('Все фрукты на месте')

# last_fruit = fruits.pop()
# print(last_fruit)
# fruits.sort()
# fruits.reverse()
# print(fruits)
# index = fruits.index("banana")
# print(index)

fruits = ["cherry", "apple", "banana", "cherry", "cherry", "cherry"]
# new_list = ["fig", "grape"]
print(fruits)

fruits.extend(["fig", "grape"])
# fruits.extend([new_list])
print(fruits)

# count = fruits.count("cherry")
# print(count)

# last_fruit = fruits.pop()
# print(last_fruit)
# fruits.sort()
# fruits.reverse()
# print(fruits)
# index = fruits.index("banana")
# print(index)

fruits = ["apple", "banana", "cherry", "banana"]
count = 0

for fruit in fruits:
    if fruit != "banana":
        count = count + 1
        print(fruit)

# print(count)
# for элемент in последовательность:
#     блок_кода

fruits = ["apple", "banana", "cherry", "banana", "potato"]
count = 0
potato = 'potato'

for fruit in fruits:
    if fruit == potato:
        count = count + 1
        print(fruit)

if count == 0:
    print('Иди в кауфланд')
else:
    print('Жарим картошку')

if билеты == купим:
 идем в кино
elif хорошая == погода:
    идем в парк

if билеты == купим:
 идем в кино

if билеты == купим and хорошая == погода:
 идем на концерт
elif хорошая == погода:
    идем в парк



# for i in range(5):
#     print(i)

fruits = ["apple","banana","cherry" ]

count = 0

for x in fruits:
    count = count + 1
   # print (f'
# while условие:
#     блок_кода

count = 0

while count < 5:
    print(count)

    if count == 0:
        count += 1
    else:
        count += 3

