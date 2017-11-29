# Hour bot with unsplash image
This bot use unsplash image to display it with special hour (morning, lunch, snack...) 

## How to set up
Install Pillow Mastodon.py and requests  
`pip install Pillow Mastodon.py requests`  
clone it
`git clone https://github.com/Dryusdan/random-unsplash-hour.git`  
create `secrets/secrets.txt` and paste this : 
```
client_id: looooong
client_secret: veryyyy loooong
access_token: toooo loooooong
mastodon_hostname: miaou.drycat.fr
```

## How to use it
`./random-image.py -h --help` to display help.  

```
usage: random-image.py [-h] [-p PERIOD] [--no-upload NO_UPLOAD]

optional arguments:
  -h, --help            show this help message and exit
  
  -p PERIOD, --period PERIOD La période du script [morning | mid-morning | lunch |           snack | apero | diner | night]
 
  --no-upload NO_UPLOAD Don't upload image

```
