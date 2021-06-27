from customer import Customer

def check_user_present(name):
    return Customer.user_presence(name)


def withdraw_money(user, currency, amount):
    return Customer.withdraw(user, currency, amount)

def main():
    print('Welcome customer')
    name = input("Enter your name: ")
    user = check_user_present(name)
    times = 0
    actions = {}
    if user != None:
        while times < 3: #BUG loop 3 times
            pin = int(input('Enter your pin:- '))
            if pin == user['pin']:
                print('Logged in')
                print('\n')
                while True:
                    print('If you want to check balance, Type:- bal \nIf you want to withdraw, Type:- withdraw \nIf you want to exit, Type:- exit')
                    print('\n')
                    code_word = input('Enter code word: ').lower()
                    
                    if code_word == 'bal':
                        print(user['balance']) 
                        actions['checked balance'] = user['balance']
                    elif code_word == 'withdraw':
                        currency = input('Withdraw in KES or USD?; Type USD or KES:- ').upper()
                        amount = int(input('Enter amount:- ')) 
                        if currency == 'USD':
                            if amount > user['balance']['USD']:
                                print('Cannot withdraw more than your balance')
                            else:
                                print(withdraw_money(user, currency, amount))
                                actions['Withdraw'] = f'{currency}, {amount}'
                        if currency == 'KES':
                            if amount > user['balance']['KES']:
                                print('Cannot withdraw more than your balance')
                            else:
                                print(withdraw_money(user, currency, amount))
                                actions['Withdraw'] = f'{currency}, {amount}'

                    elif code_word == 'exit':
                        confirm = input('Do you want a receipt: Y/N:- ').lower()
                        if confirm == 'y':
                            print(f'You have performed the following actions:-\n {actions}')
                            break
                        print('Exiting...')
                        break
                    else:
                        print('Exiting..')
                        break

            else:
                print('Wrong pin')
                times += 1
            break

if __name__ == '__main__':
    main()