def find_average(lists):

    length = len(lists)
    sum = 0

    for tuples in lists:
        if tuples[2] == None:
            pass
        else:
            sum = sum + tuples[2]

    avg = sum/length
    print("Average age is: ", avg)

    for tuples in lists:
        age_check = ''
        if tuples[2] == None:
            print(tuples[0], "Age Undefined")
        else:
            if tuples[2] > avg:
                age_check = 'Old'
            else:
                age_check = 'Young'
            print(tuples[0], age_check)


lists = [('sudarshan', 'adhikari', 11), ('mukesh', 'khadka', 25),
         ('sanjog', 'piya', 30), ('ronish', 'gopaju', 34), ('sanish', 'manandhar', None)]
find_average(lists)
