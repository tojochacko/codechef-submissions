#this won't work for cases where input is less than 97
#we need to write a if case for input less than 97
import sys


def sum_of_digits(number):
    calculated_sum = 0
    while number:
        digit = number % 10

        calculated_sum += digit

        # remove last digit from number (as integer)
        number //= 10

    return calculated_sum


def main(chkval):
    ans = 0
    for number in range(chkval-97, chkval+1):
        temp1 = sum_of_digits(number)
        temp2 = sum_of_digits(temp1)

        if (number + temp1 + temp2) == chkval:
            ans += 1

    return ans

N = int(sys.stdin.readline())
print(main(N))
