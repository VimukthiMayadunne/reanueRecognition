from Bin.Support.getInput import setContractData, setPerformanceObligations
from Bin.Support.caclulations import calculatePropotionOfToalStandaloePrice

newContract = setContractData()
performanceObligations = setPerformanceObligations(newContract)
result = calculatePropotionOfToalStandaloePrice(newContract, performanceObligations)
