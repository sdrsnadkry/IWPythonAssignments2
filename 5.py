def sort_people(people):
    sudarshan = ('Sudarshan', 'Adhikari', 24)
    john = ('John', 'Doe', 35)
    ram = ('Ram', 'Prasad', 26)

    people.extend((sudarshan, john, ram))

    people.sort(key=lambda x: x[1])
    return people


people = []
print("Sorted according to Last Name : \n ", sort_people(people))
