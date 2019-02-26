courses = ["ICE", "DSP", "Compiler Design", "Database", "Software Engi."]

for item in courses:
    print(item)

# Printing items with
for index, item in enumerate(courses):
    print(index, item)

for index, item in enumerate(courses,start=1):
    print(index, item)
