class Device():
    name = None
    bus = None
    
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setBus(self, bus):
        self.bus = bus
        
    def getBus(self):
        return self.bus
    
    def notify(self, name, value):
        pass