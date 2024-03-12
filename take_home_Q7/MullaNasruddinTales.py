import random

DEFAULT_NUMBER_OF_TALES = '1'
ENCODING = 'utf-8'
FILE_NAME = 'The_Tales_of_Mulla_Nasruddin.txt'


def read_file_and_devide_tales():
    tales_list = []
    with open(FILE_NAME, encoding=ENCODING) as file:
            single_tale = ''
            for line in file.readlines():
                index = line.find('.')
                if line == '\n':
                    single_tale += line
                if index > 0:
                    # print(f'index of . is {index}')
                    # print(line[0 : index])
                    # print(line, end='')
                    number_string = line[0 : index]

                    if number_string.isdigit():
                        # print(f"It's a number {number_string}")
                        if single_tale != '':
                            tales_list.append(single_tale)
                        single_tale = line
                    else :
                        single_tale += line
                        # print(f"It's not a number {number_string}")
            
            if single_tale != '' and '\n':
                tales_list.append(single_tale)
    return tales_list


def main():
    tales_list = read_file_and_devide_tales()
    
    total_number_of_tales = len(tales_list)

    print(f"length of list {total_number_of_tales}")

    number = input('Enter number of Tales to retrive ')

    # while number.isdigit() == False or not number == '' :
    #     number = input(f'Please enter the valid number an integer between (1 & {total_number_of_tales}) ')    
    #     if number.isdigit() == True:
    #         number = int(number)
    #         while number > total_number_of_tales or number == '':
    #             number = input(f'Please a number less than the total available tales {total_number_of_tales} ') 

    while (not number == '') and not (number.isdigit() == True and 1 <= int(number) < total_number_of_tales):
        number = input(f'Please enter the valid number an integer between (1 & {total_number_of_tales}) ')    
        # if number.isdigit() == True:
        #     number = int(number)
        #     while number > total_number_of_tales or number == '':
        #         number = input(f'Please a number less than the total available tales {total_number_of_tales} ') 

  

    if number == '':
        number = DEFAULT_NUMBER_OF_TALES
    number = int(number)  
    random.shuffle(tales_list)

    for index in range(number):
        print(tales_list[index], end='')

main()
