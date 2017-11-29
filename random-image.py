from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests
from io import BytesIO

response = requests.get("https://source.unsplash.com/collection/1053828/1920x1080")
pattern = Image.open(BytesIO(response.content), "r").convert('RGB')

size = width, height = pattern.size
draw = ImageDraw.Draw(pattern,'RGBA')
font = ImageFont.truetype("segoeui.ttf", 140)

draw.text((750,375), "10:00", (255, 255, 255, 0),font=font)
font = ImageFont.truetype("segoeui.ttf", 65)
draw.text((847,550), "Hello", (255, 255, 255, 0),font=font)
pattern.save('output.jpg')