from number_generator import convert_text_to_int

class calculator():
    first_num = None
    second_num = None
    operation = None
    on_first_num = True

    def set_number(self, text):
        if self.on_first_num:
            self.first_num = convert_text_to_int(text)
        else:
            self.second_num = convert_text_to_int(text)
        self.on_first_num = not self.on_first_num

    def set_operation(self, text):
        self.operation = text

    def compute(self):
        to_return = 0
        if self.operation == "plus":
            to_return = str(self.first_num + self.second_num)
        elif self.operation == "minus":
            to_return = str(self.first_num - self.second_num)
        elif self.operation == "times":
            to_return = str(self.first_num * self.second_num)
        elif self.operation == "divide":
            to_return = str(self.first_num / self.second_num)
        
        return to_return

    def get_value_for_string(self, text):
        _splits = text.split("plus")
        _operation = "plus"
        if len(_splits) < 2:
            _operation = "minus"
            _splits = text.split(_operation)
        if len(_splits) < 2:
            _operation = "times"
            _splits = text.split(_operation)
        if len(_splits) < 2:
            _operation = "divide"
            _splits = text.split(_operation)
        self.set_number(_splits[0])
        self.set_operation(_operation)
        self.set_number(_splits[1])
        return self.compute()
            
calc = calculator()
print("four plus three: ",calc.get_value_for_string("four plus three"))
