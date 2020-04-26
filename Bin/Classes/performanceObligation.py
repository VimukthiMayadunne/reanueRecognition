class performanceObligation:
    name:str
    standAlonePrice:float
    recurent:bool
    recurentIntrval:int
    whenToPerforme:int
    propotionOfTotalStandAlonePrice:float = None
    standAlonePriceForPerformanceObligation:float =None

    def __init__(self,name,standAlonePrice,recurent,recurentInteval,whenToPerforme,duration):
        self.name=name
        self.standAlonePrice=standAlonePrice
        self.recurent=recurent
        if(recurent):
            self.recurentIntrval=recurentInteval
            self.standAlonePriceForPerformanceObligation=self.standAlonePrice*(duration/recurentInteval)
        else:
            self.whenToPerforme=whenToPerforme
            self.standAlonePriceForPerformanceObligation=standAlonePrice

    def getPropotionOfTotalStandAlonePrice(self,totalStandAlonePrice):
        if(self.propotionOfTotalStandAlonePrice != None):
            return self.propotionOfTotalStandAlonePrice
        else:
            return self.calculatePropotionOfTotalStandAlonePrice(totalStandAlonePrice)

    def calculatePropotionOfTotalStandAlonePrice(self,totalStandAlonePrice):
        self.propotionOfTotalStandAlonePrice=(self.standAlonePriceForPerformanceObligation/totalStandAlonePrice)*100
        return self.propotionOfTotalStandAlonePrice

