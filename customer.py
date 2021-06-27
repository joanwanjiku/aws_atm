

class Customer:
    users = [
        {'username':'trial', 'pin':0000, 'balance':{'KES':140, 'USD':0}},
        {'username':'melvin', 'pin':1234, 'balance':{'KES':350, 'USD':20}},
        {'username':'joan', 'pin':5678, 'balance':{'KES':400, 'USD':40}}
    ]

    @classmethod
    def user_presence(cls, name):
        for user in cls.users:
            if user['username'] == name:
                return user


    @classmethod
    def withdraw(cls, user, currency, amount):
        curr_user = cls.user_presence(user['username'])
        curr_user['balance'][currency] -= amount
        return curr_user['balance'] 
