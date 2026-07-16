#Race- role, action, context, expectation - List of inputs

from typing import Sequence

def process_management(message: Sequence[str])->None:
    print('Message Received')

    for m in message:
        print(m)

text = {
    "Hello",
    "How are you ?",
    "Working wiht FastApi"
}

text_tuple = (
    "Checking the input",
    "Tuple input",
    "Working or not"
)
# process_management(text)
process_management(text_tuple)
