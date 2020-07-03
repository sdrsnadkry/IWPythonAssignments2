def search(names):
    for name in names:
        if name == "John":
            return name + ' found'
        else:
            return name + ' not found'


names = ['John', 'Ram', 'Shyam', 'Raju']
print(search(names))
