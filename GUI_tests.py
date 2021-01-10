# -------------------------------------------------------------------------------
# Final Project: Banking Application
# Name: Nathan Manzo
# Python Version:  3.7.2
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Comments to grader: 
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------



from tkinter import *
from Nathan_Manzo_CLASS import Account, Bank, Saving, Checking
from Nathan_Manzo_UTILITY import createAccountNo

class MyFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.bank = Bank()
        self.welcome()
 
    def clear_frame(self): #clears the previous frame
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        root.destroy()

    def logout(self):
        del self.account
        self.welcome()
        
    def welcome(self): #welcome screen
        self.clear_frame()
        
        welcome_label = Label(self, text = 'Welcome to 209 Banking!')
        self.b1  = Button(self, text = "Existing User", \
                     command=self.existing_account_widget)
        self.b2  = Button(self, text = "New User", \
                     command=self.new_account_widget)
        self.b3  = Button(self, text = "Exit Application", \
                     command=self.exit_application)

        #layout  manager for label, b1, b2 and b3
        welcome_label.pack()
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        
        
        
    def new_account_widget(self):
        
        self.clear_frame() #clears the previous frame
        # ********************* create widgets *********************
        # first name
        label_fname = Label(self, text = "First name: ")
        self.entry_fname = Entry(self, width=15)
        # last name
        label_lname = Label(self, text = "Last name: ")
        self.entry_lname = Entry(self, width=15)
         # creates address line 1, address line 2, account type, username
        # and pin widgets
        # creates address line 1 label and entry
        label_address1 = Label(self, text = 'Address line 1')
        self.entry_address1 = Entry(self, width=15)
        
        # creates address line 2 label and entry
        label_address2 = Label(self, text = 'Address line 2')
        self.entry_address2 = Entry(self, width=15)
        
        # creates account type label and entry
        label_account = Label(self, text = 'Account Type')
        self.entry_account = Entry(self, width=15)
        
        # creates username label and entry
        label_user = Label(self, text = 'Username')
        self.entry_user = Entry(self, width=15)
        
        # creates pin label and entry
        label_pin = Label(self, text = 'Pin')
        self.entry_pin = Entry(self, width=15)

        # makes the Create Account and Main Menu Buttons
        self.button_create = Button(self, text = 'Create Account', command = \
                                    self.create_account_button_click)
        self.button_menu = Button(self, text = 'Main Menu', command = \
                                  self.welcome)

        # ********************* Layout Widgets *********************
        # first name
        label_fname.grid(row=0, column = 0)
        self.entry_fname.grid(row=0, column = 1)
        # last name
        label_lname.grid(row = 1, column = 0)
        self.entry_lname.grid(row = 1, column = 1)
        # places both address wigets
        label_address1.grid(row = 2, column = 0)
        self.entry_address1.grid(row = 2, column = 1)
        label_address2.grid(row = 3, column = 0)
        self.entry_address2.grid(row = 3, column = 1)
        
        #places account type wigets
        label_account.grid(row = 4, column = 0)
        self.entry_account.grid(row = 4, column = 1)
        
        #places login info widgets
        label_user.grid(row = 5, column = 0)
        self.entry_user.grid(row = 5, column = 1)
        label_pin.grid(row = 6, column = 0)
        self.entry_pin.grid(row = 6, column = 1)
        
        #places buttons
        self.button_create.grid(row = 7, column = 0)
        self.button_menu.grid(row = 7, column = 1)

    #Create account object
    def create_account_button_click(self):
        
        cfname= self.entry_fname.get()
        clname= self.entry_lname.get()
        # added the other information to retrieve on click
        cadd1 = self.entry_address1.get()
        cadd2 = self.entry_address2.get()
        ctype = self.entry_account.get()
        cuser = self.entry_user.get()
        cpin = self.entry_pin.get()
        #get() address line1, line2, type, username and pin

        self.clear_frame()
        label_accountno = Label(self, text = "Your account no: ")
        self.accountno  = StringVar(self, '') #create StringVar object
        label_final_accountno  = Label(self, \
                                        textvariable=self.accountno) #associate self.result with this label


        s = createAccountNo()
        self.accountno.set(s) #setting the self.result label

        #create account object for each type of account
        #self.account = Account(accountno = s, acctype = ctype,\
         #                      fname = cfname, lname = clname, line1 = cadd1,\
          #                      line2 = cadd2, username = cuser, pin = cpin)
        
        if ctype.lower() == 'saving': #creating saving object
            self.account = Saving(accountno = s, acctype = ctype,\
                               fname = cfname, lname = clname, line1 = cadd1,\
                                line2 = cadd2, username = cuser, pin = cpin)
        elif ctype.lower() == 'checking': #create checking object
            self.account = Checking(accountno = s, acctype = ctype,\
                               fname = cfname, lname = clname, line1 = cadd1,\
                                line2 = cadd2, username = cuser, pin = cpin)
        
        self.bank.display() #for printing purpose, not for user
        self.button_next  = Button(self, text = "Please Login Again", command=self.existing_account_widget)
        label_accountno.grid(column=0, columnspan = 2)
        label_final_accountno.grid(column=0, columnspan = 2)
        self.button_next.grid(column = 0, columnspan = 2 )
 

    def existing_account_widget(self):
        self.clear_frame()
         # creates username label and entry
        label_exist_user = Label(self, text = 'Username')
        self.entry_exist_user = Entry(self, width=15)
        
        # creates pin label and entry
        label_exist_pin = Label(self, text = 'Pin')
        self.entry_exist_pin = Entry(self, width=15)
        #places login info widgets
        label_exist_user.grid(row = 0, column = 0)
        self.entry_exist_user.grid(row = 0, column = 1)
        label_exist_pin.grid(row = 1, column = 0)
        self.entry_exist_pin.grid(row = 1, column = 1)
        # create buttons
        self.button_menu = Button(self, text = 'Main Menu', command = \
                                  self.welcome)
        self.button_login = Button(self, text = 'Login', command = \
                                   self.login_button_click)
        # place buttons
        self.button_login.grid(row = 2, column = 0, columnspan = 2)
        self.button_menu.grid(row = 3, column = 0, columnspan = 2)
        #login widget
        #username, pin: label and entry
        #login, main menu: buttons

    def login_button_click(self):
        u = self.entry_exist_user.get() #get username
        p = self.entry_exist_pin.get() #get pin
        if (self.bank.login_validity(u, p)): #check validity using login_validity
            self.account = self.bank.load_account(u, p) #returns account object
            self.existing_user_options()
        else: #if invalid ask again
            self.existing_account_widget()
            

    def existing_user_options(self):
        self.clear_frame()
        # creates and places deposit button
        self.deposit_button  = Button(self, text = "Deposit", \
                                      command=self.deposit_interface)
        self.deposit_button.grid(row = 0, column = 0, columnspan = 2)
        # creates and places withdraw button
        self.withdraw_button  = Button(self, text = "Withdraw", \
                                      command=self.withdraw_interface)
        self.withdraw_button.grid(row = 1, column = 0, columnspan = 2)
        # creates and places account summary button
        self.summary_button  = Button(self, text = "Account Summary", \
                                      command=self.summary_interface)
        self.summary_button.grid(row = 2, column = 0, columnspan = 2)
        # creates and places logout button
        self.logout_button  = Button(self, text = "Logout", \
                                      command=self.welcome)
        self.logout_button.grid(row = 3, column = 0, columnspan = 2)
        # creates and places exit app button
        self.exit_button  = Button(self, text = "Exit Application", \
                                      command=self.exit_application)
        self.exit_button.grid(row = 4, column = 0, columnspan = 2)
        #your code here
        #withdraw, summary, logout and exit application
        #button, step 5 in spec

    def summary_interface(self):
        self.clear_frame()
        
        # acc no label and button
        self.label_accno = Label(self, text = 'Account Number')
        self.label_accno.grid(row = 0, column = 0)
        self.entry_accno = Entry(self, width = 15)
        self.entry_accno.grid(row = 0, column = 1)
        
        # buttons
        self.button_options = Button(self, text = 'Options',\
                                     command = self.existing_user_options)
        self.button_options.grid(row = 1, column = 0)
        
        self.button_next = Button(self, text = 'Next', command = self.summary)
        self.button_next.grid(row = 1, column = 1) 
        
        #create label and entry for Account Number
        #button: Options: command = existing_user_options method
        #button: Next: command = summary method
        

    def summary(self):
        accno = self.entry_accno.get() #obtains account no from user
        self.account.getBalance(accno)
        '''
        name, address, acctype, balance = self.account.summary(accno)
        
        self.clear_frame()
        self.info_label = Label(self, text = "Account Information")
        self.name_label = Label(self, text = name)
        self.address_label = Label(self, text = address)
        self.acctype_label = Label(self, text = acctype)
        self.balance_label = Label(self, text = str(balance))
        self.info_label.pack()
        self.name_label.pack()
        self.address_label.pack()
        self.acctype_label.pack()
        self.balance_label.pack()
        

        self.button_options  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.button_options.pack()
        '''
    def deposit_interface(self):
        self.clear_frame()
        #your code here
        #step 6 in spec
        #Next button will call deposit, please see summary interface function 

    def deposit(self):
        d = self.entry_deposit.get()
        accno = self.entry_accno.get()
        self.account.deposit(d, accno)
        self.check_balance(accno)

        
    def withdraw_interface(self):
        self.clear_frame()
        self.clear_frame()
        #your code here
        #same as depost interface, see step 7 in spec


    def withdraw(self):
        pass
        #your code here
        #same as deposit


        
    def check_balance(self, accno):

        self.clear_frame()
        label_balance = Label(self, text = 'Current balance: ' + \
                              str(self.account.getBalance(accno)))
        label_balance.grid()
        
        self.options_button  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.options_button.grid()


             
#driver
root = Tk()
frame = MyFrame(root)
frame.pack()
root.mainloop()
