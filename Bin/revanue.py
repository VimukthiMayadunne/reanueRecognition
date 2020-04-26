from Bin.Support import transActionPrice, printData

duration: int = int(input('Enter the contract dureation in months:'))
print('Enter the Payment interval for the Contract')
printData.timeIntervals()
paymentMethord: int = int(input("Enter The Number:"))
paymentAmount: int = int(input("Enter the Ammount:"))

transActionPrice: int = transActionPrice.getTransactionPrice(duration, paymentAmount, paymentMethord)
print('Transaction Price:', transActionPrice)
perfomansObligations =[]
standAlonePrice =[]
numberOfPerformanceObligations: int = int(input('Number of performance Obligations:'))
for i in range(numberOfPerformanceObligations):
    tempData= input('Performance Obligation:')
    perfomansObligations.append(tempData)
    tempData= int(input('Stand Alone Price:'))
    print('Enter when to complete the performance obligation')
    printData.timeIntervals()
    paymentMethord: int = int(input("Enter The Number:"))
print(perfomansObligations)
print(transActionPrice)

