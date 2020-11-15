
class FSM:
    d1 = False
    d2 = False

    def reset(self):
        self.d1 = False
        self.d2 = False

    def process(self, i):
        output = i and not self.d2
        self.d2 = output and self.d1
        self.d1 = output
        # print("state: {}{}".format(int(self.d1), int(self.d2)))
        return bool(output)

