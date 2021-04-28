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
        """Initializing the given input as the starting value to generate a number sequence."""
        self.start = self.next = start

    def __repr__(self):
        """Shows string representation of the values."""
        return f"<SerialGenerator start={self.start} and next={self.next}>"

    def generate(self):
        """Increments the next value by 1 and displays the incrementation from the start value starting at the given input value."""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets the increment value to its original given input value."""
        self.next = self.start
