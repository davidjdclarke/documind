import openai
import requests

from datetime import datetime

openai.api_key = "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"

response = openai.Image.create(
    prompt="SmartDoc Logo",
    n=1,
    size="512x512",
)
image_url = response["data"][0]["url"]
print(image_url)

img = requests.get(image_url).content

# save image as png
with open(f"tmp/image.png-{datetime.now().}", "wb") as f:
    f.write(img)
