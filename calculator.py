class Calc(object):
#@staticmethod
    def ADD(input):
        if input == "":
            return 0
        if input.isdigit():
            return int(input)
        if len(input.split(",")) > 1 and "\n" not in input:
            my_list = [int(i) for i in input.split(",")]
            return sum(my_list)
        if "\n" in input:
            new_input = input.replace("\n", ",")
            my_list = [int(i) for i in new_input.split(",")]
            return sum(my_list)