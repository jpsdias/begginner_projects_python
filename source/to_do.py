class Complete():
    def __init__(self, state: bool = False):
        self.value = state

    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value

    def toggle_value(self):
        self.value = not self.value

    def __repr__(self):
        return f"Complete({self.value})"
    
class Task(Complete):
    def __init__(self, description: str, state: bool = False):
        self.state = Complete(state)
        self.description = description
    
    def __repr__(self):
        return f"Task(description='{self.description}', completed={self.state.get_value()})"
