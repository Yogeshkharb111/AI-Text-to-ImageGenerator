# 🖼️ Stable Diffusion Text-to-Image Generator

A simple and interactive **AI-Powered Text-to-Image Generator** built using Python, Stable Diffusion, and Tkinter. This app takes user prompts and generates high-quality images using the Stable Diffusion model.

---

## ✨ Features

- GUI-based Text-to-Image Generation using **Stable Diffusion v1-4**
- Built with **Tkinter** and **CustomTkinter** for a clean and responsive interface
- Generates images from any custom text prompt
- Real-time preview of the generated image
- Supports CPU (for local) and GPU (for Google Colab or CUDA devices)
- Save generated images easily

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter / CustomTkinter
- Hugging Face Diffusers
- Stable Diffusion v1-4
- PyTorch
- PIL (Python Imaging Library)

---

## 💾 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/text-to-image-stable-diffusion.git
    cd text-to-image-stable-diffusion
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have a valid HuggingFace token.
   - Create `authtoken.py`
   ```python
   auth_token = "your_huggingface_token_here"
