from device.device import Device

class Bus():
    # All devices added to this bus
    devices = None
    # Current values
    values = None
    
    def __init__(self):
        self.devices = dict()
        self.values = dict()
    
    def addDevice(self, device):
        """Add a new device to this bus"""
        assert type(devices) is Device
        
        device.setBus(self)
        self.devices[device.getName()] = device
        
    def removeDevice(self, device):
        """Remove the given device from this bus"""
        self.devices.pop(device.getName())
        
    def getDevices(self):
        """Return all devices on this bus"""
        return self.devices
        
    def updateValue(self, device, variable, value):
        """Update a value with a new value and notify all devices"""
        if device not in self.values:
            self.values[device] = dict()
        self.values[device][variable] = value
        self.notifyDevices(device, variable, value)
        
    def getValue(self, name):
        """Return the current value of the value with the given name"""
        return self.values[name] if name in self.values else None
        
    def notifyDevices(self, name, variable, value):
        """Notify all devices that a certain value has changed"""
        for device in self.devices:
            device.notify(device, variable, value)
        
        
    