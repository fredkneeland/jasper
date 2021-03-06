from calculator import calculator

# this is the priority by which this module will be choosen to see if it should be called
PRIORITY = 100
WORDS = ["CALCULATE"]

calculator = calculator()

# keep the context around if we can't understand the meaning of a text
_context = []

# point at which we dump context
IRRELEVANT = 10

# we always want is valid to return true so that we can always process the information
def isValid(text):
    if text is None or len(text) < 1:
        return False
    print(text)
    return True

def handle(text, mic, profile):
    reply = _processMessage(text, _context)

    _context.append(text)
    _context.append(reply)

    if len(_context) > IRRELEVANT:
        _context.pop(0)
        _context.pop(0)

    mic.say(reply)

def _processMessage(text, context):
    print(text)
    if "CALCULATE" in text:
        return "The result is ", calculator.get_value_for_string(text)
    
    return "Hello World ", text, " len: ", len(context)
