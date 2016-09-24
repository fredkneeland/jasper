import "number_generator"

class calculator():
    first_num
    second_num
    operation

    set_number(self, text):
        if not first_num:
            first_num = convert_text_to_int(text)
        else:
            second_num = convert_text_to_int(text)

    set_operation(self, text):
        operation = text

    compute(self):
        to_return = 0
        if operation == "plus":
            to_return = "" + (first_num + second_num)
        elif operation == "minus":
            to_retun = "" + (first_num - second_num)
        elif operation == "times":
            to_return = "" + (first_num * second_num)
        elif operation == "divide":
            to_return = "" + (first_num / second_num)
        
        operation = ""
        first_num = None
        second_num = None
        return to_return

