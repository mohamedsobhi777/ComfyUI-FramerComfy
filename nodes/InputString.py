class FramerComfyInputStringNode:
    
    @classmethod 
    def INPUT_TYPES(cls):
        return {
            "required": {  
                "name": ("STRING", {"default": "string_input"}),
            },
           "optional": {
               "default_value": ("STRING", {
                   "default": "",
                   "multiline": False, 
               })
           }                  
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_value"
    CATEGORY = "FramerComfy"
    
    def get_value(self, default_value):  
        return (default_value,)