from numpy import binary_repr
import re


def fantz(binary_number, number):

    list_of_powers = ['1']
    count = 0

    for i in range(len(binary_number)):
        if len(list_of_powers[i]) >= len(binary_number):
            break
        list_of_powers.append(binary_repr(number**(i+1)))
    list_of_powers.reverse()

    for power in list_of_powers:
        result_number, replace_count = re.subn(power, '', binary_number)
        binary_number = result_number
        count += replace_count
    if len(binary_number) != 0:
        return -1
    return count


if __name__ == '__main__':
    print(fantz('101101101', 5))
