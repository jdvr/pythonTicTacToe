

class Player(object):

    def __init__(self, tpe):
        self.__type = tpe

    def get_type(self):
        return self.__type

    def to_string(self):
        return "Player: %s " % self.__type.to_string()
