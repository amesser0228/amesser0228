#Get the prefix of a number

number = int(input('enter a dashless 10-digit phone number: '))
print('Please select which option you want to use for provided phone number')
prefix_code = int(input('  Enter 1 to retrieve prefix: ' '\n  Enter 2 to retrieve office code:\n  '))


if prefix_code == 1:
    number_prefix = number % 1000
    print('The prefix to number ', number , 'is ', number_prefix)

else:
    office_code = number // 10000
    office_code %= 1000
    print('The central office code is: ', office_code)
