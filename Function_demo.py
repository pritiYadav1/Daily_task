
UserName = "Name"
UserAge = 0
UserAddress= "Demo address"
UserAccountNumber=0
UserBalance=0

def acceptUserDetails() :
    global UserName,UserAge,UserAddress,UserAccountNumber,UserBalance
    UserName=input("Enter your name")
    UserAge=int(input("Enter your age"))
    UserAddress=input("Enter your address")
    UserAccountNumber=int(input("Enter account Number"))
    UserBalance=int(input("Enter the amount to open the account"))
   # displayUserDetails(UserName,UserAge,UserAddress,UserAccountNumber)
    
'''
def displayUserDetails(userName,userAge,userAdd,userAccNo):

    print("name:",userName)
    print("Age:",userAge)
    print("Address:",userAdd)
    print("Account Numbder:",userAccNo)
'''

def displayUserDetails():

    global UserName,UserAge,UserAddress,UserAccountNumber
    print("name:",UserName)
    print("Age:",UserAge)
    print("Address:",UserAddress)
    print("Account Numbder:",UserAccountNumber)

def transaction():
    global UserBalance
    choice=int(input("Press 1: Dep \n 2:With"))
    amount= int(input("Enter your amount"))
    if choice==1 :
        
        UserBalance=UserBalance+amount
        print("Balance : ",UserBalance)

    else:
        UserBalance=UserBalance-amount
        print("Balance : ",UserBalance)
    
    
 # create a  function which will describe loan (amount, year , Rate:7%)  final loan amount return   


    

acceptUserDetails()
transaction()
    
