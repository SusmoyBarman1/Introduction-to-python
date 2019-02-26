
# List uses []

courses = ["ICE","Compiler","Database","DSP"]
print(courses)
print(type(courses))

# length of a list
print(len(courses))
print(courses[0])
print(courses[1])
print(courses[len(courses) - 1])
print("\n")

# Reverse indexing
print(courses[-1])
print(courses[-2])
print(courses[-3])
print(courses[-4])
print("\n")

print(courses[0:2])
print(courses[1:])
print(courses[:2])

# Append Function
courses.append(200)
print(courses)
print(type(courses[len(courses) - 1]))

# Insert Function
courses.insert(2,3.14)
print(courses)

# Add one list to another using extend method
courses_2 = [1,2,3,4,5]
courses.extend(courses_2)
print(courses)

# append function
courses_3 = ["Votka","Maruf"]
courses.append(courses_3)
print(courses)

# pop function
courses.pop()
num = courses.pop()
print(courses)
print(num)

# sort function
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)

# sorted function, it does not sort the list, it returns the sorted version of the list
list_1 = sorted(courses)
print(list_1)
print(courses)

# min, max function
value_1 = min(courses)
value_2 = max(courses)
print("Max value:",value_2,"Min Value:",value_1)

# finding value in list
print("bangladesh" in courses)

# Character seperated values using string and join() function, if the list contains only
# strings.
list_2 = ["susmoy","barman","tiash","golam","maula","maruf"]
str = ' , '.join(list_2)
print(str)

# str to list
new_list = str.split(' , ')
print(new_list)


