
class Bank(object):
    
    accountList=[]
    def display(self): #for printing purposes only, not for user
        for account in Bank.accountList:
            print ("*********************")
            for k,v in account.options.items():
                print ('{}: {}'.format(k,v))
            print ("*********************")

    def login_validity(self, u, p): #checks for the correct login 
        for account in Bank.accountList:
            if u == account['username'] and p == account['pin']:
                return True
        return False

    def load_account(self,u, p): #loads current account
        for account in Bank.accountList:
            if u == account['username'] and p == account['pin']:
                return account #account object
        return None #no object found
    
    

class Account(object):
    default_options = {'accountno':None,'acctype': None, \
               'balance': 0, 'fname': None, 'lname': None, 'line1':None, \
                       'line2': None, 'username': None, 'pin': None}
    def __init__(self, **kwargs):
        #current object is self.options
        self.options = Account.default_options.copy() 
        # updates options with new values from kwargs
        self.options.update(kwargs)
        # adds the new account to the account list
        Bank.accountList.append(self)

    def __getitem__(self, key): #get an item by key
        return self.options[key]
    
    def __setitem__(self, key, new_value): #set an item by key
        self.options[key] = new_value
        
    def getBalance(self, accno):
        if accno == self['accountno'] : #how to access an attribute self[key]
                return self['balance']
 
    def deposit(self, amount_to_deposit, accno):
        # checks if account number is correct to perform successful deposit
        if accno == self['accountno']:
            # sets the balance to the previous balance plus the deposit amount
            self['balance'] = self['balance'] + float(amount_to_deposit)
        #please see getBalance on how to access an attribute
        #deposits amount_to_deposit to current user

    def summary(self, accno):
        # checks if account number is correct to perform successful summary
        if accno == self['accountno']:
            # creates full name
            name = self.__getitem__('fname')+' '+self.__getitem__('lname')
            # creates full address
            address = self.__getitem__('line1')+' '+self.__getitem__('line2')
            # retrieves the account type
            acc_type = self.__getitem__('acctype')
            # retrieves the balance
            balance = self.__getitem__('balance')
            return name, address, acc_type, balance
        #return full name, address, account type and current balance


      
class Saving(Account):
    withdraw_charge = 2.53 #flat rate to subtract from saving account
    def withdraw(self, amount_to_withdraw, accno):
        # checks if account number is correct to perform successful withdrawal
        if accno == self['accountno']:
            # subtracts the withdraw amount and withdraw charge
            # from the current balance 
            new_bal = self['balance'] - float(amount_to_withdraw) -\
                      Saving.withdraw_charge
            # sets the new balance
            self['balance'] = new_bal

class Checking(Account):
    withdraw_charge = 1.00 #flat rate to subtract from checking account
    def withdraw(self, amount_to_withdraw, accno):
        # checks if account number is correct to perform successful withdrawal
        if accno == self['accountno']:
            # subtracts the withdraw amount and withdraw charge
            # from the current balance
            self['balance'] = self['balance'] - float(amount_to_withdraw) - \
                              Checking.withdraw_charge

