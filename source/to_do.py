class Complete():
    def __init__(self):
        self.value = False

    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value

    def toggle_value(self):
        self.value = not self.value

    def __repr__(self):
        """
        Return a string representation of the BooleanHolder.
        """
        return f"BooleanHolder({self.value})"