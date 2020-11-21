class FSM:
    d1 = False
    d2 = False

    def process(self, i: bool) -> bool:
        output = not i and not self.d2
        self.d2 = output and self.d1
        self.d1 = output
        return not bool(output)
