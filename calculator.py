class Calc(object):
#@staticmethod
    def ADD(input):
        if input == "":
            return 0
        if input.isdigit():
            return int(input)
        if len(input.split(",")) > 1:
            my_list = [int(i) for i in input.split(",")]
            return sum(my_list)