from selenium import webdriver
from selenium.webdriver.common.by import By
from resizeimage import resizeimage
import requests
import io
import time
from PIL import Image

PATH = "/Users/adityaramachandran/Desktop/chromedriver"

wd = webdriver.Chrome(PATH)
#src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Sri_Maha_Mariamman_Koyil_Bangkok_%28Wat_Khaek_Silom%29_2019_03.jpg/220px-Sri_Maha_Mariamman_Koyil_Bangkok_%28Wat_Khaek_Silom%29_2019_03.jpg"
#<img src="https://c8.alamy.com/comp/FDFPG8/entrance-tower-of-the-dravidian-styled-hindu-sri-mariamman-temple-FDFPG8.jpg" jsaction="load:XAeZkd;" jsname="HiaYvf" class="n3VNCb" alt="Entrance tower of the Dravidian styled Hindu Sri Mariamman Temple,  Singapore Stock Photo - Alamy" data-noaft="1" style="width: 209.741px; height: 339px; margin: 0px;">
#<img data-ils="4" jsaction="rcuQ6b:trigger.M8vzZb;" class="rg_i Q4LuWd" jsname="Q4LuWd" alt="Tales Of A Nomad: The Most Spectacular Temple Towers in South India" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-1T-bR-N8aRD7ibQmhusT5Tph48D_iPhpOw&amp;usqp=CAU" width="138" height="207">
#<img src="https://1.bp.blogspot.com/-FdRAduOtyd0/XgbL1GzaDgI/AAAAAAABXTU/A1CltFx1-Zgvewo1MqmfgdMZl5zfzpZGwCLcBGAsYHQ/s1600/chidambaram.JPG" jsaction="load:XAeZkd;" jsname="HiaYvf" class="n3VNCb" alt="Tales Of A Nomad: The Most Spectacular Temple Towers in South India" data-noaft="1" style="width: 162.565px; height: 244px; margin: 0px;">

def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?q=City+Palace,+Jaipur&client=firefox-b-d&channel=crow5&sxsrf=APq-WBsstJptvF4qiHrLlGelLCUo7mypdw:1649647496291&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiikZXoh4v3AhVMR2wGHWBpBkAQ_AUoAnoECAIQBA&biw=1440&bih=787&dpr=2"
    wd.get(url)


    image_urls = set()
    skips = 0
    print(max_images)
    while len(image_urls) + skips < max_images:
        print(len(image_urls) + skips)
        scroll_down(wd)
        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")
        if len(image_urls) + skips >= max_images:
            break
        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue

            images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
            for image in images:
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    skips += 1
                    break

                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")

    return image_urls


def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        #image = resizeimage.resize_cover(image, [200, 100
        #image= image.resize((100, 200))
        file_path = download_path + file_name

        with open(file_path,"wb") as f:
            image.save(f,"JPEG")

        print("Done")
    except Exception as e:
        print('FAILED - ', e)

#download_image("",src, "test.jpg")
urls = get_images_from_google(wd, 1, 30)
for i,url in enumerate(urls):
    download_image("Rajput-New/", url, "CityPlace-Jaipur" + str(i) + ".jpg")

wd.quit()
