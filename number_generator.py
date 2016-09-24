import math

units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]


tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

scales = ["hundred", "thousand", "million", "billion", "trillion"]
scales_to_value = [2, 3, 6, 9, 12]


def convert_text_to_int(text):
    _split_string = text.replace("-", " ").split(" ")
    _currentMultiple = 0
    _currentSmall = 0
    _currentTotal = 0    
    for word in _split_string:
        if word in units or word.upper() == "AND":
            _currentTotal += _currentSmall
            _currentSmall = 10 * _currentMultiple + units.index(word)
            _currentMultiple = 0
        elif word in tens:   
            _currentMultiple = tens.index(word)
            print(_currentMultiple)
        elif word in scales:
            _multiple = math.pow(10, scales_to_value[scales.index(word)])
            _currentSmall *= _multiple
    _currentTotal += _currentSmall
    return _currentTotal
                        
print convert_text_to_int("two trillion seven hundred forty-three billion sixteen million seven thousand four hundred thirty-six")
