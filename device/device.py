class Device():
    name = None
    bus = None
    variables = dict()
    
    def __init__(self, config, bus):
        # Assert the existence of some items
        assert 'name' in config, 'A device should have a name'

        # Set properties from config
        self.name = config['name']
        if 'variables' in config:
            for variable in config['variables']:
                pass


    def emit(self, variable, value):
        """Emit a new variable value to the other devices"""
        self.getBus().updateValue(self.name, variable, value)

        
    def getName(self):
        return self.name
    
    def setBus(self, bus):
        self.bus = bus
        
    def getBus(self):
        return self.bus
    
    def notify(self, device, variable, value):
        pass