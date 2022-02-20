from selenium import webdriver
import time

target = "고양이"
targets = ["고양이", "멍멍이", "토끼", "거북이", "고래", "여우"]
driver = webdriver.Chrome("./chromedriver")

def downImg(target):

    driver.get("https://www.google.com/")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(target)
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("/html/body/div[7]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/a").click()
    driver.implicitly_wait(3)

    imgs = driver.find_elements_by_xpath("/html/body/div/c-wiz/div/div/div/div/div/div/div/span/div/div/div/a/div/img")
    urls = []
    for img in imgs:
        print(img.get_attribute("src"))
        urls.append(img.get_attribute("src"))
        
    import os
    import urllib.request

    path = "C:/Users/jeon_minGyu/Desktop/zzam/DeepLearnningTest/image/" + target

    if not os.path.isdir(path):
        os.makedirs(path)
        
    for i, url in enumerate(urls):
        if url != None:
            urllib.request.urlretrieve(url, path + f'/{i}.jpg')




if __name__ == "__main__":
    for target in targets:
        downImg(target)

