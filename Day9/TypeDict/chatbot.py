from typing import Union, Sequence

InputData = Union[str,bytes]

def chatbots(inputs:Sequence[InputData]):
    for item in inputs:
        if isinstance(item,str):
            print("User Text: ", item)
        else:
            print("Image Uploaded: , (",len(item), "bytes)")

conversation = (
    "Hi",
    "Show me nearby restrtaunt",
    b'\x89PNG',
    "Explain this image"
)
chatbots(conversation)