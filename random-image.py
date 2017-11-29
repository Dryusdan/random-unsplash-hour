#!/usr/bin/python

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
parser.add_argument("-p", "--period", help="La période du script [morning | mid-morning | lunch | snack | apero | diner ]")
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
	response = requests.get("https://source.unsplash.com/collection/1088119/1920x1080")
	pattern = Image.open(BytesIO(response.content), "r").convert('RGB')
	size = width, height = pattern.size
	draw = ImageDraw.Draw(pattern,'RGBA')
	font = ImageFont.truetype("segoeui.ttf", 140)

	draw.text((835,375), "8:00", (255, 255, 255, 0),font=font)
	font = ImageFont.truetype("segoeui.ttf", 65)
	draw.text((853,550), "Bonjour", (255, 255, 255, 0),font=font)
elif args.period == "mid-morning":
	response = requests.get("https://source.unsplash.com/collection/1053828/1920x1080")
	pattern = Image.open(BytesIO(response.content), "r").convert('RGB')
	size = width, height = pattern.size
	draw = ImageDraw.Draw(pattern,'RGBA')
	font = ImageFont.truetype("segoeui.ttf", 140)

	draw.text((800,375), "10:00", (255, 255, 255, 0),font=font)
	font = ImageFont.truetype("segoeui.ttf", 65)
	draw.text((890,550), "Hello", (255, 255, 255, 0),font=font)
elif args.period == "lunch":
	response = requests.get("https://source.unsplash.com/collection/962861/1920x1080")
	pattern = Image.open(BytesIO(response.content), "r").convert('RGB')
	size = width, height = pattern.size
	draw = ImageDraw.Draw(pattern,'RGBA')
	font = ImageFont.truetype("segoeui.ttf", 140)

	draw.text((800,375), "12:00", (255, 255, 255, 0),font=font)
	font = ImageFont.truetype("segoeui.ttf", 65)
	draw.text((815,550), "Bon appétit", (255, 255, 255, 0),font=font)
elif args.period == "snack":
	response = requests.get("https://source.unsplash.com/collection/1162798/1920x1080")
	pattern = Image.open(BytesIO(response.content), "r").convert('RGB')
	size = width, height = pattern.size
	draw = ImageDraw.Draw(pattern,'RGBA')
	font = ImageFont.truetype("segoeui.ttf", 140)

	draw.text((800,375), "16:00", (255, 255, 255, 0),font=font)
	font = ImageFont.truetype("segoeui.ttf", 65)
	draw.text((813,550), "Goûté time", (255, 255, 255, 0),font=font)
elif args.period == "apero":
	response = requests.get("https://source.unsplash.com/collection/829192/1920x1080")
	pattern = Image.open(BytesIO(response.content), "r").convert('RGB')
	size = width, height = pattern.size
	draw = ImageDraw.Draw(pattern,'RGBA')
	font = ImageFont.truetype("segoeui.ttf", 140)

	draw.text((800,375), "18:00", (255, 255, 255, 0),font=font)
	font = ImageFont.truetype("segoeui.ttf", 65)
	draw.text((855,550), "#Apéro !", (255, 255, 255, 0),font=font)
elif args.period == "diner":
	response = requests.get("https://source.unsplash.com/collection/1300619/1920x1080")
	pattern = Image.open(BytesIO(response.content), "r").convert('RGB')
	size = width, height = pattern.size
	draw = ImageDraw.Draw(pattern,'RGBA')
	font = ImageFont.truetype("segoeui.ttf", 140)

	draw.text((800,375), "19:30", (255, 255, 255, 0),font=font)
	font = ImageFont.truetype("segoeui.ttf", 65)
	draw.text((810,550), "Bon appétit", (255, 255, 255, 0),font=font)
	
pattern.save('output.jpg')

if args.no_upload:
	print("don't upload this image")
else:
	media_dict = mastodon.media_post("output.jpg")
	status = " TEST"
	status.encode('utf-8').strip()
	mastodon.status_post(status, in_reply_to_id=None, media_ids=[media_dict])
