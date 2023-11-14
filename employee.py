"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    def __init__(self, name):
        self.name = name
        self.contract_type = "salary"
        self.salary = 0
        self.hourly_wage = 0
        self.hours_worked = 0
        self.bonus = 0
        self.commission_rate = 0
        self.contracts_landed = 0
        self.total_pay = 0

    def get_pay(self):
        contract_pay = 0

        if self.contract_type == "salary":
            contract_pay = self.salary
        elif self.contract_type == "hourly":
            contract_pay = self.hourly_wage * self.hours_worked

        commission = self.calculate_commission()
        self.total_pay = contract_pay + commission  # Store total pay in the instance variable
        return self.total_pay

    def calculate_commission(self):
        if self.bonus > 0:
            return self.bonus
        elif self.commission_rate > 0:
            return self.commission_rate * self.contracts_landed
        else:
            return 0

    def __str__(self):
        fstring = ''
        return fstring

# Subclass for employees on a fixed salary contract without commission
class FixedContract(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.contract_type = "salary"
        self.salary = salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.total_pay}."

# Subclass for employees on an hourly contract without commission
class HourlyContract(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name)
        self.contract_type = "hourly"
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hourly_wage} hours at {self.hours_worked}/hour. Their total pay is {self.total_pay}."

# Subclass for employees on a fixed salary contract with a bonus commission
class FixedContractWithBonus(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.contract_type = "salary"
        self.salary = salary
        self.bonus = bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.total_pay}."

# Subclass for employees on an hourly contract with a bonus commission
class HourlyContractWithBonus(Employee):
    def __init__(self, name, hourly_wage, hours_worked, bonus):
        super().__init__(name)
        self.contract_type = "hourly"
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus = bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hourly_wage} hours at {self.hours_worked}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.total_pay}."

# Subclass for employees on a fixed salary contract with a contract commission
class FixedContractWithCommission(Employee):
    def __init__(self, name, salary, commission_rate, contracts_landed):
        super().__init__(name)
        self.contract_type = "salary"
        self.salary = salary
        self.commission_rate = commission_rate
        self.contracts_landed = contracts_landed

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts_landed} contract(s) at {self.contracts_landed}/contract. Their total pay is {self.total_pay}."

# Subclass for employees on an hourly contract with a contract commission
class HourlyContractWithCommission(Employee):
    def __init__(self, name, hourly_wage, hours_worked, commission_rate, contracts_landed):
        super().__init__(name)
        self.contract_type = "hourly"
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.commission_rate = commission_rate
        self.contracts_landed = contracts_landed

    def __str__(self):
        return f"{self.name} works on a contract of {self.hourly_wage} hours at {self.hours_worked}/hour and receives a commission for {self.contracts_landed} contract(s) at {self.contracts_landed}/contract. Their total pay is {self.total_pay}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = FixedContract('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyContract('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = FixedContractWithCommission('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContractWithCommission('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = FixedContractWithBonus('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyContractWithBonus('Ariel', 30, 120, 600)
