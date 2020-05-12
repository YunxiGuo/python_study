print('give me two numbers,and i`ll divide them.')
print('enter "q" to quit.')
while True:
    first = input('\n first number: ')
    if first == 'q':
        break
    second = input(' second number: ')
    try:
        result = int(first) / int(second)
    except ZeroDivisionError:
        print('division can not been zero')
    else:
        print(result)
