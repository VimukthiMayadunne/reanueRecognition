from Bin.Support.getInput import setContractData, setPerformanceObligations

newContract = setContractData()
performanceObligations = setPerformanceObligations(newContract)

totStandAlonePrice = sum(c.standAlonePriceForPerformanceObligation for c in performanceObligations)
transactionPrice = newContract.getTransactionPrice()
print(transactionPrice)
print(totStandAlonePrice)
for i in range(len(performanceObligations)):
    print(performanceObligations[i].getPropotionOfTotalStandAlonePrice(totStandAlonePrice))
