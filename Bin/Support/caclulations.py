from Bin.Classes.contract import contract
from Bin.Classes.performanceObligation import performanceObligation
from Bin.Support.accontingTreatment import intervalPayment
import csv


def calculatePropotionOfToalStandaloePrice(newContract, performanceObligations):
    totStandAlonePrice = newContract.getTotalStandAlonePrice(performanceObligations)
    transactionPrice = newContract.getTransactionPrice()
    print(transactionPrice)
    print(totStandAlonePrice)
    for i in range(len(performanceObligations)):
        print(performanceObligations[i].getPropotionOfTotalStandAlonePrice(totStandAlonePrice))
    response = [{'Field': 'Transaction Price', 'Amounts': transactionPrice},
                {'Field': 'Total StandAlone Price', 'Amounts': totStandAlonePrice}]
    data = intervalPayment(newContract, performanceObligations)
    a = list(data)
    print(len(a))
    return a
