class TemperaturesensorDevice(Device):
    name = None
    
    def __init__(self, name, valueName):
        super(TemperaturesensorDevice, self).__init__(name)