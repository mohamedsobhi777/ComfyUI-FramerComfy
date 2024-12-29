

from .nodes.InputString import InputStringNode
from .nodes.InputNumber import InputNumberNode
from .nodes.InputImage import InputImageNode

NODE_CLASS_MAPPINGS = {
    "InputStringNode": InputStringNode,
    "InputNumberNode": InputNumberNode,
    "InputImageNode": InputImageNode    
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InputStringNode": "FramerComfy Input String", 
    "InputNumberNode": "FramerComfy Input Number", 
    "InputImageNode": "FramerComfy Input Image"
}
