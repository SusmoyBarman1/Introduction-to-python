# working with key-value pair

student = {"Name":"Susmoy Barman","Age":23,"Dept.:":"CSE","Courses:":["DSP","Database","Compiler "
                                                                                       "Design"]}

print(student)
print(student["Name"])
print(student.get("Name")) # We should use get() method instead of index

#student["Phone"] = 555-55555
student.update({'phone':555-55555})
print(student)

# Deleting value
del student['Age']
print(student)

print(student.values())
print(student.items())
print(student.keys())