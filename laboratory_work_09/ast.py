class String:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class Print:
    def __init__(self, value):
        self.value = value

    def eval(self):
        result = self.value.eval()
        print(result)