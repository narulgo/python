i = input('Give a letter of your choice: ')

if i in ('a','e','i','o','u') or i in ('A','E','I','O','U'):

    print(i, 'is a vowel')

elif i =='y' or i=='Y':

    print('%s is either a vowel or consonant' %i)

else:

    print('{} is a consonant'.format(i))