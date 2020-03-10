def searching (number) :
    sum = 0
    numbers = []
    for index in range (1 , number) :
        if  (number % index) == 0 :
            numbers.append (index)
    for index in numbers :
        sum = sum + index
    return sum


print ('Hello, this is an application which is searching for Amicable numbers,')
answer = input ('type "info" if you want information about Amicable numbers or "start" to run the application!\n>>> ')
if answer == 'info' : print ('Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number.')
while answer != 'start' :
    answer = input('If you want to start type "start" else type "close" to close the application\n>>> ')


if answer == 'start' :
    
    ignore_list = []
    destination = int(input ('Until Which number should I search for Amicable numbers?\n>>> '))
    for first_number in range (1 , destination + 1) :
        second_number = searching (first_number)
        potantial_first_number = searching (second_number)

        if potantial_first_number == first_number :
            if potantial_first_number != second_number :
                ignore_list.append (first_number)
                if (first_number not in ignore_list) or (second_number not in ignore_list) :
                    print ('The numbers', first_number ,'and', second_number ,'are amicable!')

    answer2 = input("Type 'check' if you want to see the sum of a number's proper divisors or 'finish' to close the application\n>>> ")
    while answer2 == 'check' or answer2 == 'again' :
        number = int(input ('Number: '))
        print (searching (number))
        answer2 = input ('Type "again" if you want to check another number or "finish" to close the application!\n>>> ')
