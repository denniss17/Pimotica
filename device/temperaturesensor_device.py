from device import Device

class TemperaturesensorDevice(Device):
    name = None
    
    def __init__(self, config):
        super(TemperaturesensorDevice, self).__init__(config)