class Calc(object):
#@staticmethod
    def ADD(input):
        if input == "":
            return 0
        if input.isdigit():
            return int(input)
        if "-" in input:
            my_list = [int(i) for i in input.split(",")]
            negative_list = []
            for i in my_list:
                if i < 0:
                    negative_list.append(i)
            negative_list = (str(negative_list)[1:-1]).replace(" ", "")
            return "Negatives not allowed: {}".format(negative_list)
        if len(input.split(",")) > 1:
            if "\n" in input:
                new_input = input.replace("\n", ",")
                my_list = [int(i) for i in new_input.split(",")]
            else:
                my_list = [int(i) for i in input.split(",")]
                for i in my_list:
                    if i > 1000:
                        my_list.remove(i)
            return sum(my_list)

#elif