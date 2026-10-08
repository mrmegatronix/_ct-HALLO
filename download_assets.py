import urllib.request
import os

# Create dir if not exists
os.makedirs("/run/media/zeus/6TB-1/__GITHUB NUC/_ct-HALLO/assets", exist_ok=True)

def download(url, filename):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
        out_file.write(response.read())

print("Downloading Moon...")
download("https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg", "/run/media/zeus/6TB-1/__GITHUB NUC/_ct-HALLO/assets/moon.jpg")

print("Downloading Bat GIF...")
download("https://upload.wikimedia.org/wikipedia/commons/1/15/Bat_animated.gif", "/run/media/zeus/6TB-1/__GITHUB NUC/_ct-HALLO/assets/bat.gif")

print("Done")
