class Calc(object):
#@staticmethod
    def ADD(input):
        if input == "":
            return 0
        if input.isdigit():
            return int(input)