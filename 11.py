def filename(name):
    extension = name[-3:]
    filename = name[:-3]

    print(filename, extension, sep=" is filename and extension is ")


name = input("Enter a  filename with extension: ")
filename(name)
