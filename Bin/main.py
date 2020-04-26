from Bin.Classes.contract import contract
from Bin.Support.supportfunctions import trueFalse

contractor:str = input('Enter the Name of The Contractor')
contractee:str = input('Enter the Name of The Contractee')
duration: int = int(input('Enter the contract dureation in months:'))
print('Is the payment due in propotionate manner ?')
intervalPayment:bool =bool(trueFalse('Enter true or false:'))
print(intervalPayment)
if(intervalPayment):
    interval:int =int(input('Enter the time interval betwenn tow payments by number of months:'))
    ammount:float =float(input("Enter the ammout payble per time interval"))
    newContract = contract(contractor,contractee,duration,intervalPayment,interval,ammount)
else:
    ammount:float = float(input('Enter the ammount payable under contract:'))
    newContract = contract(contractor,contractee,duration,intervalPayment,None,ammount)

print(newContract.getTransactionPrice())
