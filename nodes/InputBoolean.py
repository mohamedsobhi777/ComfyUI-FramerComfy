class BooleanInput:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": "bool_input"}),
                "value": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "get_value"
    CATEGORY = "FramerComfy"

    def get_value(self, name, value):
        return (value,)

