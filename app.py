import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
from authtoken import auth_token

import torch
from diffusers import StableDiffusionPipeline

# App window setup
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")


prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")


prompt.place(x=10, y=10)


lmain = ctk.CTkLabel(master=app, height=512, width=512)

lmain.place(x=10, y=110)

# Load Model (without autocast, without fp16)
modelid = "CompVis/stable-diffusion-v1-4"
device = "cpu"
pipe = StableDiffusionPipeline.from_pretrained(modelid, use_auth_token=auth_token)
pipe.to(device)

# Image Generation
def generate():
    image = pipe(prompt.get(), guidance_scale=8.5).images[0]
    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)
    lmain.image = img  # Important! Avoids garbage collection

# Button

trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue", command=generate)

trigger.configure(text="Generate")
trigger.place(x=206, y=60)

app.mainloop()
