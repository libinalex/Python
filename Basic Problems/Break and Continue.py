while True:
    print('Who are you?')
    name = input()
    if name != 'Libin':
        continue
    print('Hello, Libin! What is the password? (It is Football)')
    password = input()
    if password == 'Basketball':
        break
print('Access granted.')