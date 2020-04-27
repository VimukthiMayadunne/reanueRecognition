from Bin.Classes.contract import contract
from Bin.Classes.performanceObligation import performanceObligation

def calculatePropotionOfToalStandaloePrice(newContract, performanceObligations):
    totStandAlonePrice = sum(c.standAlonePriceForPerformanceObligation for c in performanceObligations)
    transactionPrice = newContract.getTransactionPrice()
    print(transactionPrice)
    print(totStandAlonePrice)
    for i in range(len(performanceObligations)):
        print(performanceObligations[i].getPropotionOfTotalStandAlonePrice(totStandAlonePrice))
    return 0
