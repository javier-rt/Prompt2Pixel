from huggingface_hub import InferenceClient
from PIL import Image

class ImageEngine:
    """
    Interface for text-to-image synthesis using Latent Diffusion Models.

    This class manages the connection to Hugging Face's Inference API and
    handles the transformation of natural language prompts into visual assets.

    Parameters
    ----------
    model_id : str, optional
        The Hugging Face model repository ID. 
        Defaults to "stabilityai/stable-diffusion-xl-base-1.0".

    Attributes
    ----------
    client : huggingface_hub.InferenceClient
        The authenticated client used to communicate with the Inference API.
    model_id : str
        The specific model identifier being used for generation.
    """

    def __init__(self, model_id: str = "stabilityai/stable-diffusion-xl-base-1.0"):
        self.model_id = model_id
        try:
            with open("HF_TOKEN.txt") as f:
                token = f.read().strip()

            self.client = InferenceClient(model=model_id, token=token)

        except FileNotFoundError:
            raise Exception("'HF_TOKEN.txt' not found. Please create the file with your HuggingFace token.")

    def generate(self, prompt: str) -> Image.Image:
        """
        Synthesize an image based on a textual description.

        Parameters
        ----------
        prompt : str
            The natural language description of the image to be generated.

        Returns
        -------
        PIL.Image.Image
            The generated image object.

        Raises
        ------
        Exception
            If the Inference API returns an error or if the 
            token is invalid/exhausted.
        """
        try:
            return self.client.text_to_image(
                prompt=prompt, 
                num_inference_steps=25,
                guidance_scale=7.5
            )
                
        except Exception as e:
            raise Exception(f"Inference API Error: {str(e)}")