from Bin.Classes.contract import contract
from Bin.Classes.performanceObligation import performanceObligation
from Bin.Support.caclulations import calculatePropotionOfToalStandaloePrice


def appendData(data):
    newContract = contract(data.get('contractor'), data.get('contractee'), data.get('duration'),
                           data.get('intervalPayment'), data.get('interval'), data.get('ammount'))

    performanceObligations = []
    for i in range(data.get('numberOfPerformanceObligations')):
        newPerformanceObligation = performanceObligation(data.get('poi')[i].get('Name'),
                                                         data.get('poi')[i].get('StandAlonePrice'),
                                                         data.get('poi')[i].get('Recurent'),
                                                         data.get('poi')[i].get('RecurentInterval'),
                                                         data.get('poi')[i].get('whenToPerform'),
                                                         newContract.getContactDuration())
        performanceObligations.append(newPerformanceObligation)
    print(data)
    results = calculatePropotionOfToalStandaloePrice(newContract, performanceObligations)
    return results
