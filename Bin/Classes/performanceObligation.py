class performanceObligation:
    name: str
    standAlonePrice: float
    recurrent: bool
    recurrentInterval: int
    whenToPerform: int
    proportionOfTotalStandAlonePrice: float = None
    standAlonePriceForPerformanceObligation: float = None
    actualPrice: float = None

    def __init__(self, name, standAlonePrice, recurrent, recurentInteval, whenToPerforme, duration):
        self.name = name
        self.standAlonePrice = standAlonePrice
        self.recurrent = recurrent
        if recurrent:
            self.recurrentInterval = recurentInteval
            self.standAlonePriceForPerformanceObligation = self.standAlonePrice * (duration / recurentInteval)
        else:
            self.whenToPerform = whenToPerforme
            self.standAlonePriceForPerformanceObligation = standAlonePrice

    def getPropotionOfTotalStandAlonePrice(self, totalStandAlonePrice):
        if (self.proportionOfTotalStandAlonePrice != None):
            return self.proportionOfTotalStandAlonePrice
        else:
            return self.calculatePropotionOfTotalStandAlonePrice(totalStandAlonePrice)

    def calculatePropotionOfTotalStandAlonePrice(self, totalStandAlonePrice):
        self.proportionOfTotalStandAlonePrice = (self.standAlonePriceForPerformanceObligation /
                                                 totalStandAlonePrice)
        return self.proportionOfTotalStandAlonePrice

    def getActualPrice(self, transactionPrice):
        if self.actualPrice is None:
            return self.calculateActualPrice(transactionPrice)
        else:
            return self.actualPrice

    def calculateActualPrice(self, transactionPrice):
        self.actualPrice = transactionPrice * self.proportionOfTotalStandAlonePrice
        return self.actualPrice
