class Move:


    def __init__(self, value) -> None:
        self._value = value


    @property
    def value(self):
        return self._value
    

    def is_valid(self):
        return 1 <= self._value <= 9
    

    def get_row(self):
        return (self._value - 1) // 3
    

    def get_column(self):
        return (self._value - 1) % 3