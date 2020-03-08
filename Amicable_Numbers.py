def Searching (Number) :
    Sum = 0
    Numbers = []
    for index in range (1 , Number) :
        if  (Number % index) == 0 :
            Numbers.append (index)
    for index in Numbers :
        Sum = Sum + index
    return Sum


print ('Hello, this is an application which is searching for Amicable numbers,')
Answer = input ('type "info" if you want information about Amicable numbers or "start" to run the application!\n>>> ')
if Answer == 'info' : print ('Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number.')
while Answer != 'start' :
    Answer = input('If you want to start type "start" else type "close" to close the application\n>>> ')


if Answer == 'start' :
    ignore_list = []
    destination = int(input ('Until Which number should I search for Amicable numbers?\n>>> '))

    for first_number in range (1 , destination + 1) :
        second_number = Searching (first_number)
        potantial_first_number = Searching (second_number)

        if potantial_first_number == first_number :
            if potantial_first_number != second_number :
                ignore_list.append (first_number)
                if (not(first_number in ignore_list)) or (not(second_number in ignore_list)) :
                    print (first_number , second_number)
    Answer2 = input("Type 'check' if you want to see the sum of a number's proper divisors or 'finish' to close the application\n>>> ")
    while Answer2 == 'check' or Answer2 == 'again' :
        Number = int(input ('Number: '))
        print (Searching (Number))
        Answer2 = input ('Type "again" if you want to check another number or "finish" to close the application!\n>>> ')
