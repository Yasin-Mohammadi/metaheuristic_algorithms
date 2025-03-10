a = 7

if a > 10:
    print('a is greater than 10')
elif a >= 8 and a <= 10 :
    print ('a is between 8 and 10')

else:
    print('a smaller than 8')
    

a = 'python'

print(a.ljust(10, '*'))
print(a.rjust(10, '*'))

inp = '1111Maryam1111'
print(inp.strip('1'))

print('--' * 40)

name = "Ahamd"
family = "Moradi"
age = 25

print("the user is {1} {0} and {2} years old".format(name, family, age))


dict1 = {'st1': "ali", 'st2':"Maryam"}

for k, v in dict1.items():
    print(k, v)

for i in dict1.keys():
    print(i, dict1[i])
    

students = [
    {'name': 'ali', 'age': 12, 'scores' : [12, 23, 12, 17]},
    {'name': 'maryam', 'age': 43, 'scores' : [121, 23, 12, 17]},
    {'name': 'reza', 'age': 53, 'scores' : [12, 203, 12, 17]},
]

print('--' * 40)
print(students[0])