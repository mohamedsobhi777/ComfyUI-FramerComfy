class FramerComfyInputImageNode:

    @classmethod  
    def INPUT_TYPES(cls):  
        return {
            "required": { 
                "name": ("STRING", {"default": "image_input"}),
                "image": ("IMAGE",), 
            },               
        }
    
    RETURN_TYPES = ("IMAGE","STRING",)
    FUNCTION = "get_image"
    CATEGORY = "FramerComfy"
    
    def get_image(self, name, image):  
        return (image,)