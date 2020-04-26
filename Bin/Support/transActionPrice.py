from asn1crypto._ffi import null


def getTransactionPrice(duration: int, amount: int, methord: int) -> int:
    if(methord == 1):
        return uprontPayment(amount)
    elif(methord == 2):
        return monthlyPayments(duration,amount)
    else:
        print('Unable To Calculate Transaction price')
        return null()

def monthlyPayments(duration,amount):
    return duration*amount

def uprontPayment(amount):
    return amount

def atCompletion():
    return  null()
