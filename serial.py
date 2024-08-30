"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Initialize with a starting number."""
        self.start = start
        self.current = start
    
    def __repr__(self):
        """Show representation."""
        return f"<SerialGenerator start={self.start} current={self.start}>" 
    
    def generate(self):
        """Returning the next serial number and adding by 1."""
        serial_num = self.current
        self.current += 1
        return serial_num
    
    def reset(self):
        """Resetting the serial number to the starting number."""
        self.current = self.start
            
