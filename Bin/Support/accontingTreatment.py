def prePayment():
    print('Method Under Construction')
    return None


def intervalPayment(contract, performanceObligations):
    print('Methnata AWA')
    results = map(lambda performanceObligation: checkPos(performanceObligation,contract), performanceObligations)
    return results


def checkPos(performaceObligation, contract):
    if performaceObligation.recurrent:
        return checkSync(performaceObligation, contract)
    else:
        return checkWhenToPerform(performaceObligation, contract)


def checkWhenToPerform(performaceObligation, contract):
    if performaceObligation.whenToPerform == 0:
        collection=[]
        collection.append({'Name': performaceObligation.name, 'Time': 'At the Begging of TheContract'})
        collection.append({'DrCr': 'Dr', 'AccountName': 'Contract Asset',
                           'Amount': performaceObligation.getActualPrice(contract.getTransactionPrice())})
        collection.append({'DrCr': 'Cr', 'AccountName': 'Revenue',
                           'Amount': performaceObligation.getActualPrice(contract.getTransactionPrice())})
        collection.append({'Name': performaceObligation.name, 'Time': 'Each month'})
        collection.append({'DrCr': 'Dr', 'AccountName': 'Receivables',
                           'Amount': (performaceObligation.getActualPrice(
                               (contract.getTransactionPrice())) / contract.getContactDuration())})
        collection.append({'DrCr': 'Cr', 'AccountName': 'ContractAsset',
                           'Amount': (performaceObligation.getActualPrice(
                               (contract.getTransactionPrice())) / contract.getContactDuration())})
        return collection
    else:
        print('Method Under Construction')
        return None


def checkSync(performaveObligation, contract):
    if performaveObligation.recurrentInterval is not None:
        return checkIntreval(performaveObligation, contract)
    else:
        print('Method Under Construction')
        return None


def checkIntreval(performaceObligation, contract):
    if performaceObligation.recurrentInterval == 1:
        collection=[]
        collection.append({'Name': performaceObligation.name, 'Time': 'Each Month'})
        collection.append({'DrCr': 'Dr', 'AccountName': 'Receivables',
                           'Amount': performaceObligation.getActualPrice(
                               contract.getTransactionPrice()) / contract.duration})
        collection.append({'DrCr': 'Cr', 'AccountName': 'Revenue',
                           'Amount': performaceObligation.getActualPrice(
                               contract.getTransactionPrice()) / contract.duration})
        return collection
    else:
        print('Method Under Construction')
        return None
