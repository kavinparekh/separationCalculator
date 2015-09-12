class NotConnected(Exception):
    def __init__(self, arg):
        self.msg = arg