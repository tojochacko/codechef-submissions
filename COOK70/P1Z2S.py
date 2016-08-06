import sys

1 - 1
2 - 1
3 - 2
4 - 2
5 - 3
6 - 3
7 - 4
8 - 4


# no of test cases
no_of_chefs = int(input())

if no_of_chefs > 10**5 or no_of_chefs < 1:
    sys.exit()

possible_visits = no_of_chefs * 2 #based on each gets a single ticket
total_visits = 0
no_of_times = input()
no_of_timesList = no_of_times.split(' ')

for times in no_of_timesList:
    total_visits += int(times)

diff = total_visits - possible_visits

if diff == 0:
    print(no_of_chefs)
elif diff > 0:
    print(no_of_chefs + ??? )
