from Bin.Support.getInput import setContractData, setPerformanceObligations

newContract = setContractData()
performanceObligations = setPerformanceObligations(newContract)

totStandalonePrice = sum(c.standAlonePriceForPerformanceObligation for c in performanceObligations)
transactionPrice = newContract.getTransactionPrice()
print(transactionPrice)
print(totStandalonePrice)
