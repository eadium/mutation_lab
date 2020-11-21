class FSM:
    d1 = False
    d2 = False

    def process(self, i: bool) -> bool:
        output = i or not self.d2
        self.d2 = output and self.d1
        self.d1 = output
        return bool(output)
