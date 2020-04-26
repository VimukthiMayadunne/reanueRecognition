class contract:
    contractor:str
    contractee:str
    duration:int
    intervalPayment:bool
    interval:int
    ammount:float
    transactionPrice:float = None

    def __init__(self,contractor,contractee,duration,intervalPayment,interval,ammount):
        self.contractor=contractor
        self.contractee=contractee
        self.duration=duration
        self.intervalPayment=intervalPayment
        if(intervalPayment):
            self.interval=interval
        self.ammount=ammount

    def getTransactionPrice(self):
        if(self.transactionPrice != None):
            return self.transactionPrice
        else:
            return self.calculateTransactionPrice()

    def calculateTransactionPrice(self):
        if(self.intervalPayment):
            self.transactionPrice=(self.duration/self.interval)*self.ammount
        else:
            self.transactionPrice=self.ammount
        return self.transactionPrice

