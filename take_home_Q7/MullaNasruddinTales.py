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
                    number_string = line[0 : index]

                    if number_string.isdigit():
                        if single_tale != '':
                            tales_list.append(single_tale)
                        single_tale = line
                    else :
                        single_tale += line
            
            if single_tale != '' and '\n':
                tales_list.append(single_tale)
    return tales_list


def main():
    tales_list = read_file_and_devide_tales()
    
    total_number_of_tales = len(tales_list)

    print(f"Total tales we have {total_number_of_tales}")

    number = input('Enter the number of tales to retrieve (1-{total_number_of_tales}): ')

    while (not number == '') and not (number.isdigit() == True and 1 <= int(number) <= total_number_of_tales):
        number = input(f'Please enter a valid number between 1 and {total_number_of_tales}: ')    

    if number == '':
        number = DEFAULT_NUMBER_OF_TALES
    number = int(number)  
    random.shuffle(tales_list)

    for index in range(number):
        print(tales_list[index], end='')

main()
