

class FramerComfyFloatInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": "float_input"}),
                "number": ("FLOAT", {"default": 0}),
                "min": ("FLOAT", {"default": -float(2**31)}),
                "max": ("FLOAT", {"default": float(2**31)}),
                "step": ("FLOAT", {"default": 0.1}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_number"
    CATEGORY = "FramerComfy"

    def get_number(self, name, number, min, max, step):
        return (number,)
