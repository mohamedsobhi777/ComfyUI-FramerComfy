

from .nodes.InputString import FramerComfyInputStringNode
from .nodes.InputNumber import FramerComfyInputNumberNode
from .nodes.InputImage import FramerComfyInputImageNode

NODE_CLASS_MAPPINGS = {
    "FramerComfyInputStringNode": FramerComfyInputStringNode,
    "FramerComfyInputNumberNode": FramerComfyInputNumberNode,
    "FramerComfyInputImageNode": FramerComfyInputImageNode    
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FramerComfyInputStringNode": "FramerComfy Input String", 
    "FramerComfyInputNumberNode": "FramerComfy Input Number", 
    "FramerComfyInputImageNode": "FramerComfy Input Image"
}
