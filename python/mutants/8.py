class FSM:
    d1 = False
    d2 = False

    def process(self, i: bool) -> bool:
        output = i and self.d2
        self.d2 = output and self.d1
        self.d1 = output
        return bool(output)
