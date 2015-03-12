from bus.bus import Bus

class Pimotica():
    bus = None
    config = None
    
    def __init__(self):
        self.bus = Bus()
    
    def start(self):
        self.config = self.loadConfig()
        self.bus.addDevice(TemperaturesensorDevice('inside temperature sensor'))
        
    
    def loadConfig(self):
        """Load the configuration and return it"""
        # TODO load from file
        #return {'devices': {'inside/temperature': {'type'}}}
        pass


if __name__ == '__main__':
    p = Pimotica()
    p.start()