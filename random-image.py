#!/usr/bin/python3
# coding: utf-8
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
from mastodon import Mastodon
import requests
import os
import sys
import time
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--period", help="Time periode when script launch [morning | mid-morning | lunch | snack | apero | diner | night]")
parser.add_argument("--no-upload", help="Don't upload image")
args = parser.parse_args()

def get_parameter( parameter, file_path ):
    # Check if secrets file exists
    if not os.path.isfile(file_path):    
        print("File %s not found, exiting."%file_path)
        sys.exit(0)

    # Find parameter in file
    with open( file_path ) as f:
        for line in f:
            if line.startswith( parameter ):
                return line.replace(parameter + ":", "").strip()

    # Cannot find parameter, exit
    print(file_path + "  Missing parameter %s "%parameter)
    sys.exit(0)


# Load secrets from secrets file
secrets_filepath = "secrets/secrets.txt"
uc_client_id     = get_parameter("client_id",     secrets_filepath)
uc_client_secret = get_parameter("client_secret", secrets_filepath)
uc_access_token = get_parameter("access_token", secrets_filepath)
mastodon_hostname = get_parameter("mastodon_hostname", secrets_filepath)

mastodon = Mastodon(
    client_id = uc_client_id,
    client_secret = uc_client_secret,
    access_token = uc_access_token,
    api_base_url = 'https://' + mastodon_hostname,
)

#https://source.unsplash.com/collection/1053828/1920x1080
if args.period == "morning":
	collection = "1088119"
	hour_x = 835
	hour = "8:00"
	text_x = 853
	text = "Bonjour"
elif args.period == "mid-morning":
	collection = "1053828"
	hour_x = 800
	hour = "10:00"
	text_x = 890
	text = "Hello"
elif args.period == "lunch":
	collection = "962861"
	hour_x = 800
	hour = "12:00"
	text_x = 815
	text = "Bon appétit"
elif args.period == "snack":
	collection = "1162798"
	hour_x = 800
	hour = "16:00"
	text_x = 813
	text = "Goûter time"
elif args.period == "apero":
	collection = "829192"
	hour_x = 800
	hour = "18:00"
	text_x = 855
	text = "#Apéro !"
elif args.period == "diner":
	collection = "262127"
	hour_x = 800
	hour = "19:30"
	text_x = 810
	text = "Bon appétit"
elif args.period == "night":
	collection = "296884"
	hour_x = 800
	hour = "22:00"
	text_x = 815
	text = "Bonne nuit"
	
response = requests.get("https://source.unsplash.com/collection/"+collection+"/1920x1080")
pattern = Image.open(BytesIO(response.content), "r").convert('RGB')
size = width, height = pattern.size
draw = ImageDraw.Draw(pattern,'RGBA')
font = ImageFont.truetype("segoeui.ttf", 140)
draw.text((hour_x,375), hour, (255, 255, 255, 0),font=font)
font = ImageFont.truetype("segoeui.ttf", 65)
draw.text((text_x,550), text, (255, 255, 255, 0),font=font)
pattern.save('output.jpg')

if args.no_upload:
	print("don't upload this image")
else:
	media_dict = mastodon.media_post("output.jpg")
	#text.encode('utf-8').strip()
	mastodon.status_post(text, in_reply_to_id=None, media_ids=[media_dict])
