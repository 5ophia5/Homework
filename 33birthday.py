#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

n = 25 #number of people
trials = 100
count = 0

for i in range(trials):
	calendar = [] #blank calendar
	for i in range(n): #random assignment of birthdays to each person
		birthday = (random.randint(1, 365))
		calendar.append(birthday)

	#are there shared birthdays?
	calendar.sort()
	j = 0
	while(j < n - 1):
		if calendar[j] == calendar[j + 1]:
			count += 1
			break
		j += 1
print(count / trials)

"""
python3 33birthday.py
0.571
"""

