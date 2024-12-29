

class FramerComfyInputNumberNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": "int_input"}),
                "number": ("INT", {"default": 0}),
                "min": ("INT", {"default": -(2**31)}),
                "max": ("INT", {"default": 2**31 - 1}),
                "step": ("INT", {"default": 1}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "get_number"
    CATEGORY = "FramerComfy"


    def get_number(self, name, number, min, max, step):
        return (number,)
