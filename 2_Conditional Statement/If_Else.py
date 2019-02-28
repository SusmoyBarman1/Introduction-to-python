
if True:
    print("Condition is true")

language = 'Python'
if language == 'Java':
    print('Language is Python')
elif language == 'C':
    print('Language is C')
else:
    print('Defult is python')

name = 'Susu'
logged_in = True

if name=='Susu' and logged_in:
    print('Welcome to the browser')

if not logged_in:
    print('Please log in')

a = [1,2,3]
b = [1,3,3]
print(id(a))
print(id(b))

print(a is b)

b = a
print(id(a))
print(id(b))

print(a is b)