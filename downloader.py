import random
import urllib.request

def download_img(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

download_img("https://www.teslarati.com/wp-content/uploads/2018/06/tesla-model-y-render-559x294.jpg")