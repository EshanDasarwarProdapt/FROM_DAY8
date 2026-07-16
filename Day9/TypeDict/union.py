from typing import Union    

def process_input(data: Union[str, bytes])->None:
    if isinstance(data,str):
        print("Processing Text: ", data)
    elif isinstance(data, bytes):
        print("Processing Image/Audio Bytes: ", data)
process_input("Artificial Intelligence")
process_input(b'\x89PNG\r\n')

#Union-One variable can accept different datatype
#x89 -Non Printable Byte Used to identify the png image
#PNG- png image
#\r-Carriage return
#isinstance-checking the input datatype