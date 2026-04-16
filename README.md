# Prompt2Pixel

High-performance, serverless web application that transforms textual descriptions into high-fidelity images. By leveraging the **Stable Diffusion XL (SDXL)** model via Hugging Face's distributed Inference API, the project achieves high-end AI generation without requiring local GPU resources.

---

## Features
High-Resolution Synthesis: Generates 1024x1024 images using the state-of-the-art SDXL model.

* Serverless Infrastructure: Uses Hugging Face Inference API; no local model downloads or high-end hardware needed.

* Persistent State: Uses Streamlit Session State to keep your generated images visible across interactions.

* Fast & Lightweight: Optimized for low-latency inference on serverless nodes.

* Download Ready: Built-in serialization to download your creations instantly in PNG format.

* Clean Interface: Professional dashboard designed for clear input-output visualization.

---

## Project Structure
```
prompt2pixel/
│── LICENSE             # MIT License
│── main.py             # Entry point, launches Streamlit app
│── README.md           # Project documentation
│── requirements.txt    # Python dependencies
│── HF_TOKEN.txt        # Your Hugging Face API token (ignored in git)
│── utils/
    │── app.py          # Streamlit UI and logic
    │── models.py       # ImageEngine class and Inference API connection
```
--- 
## Requirements
* Python 3.9+ recommended

* Streamlit

* Hugging Face Hub

* Pillow (PIL)

---

## Install dependencies:
```
pip install -r requirements.txt
```

---

## Hugging Face Token
This project requires a personal Hugging Face API token.

1. Create an account at huggingface.co.

2. Get your Access Token from your profile settings.

3. Create a file called HF_TOKEN.txt inside the project root (prompt2pixel/) and paste your token there.

⚠️ HF_TOKEN.txt is already in .gitignore, so your token stays private.

---

## Run the App
Simply run:

```
python main.py
```

This will launch Streamlit and open the app in your browser.

---

## How It Works
You type a descriptive prompt in the text area (e.g., "A vintage photo of a robot drinking coffee").

The app sends the request to the Hugging Face Inference API using the model:

stabilityai/stable-diffusion-xl-base-1.0

---

## Inference Flow:

* The request is processed on remote A100/H100 GPUs.

* The model performs 25+ denoising steps in the latent space to synthesize the image.

* No models are downloaded locally, keeping the app extremely lightweight.

* The resulting binary data is captured in an io.BytesIO buffer.

* The app displays the image and generates a download link for the user.

---

## License
This project is licensed under the terms of the MIT License.
See the [LICENSE](LICENSE)  file for details.

---

## Acknowledgements
* Stability AI for the SDXL model weights.

* Hugging Face for the robust Inference API and hosting.

* Streamlit for making AI-powered dashboards fast and intuitive.
