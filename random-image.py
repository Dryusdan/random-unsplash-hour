from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests
from io import BytesIO
from mastodon import Mastodon

# Load secrets from secrets file
secrets_filepath = "secrets/secrets.txt"
uc_client_id     = get_parameter("client_id",     secrets_filepath)
uc_client_secret = get_parameter("client_secret", secrets_filepath)
uc_access_token = get_parameter("access_token", secrets_filepath)
mastodon_hostname = get_parameter("mastodon_hostname", config_filepath) # E.g., mastodon.social

mastodon = Mastodon(
    client_id = uc_client_id,
    client_secret = uc_client_secret,
    access_token = uc_access_token,
    api_base_url = 'https://' + mastodon_hostname,
)

response = requests.get("https://source.unsplash.com/collection/1053828/1920x1080")
pattern = Image.open(BytesIO(response.content), "r").convert('RGB')

size = width, height = pattern.size
draw = ImageDraw.Draw(pattern,'RGBA')
font = ImageFont.truetype("segoeui.ttf", 140)

draw.text((750,375), "10:00", (255, 255, 255, 0),font=font)
font = ImageFont.truetype("segoeui.ttf", 65)
draw.text((847,550), "Hello", (255, 255, 255, 0),font=font)
pattern.save('output.jpg')

file_to_upload = 'output.jpg'

print "Uploading %s..."%file_to_upload
media_dict = mastodon.media_post(file_to_upload,"image/jpg")
mastodon.status_post(toot_text, in_reply_to_id=None, media_ids=[media_dict] )