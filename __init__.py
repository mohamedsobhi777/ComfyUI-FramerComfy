

from .nodes.InputString import FramerComfyInputStringNode
from .nodes.InputNumber import FramerComfyInputNumberNode
from .nodes.InputImage import FramerComfyInputImageNode
from .nodes.InputFloat import FramerComfyFloatInputNode
from .nodes.InputBoolean import FramerComfyBooleanInputNode
from .nodes.OutputImage import FramerComfySaveImageNode

NODE_CLASS_MAPPINGS = {
    "FramerComfyInputStringNode": FramerComfyInputStringNode,
    "FramerComfyInputNumberNode": FramerComfyInputNumberNode,
    "FramerComfyInputImageNode": FramerComfyInputImageNode,
    "FramerComfyFloatInputNode": FramerComfyFloatInputNode,
    "FramerComfyBooleanInputNode": FramerComfyBooleanInputNode,
    "FramerComfySaveImageNode": FramerComfySaveImageNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FramerComfyInputStringNode": "FramerComfy Input String", 
    "FramerComfyInputNumberNode": "FramerComfy Input Number", 
    "FramerComfyInputImageNode": "FramerComfy Input Image", 
    "FramerComfyFloatInputNode": "FramerComfy Input Float",
    "FramerComfyBooleanInputNode": "FramerComfy Input Boolean",
    "FramerComfySaveImageNode": "FramerComfy Save Image"
}
