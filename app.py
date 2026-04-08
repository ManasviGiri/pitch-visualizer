from flask import Flask, render_template, request
import os
from PIL import Image, ImageDraw

app = Flask(__name__)

# ✅ Step 1: Simple Text Segmentation (NO NLTK)
def split_text(text):
    sentences = text.split(".")
    return [s.strip() for s in sentences if s.strip() != ""]

# ✅ Step 2: Prompt Engineering
def enhance_prompt(sentence):
    return f"A detailed scene showing: {sentence}, high quality, realistic"

# ✅ Step 3: Image Generation (placeholder images)
def generate_image(prompt, index):
    img = Image.new('RGB', (512, 512), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.text((20, 200), prompt[:80], fill=(0, 0, 0))

    path = f"static/images/image_{index}.png"
    img.save(path)
    return path

@app.route("/", methods=["GET", "POST"])
def index():
    images = []
    captions = []

    if request.method == "POST":
        text = request.form["text"]

        sentences = split_text(text)

        for i, sentence in enumerate(sentences):
            prompt = enhance_prompt(sentence)
            image_path = generate_image(prompt, i)

            images.append(image_path)
            captions.append(sentence)

    return render_template("index.html", images=images, captions=captions)

if __name__ == "__main__":
    app.run(debug=True)