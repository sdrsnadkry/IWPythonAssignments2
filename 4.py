def appends(insert):
    names = ['John', 'Shyam']
    id_1 = id(names)

    words = insert.split(" ")
    for n in words:
        names.append(n)
    id_2 = id(names)

    sortedNames = sorted(names)

    if id_1 == id_2:
        print('Id are same')
    else:
        print('Id are different')

    print("First Item:", sortedNames[0], " Second Item:", sortedNames[1])


insert = input("Enter names to be appended: ")
appends(insert)
