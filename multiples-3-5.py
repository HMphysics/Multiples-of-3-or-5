def solution(number):
    # First we will check if number is below 0 or not.

    # If number is above 0 or is 0, these sentences were applied.
    if number >= 0:

        # We will generate a list with every number below our number except that unique number.
        # The list has been created using a loop with each number we are interested in.
        lista = [i for i in range(number)]

        # We will create two more lists to keep every number multiple of 3 or 5.
        mult3 = list()
        mult5 = list()

        # We will use a loop through the list where our numbers are.
        # Later we will evaluate the numbers and we will keep them in each list of multiples.
        for i in lista:
            if i % 3 == 0:
                mult3.append(i)
            elif i % 5 == 0:
                mult5.append(i)

        # Finally we will sum each number on the lists and sum two lists.
        sum3 = sum(mult3)
        sum5 = sum(mult5)

        return sum3+sum5

    # If number is below 0, these sentences were applied.
    elif number < 0:
        return 0
