"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    
    contract_pay = 0
    total_pay = 0

    #sal_con = False

    
    commission = False
    fstring = ''
    
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        #pass
        
        if self == billie:
            set_salary_con(4000)
            fstring = f'{self.name} works on a monthly salary of {contract_pay}. '
        elif self == charlie:
            set_hourly_con(25, 100)
            fstring = f'{self.name} works on a contract of 100 hours at 25/hour. '
        elif self == renee:
            set_salary_con(3000)
            set_con_comm(4, 200)
            fstring = f'{self.name} works on a monthly salary of {contract_pay} and receives a commission for 4 contracts at 200/contract. '
        elif self == jan:
            set_hourly_con(25, 150)
            set_con_comm(3, 220)
            fstring = f'{self.name} works on a contract of 150 hours at 25/hour and receives a commission for 3 contracts at 220/contract. '
        elif self == robbie:
            set_salary_con(2000)
            set_bonus_comm(1500)
            fstring = f'{self.name} works on a monthly salary of {contract_pay} and receives a bonus commission of 1500. '
        elif self == ariel:
            set_hourly_con(30, 120)
            set_bonus_comm(600)
            fstring = f'{self.name} works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. '

        total_pay = get_total_pay()

        return total_pay

    def __str__(self):
        final string = fstring + 'Their total pay is ' + get_total_pay()
        #return self.name
        #if self.name = 'Billie' or 'Renee' or 'Robbie':
            #fstring = f'{self.name} works on a {} of {get_contract()}. Their total pay is {get_total_pay}.'
        #else:
            #string = f'{self.name} works on a {} of {get_contract()}. '
        
        #final_string = contract_pay_string + comm_pay_string
        #return final_string


    #def contract_pay_string():
    #    if sal_con == True:
    #        con_string = 'monthly salary'
    #    else:
    #        con_string = 'contract of {} hours at {}/hour'
    #    fstring = f'{self.name} works on a {con_string}'

    #def total_pay_substring():
    #    final_string = 



    
    
    def get_contract():
        return contract_pay

    def set_salary_con(amount):
        contract_pay = amount
        
    def set_hourly_con(int wage, int hours):
        contract_pay = wage * hours

    def set_bonus_comm(amount):
        comm_pay = amount
        commission = True

    def set_con_comm(int contracts, int commission):
        comm_pay = contracts * commission
        commission = True
        
    def get_comm():
        return comm_pay
        

    def get_total_pay():
        if commission == True:
            total_pay = get_contract() + get_comm()
        else:
            total_pay = get_contract()
        return total_pay

    #def add_to_string(phrase):
        #fstring = f'{self.name} works on a {phrase}'
    


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
