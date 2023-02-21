class Calculator:
    def __init__(self):
        self.x: int
        self.y: int
        self.result: int
        self.delta: int

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_result(self) -> int:
        return self.result

    def get_delta(self) -> int:
        return self.delta

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_delta(self, a:int, b:int, c:int) -> int:
        self.delta = (b*b)-(4*a*c)

    def set_result(self, result):
        self.result = result

    def add(self):
        self.set_result(self.x + self.y)

    def sub(self):
        self.set_result(self.x - self.y)

    def number_of_solutions(self) -> int:
        if self.delta > 0:
            return 2
        elif self.delta == 0:
            return 1
        else:
            return 0

    

    

    