

from .nodes.InputString import FramerComfyInputStringNode
from .nodes.InputNumber import FramerComfyInputNumberNode
from .nodes.InputImage import FramerComfyInputImageNode
from .nodes.InputFloat import FloatInput
from .nodes.InputBoolean import BooleanInput
from .nodes.OutputImage import FramerComfySaveImageNode

NODE_CLASS_MAPPINGS = {
    "FramerComfyInputStringNode": FramerComfyInputStringNode,
    "FramerComfyInputNumberNode": FramerComfyInputNumberNode,
    "FramerComfyInputImageNode": FramerComfyInputImageNode,
    "FramerComfyFloatInputNode": FloatInput,
    "FramerComfyBooleanInputNode": BooleanInput,
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
