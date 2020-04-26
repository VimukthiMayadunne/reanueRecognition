from Bin.Classes.contract import contract
from Bin.Classes.performanceObligation import performanceObligation
from Bin.Support.supportfunctions import trueFalse


def setContractData():
    contractor: str = input('Enter the Name of The Contractor')
    contractee: str = input('Enter the Name of The Contractee')
    duration: int = int(input('Enter the contract dureation in months:'))
    print('Is the payment due in propotionate manner ?')
    intervalPayment: bool = bool(trueFalse('Enter true or false:'))
    print(intervalPayment)
    if (intervalPayment):
        interval: int = int(input('Enter the time interval betwenn tow payments by number of months:'))
        ammount: float = float(input("Enter the ammout payble per time interval"))
        newContract = contract(contractor, contractee, duration, intervalPayment, interval, ammount)
    else:
        ammount: float = float(input('Enter the ammount payable under contract:'))
        newContract = contract(contractor, contractee, duration, intervalPayment, None, ammount)
    return newContract

def setPerformanceObligations(newContract):
    performanceObligations = []
    numberOfPerformanceObligations: int = int(input('Number of performance Obligations:'))
    for i in range(numberOfPerformanceObligations):
        tempName = input('Performance Obligation:')
        tempStandAlonePrice = float(input('standAlonePrice:'))
        print("Is the performace obligation Recurent ?")
        tempRecurent = bool(trueFalse('Enter true or false:'))
        if (tempRecurent):
            tempRecurentInterval = int(input('Enter the recurrent interval in months'))
            newPerformanceObligation = performanceObligation(tempName, tempStandAlonePrice, tempRecurent,
                                                             tempRecurentInterval, None, newContract.getContactDuration())
        else:
            tempWhenToPerform = int(input('When to Performa the aggred performance obligation'))
            newPerformanceObligation = performanceObligation(tempName, tempStandAlonePrice, tempRecurent, None,
                                                             tempWhenToPerform, newContract.getContactDuration())
        performanceObligations.append(newPerformanceObligation)
    return performanceObligations
