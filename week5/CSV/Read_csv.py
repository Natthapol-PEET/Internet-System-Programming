import csv

f = open('username-or-email.csv')

word = input('Plases enter your Username: ')

for row in csv.reader(f, delimiter=';'):
    if word == row[0]:
        print(row)
        print('Username: ', row[0])
        print('Email: ', row[1])
        print('Identifier: ', row[2])
        print('First name: ', row[3])
        print('Last name: ', row[4])
