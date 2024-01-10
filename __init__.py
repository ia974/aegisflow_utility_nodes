# IMAGE PassThrough (Aegis72)
# this node takes an image as an input andpasses it through. It is used for remote
# targeting with an "Anything Everywhere" node sender

import sys
import torch
import numpy as np
from PIL import Image, ImageFilter


p310_plus = (sys.version_info >= (3, 10))

MANIFEST = {
    "name": "Aegisflow Utility Nodes",
    "version": (1, 1, 0),
    "author": "Aegis72",
    "project": "https://majorstudio.gumroad.com",
    "description": "UtilityNodes for Aegisflow comfyui workflow, based heavily on WASquatch's image batch node",
}


class aegisflow_multi_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "latent": ("LATENT",),
                "model": ("MODEL",),                
                "vae": ("VAE",),
                "clip": ("CLIP",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "sdxl tuple": ("SDXL_TUPLE",),

            },
        }

    RETURN_TYPES = ("IMAGE", "MASK", "LATENT", "MODEL", "VAE", "CLIP", "CONDITIONING", "CONDITIONING", "SDXL_TUPLE",)
    RETURN_NAMES = ("image", "mask", "latent", "model", "vae", "clip", "positive", "negative", "sdxl tuple",)
    FUNCTION = "af_passnodes"
    CATEGORY = "AegisFlow/passers"

    def af_passnodes(self, **kwargs):
        output_order = ("image", "mask", "latent", "model", "vae", "clip", "positive", "negative", "sdxl tuple",)
        return [kwargs.setdefault(key, '0') for key in output_order]


# model PassThrough (Aegis72)
# this node takes a model as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_model_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "model": ("MODEL",),
            },
        }

    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "model_passer"
    CATEGORY = "AegisFlow/passers"

    def model_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 

# clip PassThrough (Aegis72)
# this node takes CLIP as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_clip_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "clip": ("CLIP",),
            },
        }

    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("clip",)
    FUNCTION = "clip_passer"
    CATEGORY = "AegisFlow/passers"

    def clip_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 

# PosNeg PassThrough (Aegis72)
# this node takes CLIP as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_posneg_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
            },
        }

    RETURN_TYPES = ("CONDITIONING","CONDITIONING",)
    RETURN_NAMES = ("positive","negative",)
    FUNCTION = "posneg_passer"
    CATEGORY = "AegisFlow/passers"

    def posneg_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 

# Conditioning PassThrough (Aegis72)
# this node takes CONDITIONING as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_cond_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "conditioning": ("CONDITIONING",),
            },
        }

    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("conditioning",)
    FUNCTION = "conditioning_passer"
    CATEGORY = "AegisFlow/passers"

    def conditioning_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 
    
# SDXL Tuple PassThrough (Aegis72)
# this node takes CONDITIONING as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_sdxltuple_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "sdxl tuple": ("SDXL_TUPLE",),
            },
        }

    RETURN_TYPES = ("SDXL_TUPLE",)
    RETURN_NAMES = ("sdxl tuple",)
    FUNCTION = "tuple_passer"
    CATEGORY = "AegisFlow/passers"

    def tuple_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None]     

# vae PassThrough (Aegis72)
# this node takes a vae as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender



class aegisflow_vae_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "vae": ("VAE",),
            },
        }

    RETURN_TYPES = ("VAE",)
    RETURN_NAMES = ("vae",)
    FUNCTION = "vae_passer"
    CATEGORY = "AegisFlow/passers"

    def vae_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 


class aegisflow_image_pass:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "image": ("IMAGE",),
                "mask": ("MASK",),    
            },
        }

    RETURN_TYPES = ("IMAGE", "MASK",)
    RETURN_NAMES = ("image", "mask",)
    FUNCTION = "image_passer"
    CATEGORY = "AegisFlow/passers"

    def image_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None]  


# LATENT PassThrough (Aegis72)
# this node takes an latent as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender

class aegisflow_latent_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "latent": ("LATENT",),
            },
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "latent_passer"
    CATEGORY = "AegisFlow/passers"

    def latent_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None]  

# MASK PassThrough (Aegis72)
# this node takes a mask as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_mask_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "mask": ("MASK",),
            },
        }

    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = "mask_passer"
    CATEGORY = "AegisFlow/passers"

    def mask_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None]  


# ---------------------------------------------------------------------------------------------------------------------#
# This is an input switch for Controlnet Preprocessors.  Can pick an input and that image will be the one picked for the workflow.
class af_preproc_chooser:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 9}),
            },
            "optional": {
                "c1_passthrough": ("IMAGE",),
                "c2_normal_lineart": ("IMAGE",),
                "c3_anime_lineart": ("IMAGE",),
                "c4_manga_lineart": ("IMAGE",),
                "c5_midas_depthmap": ("IMAGE",),
                "c6_color_palette": ("IMAGE",),
                "c7_canny_edge": ("IMAGE",),
                "c8_openpose_recognizer": ("IMAGE",),
                "c9_scribble_lines": ("IMAGE",),
                "c10_yourchoice1": ("IMAGE",),
                "c11_yourchoice2": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "af_preproc_chooser"
    CATEGORY = "AegisFlow/passers"

    def af_preproc_chooser(self, Input, to_process=None, c1_passthrough=None, c2_normal_lineart=None, c3_anime_lineart=None, c4_manga_lineart=None, c5_midas_depthmap=None, c6_color_palette=None, c7_canny_edge=None, c8_openpose_recognizer=None, c9_scribble_lines=None, c10_yourchoice1=None, c11_yourchoice2=None,):
        if Input == 1:
            return (c1_passthrough, )
        elif Input == 2:
            return (c2_normal_lineart, )
        elif Input == 3:
            return (c3_anime_lineart, )
        elif Input == 4:
            return (c4_manga_lineart, )
        elif Input == 5:
            return (c5_midas_depthmap, )
        elif Input == 6:
            return (c6_color_palette, )
        elif Input == 7:
            return (c7_canny_edge, )
        elif Input == 8:
            return (c8_openpose_recognizer, )
        elif Input == 9:
            return (c9_scribble_lines, )
        elif Input == 10:
            return (c10_yourchoice1, )
        else:
            return (c11_yourchoice2, )

# Developed by Ally - https://www.patreon.com/theally
# https://civitai.com/user/theally

# This node provides a simple interface to adjust the brightness/contrast of the output image prior to saving
# many users were having difficulties with both installing and keeping theAlly nodes consistent and so I am integrating the three required them into this node set.


class BrightnessContrast_theAlly:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types

        """
        return {
            "required": {
                "image": ("IMAGE",),
                "mode": (["brightness", "contrast"],),
                "strength": ("FLOAT", {"default": 0.5, "min": -1.0, "max": 1.0, "step": 0.01}),
                "enabled": ("BOOLEAN", {"default": True},),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_filter"

    CATEGORY = "AegisFlow/fx"

    def apply_filter(self, image, mode, strength, enabled):
        # Choose a filter based on the 'mode' value
        if enabled:
            if mode == "brightness":
                image = np.clip(image + strength, 0.0, 1.0)
            elif mode == "contrast":
                image = np.clip(image * strength, 0.0, 1.0)
            else:
                print(f"Invalid filter option: {mode}. No changes applied.")
        return (image,)


# Developed by Ally - https://www.patreon.com/theally
# https://civitai.com/user/theally

# This node provides a simple interface to flip the image horizontally or vertically prior to saving

class ImageFlip_theAlly:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "flip_type": (["horizontal", "vertical"],),
                "enabled": ("BOOLEAN", {"default": True},),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "flip_image"
    CATEGORY = "AegisFlow/fx"

    def flip_image(self, image, flip_type, enabled):

        # Convert the input image tensor to a NumPy array
        image_np = 255. * image.cpu().numpy().squeeze()

        if not enabled:
            return (image,)

        if flip_type == "horizontal":
            flipped_image_np = np.flip(image_np, axis=1)
        elif flip_type == "vertical":
            flipped_image_np = np.flip(image_np, axis=0)
        else:
            print("Invalid flip_type. Must be either 'horizontal' or 'vertical'. No changes applied.")
            return (image,)
        # Convert the flipped NumPy array back to a tensor
        flipped_image_np = flipped_image_np.astype(np.float32) / 255.0
        flipped_image_tensor = torch.from_numpy(flipped_image_np).unsqueeze(0)

        return (flipped_image_tensor,)


# Developed by Ally - https://www.patreon.com/theally
# https://civitai.com/user/theally

# This node provides a simple interface to apply a gaussian blur approximation (with box blur) to the image prior to output

class GaussianBlur_theAlly:
    """
    This node provides a simple interface to apply Gaussian blur to the output image.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "image": ("IMAGE",),
                "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 200.0, "step": 0.01}),
                "enabled": ("BOOLEAN", {"default": True},),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_filter"

    CATEGORY = "AegisFlow/fx"

    def apply_filter(self, image, strength, enabled):

        if not enabled:
            return (image,)

        i = 255. * image.cpu().numpy().squeeze()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

        # Apply Gaussian blur using the strength value
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=strength))

        # Convert the blurred PIL Image back to a tensor
        blurred_image_np = np.array(blurred_img).astype(np.float32) / 255.0
        blurred_image_tensor = torch.from_numpy(blurred_image_np).unsqueeze(0)
        return (blurred_image_tensor,)


class af_placeholdertuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {}}

    RETURN_TYPES = ("SDXL_TUPLE",)
    FUNCTION = "placeholdertuple"
    CATEGORY = "AegisFlow/placeholders"

    def placeholdertuple(self,):

        provided_tuple_string = "(<comfy.model_patcher.ModelPatcher object at 0x00000215AF92E410>, " \
                                "<comfy.sd.CLIP object at 0x0000021582576110>, " \
                                "[[tensor([[[-0.3921,  0.0278, -0.0675,  ..., -0.4916, -0.3165,  0.0655], " \
                                "[-0.6300, -0.3306,  0.3012,  ...,  0.2379, -0.3163,  0.4271], " \
                                "[ 0.2102,  0.3428,  0.3694,  ..., -1.1688, -1.4279, -0.7521], " \
                                "..., " \
                                "[-0.3279, -0.1775, -1.6074,  ..., -0.3802, -1.1385, -0.0408], " \
                                "[-0.3222, -0.1721, -1.5919,  ..., -0.3691, -1.1436, -0.0270], " \
                                "[-0.3520, -0.0728, -1.5434,  ..., -0.3932, -1.0915, -0.0713]]]), {'pooled_output': None}]], " \
                                "[[tensor([[[-0.3921,  0.0278, -0.0675,  ..., -0.4916, -0.3165,  0.0655], " \
                                "[-0.6300, -0.3306,  0.3012,  ...,  0.2379, -0.3163,  0.4271], " \
                                "[ 0.2102,  0.3428,  0.3694,  ..., -1.1688, -1.4279, -0.7521], " \
                                "..., " \
                                "[-0.2891, -0.6821, -1.5167,  ..., -0.6290, -1.7984,  0.3385], " \
                                "[-0.2864, -0.6799, -1.5096,  ..., -0.6233, -1.7977,  0.3522], " \
                                "[-0.2866, -0.5871, -1.4560,  ..., -0.6451, -1.7306,  0.2990]]]), {'pooled_output': None}]], " \
                                "None, None, None, None)"
        result = tuple(provided_tuple_string.split(", "))
        return (result,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "aegisflow Multi_Pass": aegisflow_multi_pass,
    "Aegisflow Image Pass": aegisflow_image_pass,
    "Aegisflow Mask Pass": aegisflow_mask_pass,
    "Aegisflow Latent Pass": aegisflow_latent_pass,
    "Aegisflow Model Pass": aegisflow_model_pass,
    "Aegisflow VAE Pass": aegisflow_vae_pass,
    "Aegisflow CLIP Pass": aegisflow_clip_pass,
    "Aegisflow Conditioning Pass": aegisflow_cond_pass,
    "Aegisflow Pos/Neg Pass": aegisflow_posneg_pass,
    "Aegisflow SDXL Tuple Pass": aegisflow_sdxltuple_pass,
    "Aegisflow Controlnet Preprocessor Bus": af_preproc_chooser,
    "Brightness & Contrast_Ally": BrightnessContrast_theAlly,
    "Image Flip_ally": ImageFlip_theAlly,
    "Gaussian Blur_Ally": GaussianBlur_theAlly,
    "Placeholder Tuple": af_placeholdertuple
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "WEB_DIRECTORY"]
