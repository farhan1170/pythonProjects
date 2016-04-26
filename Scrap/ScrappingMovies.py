from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




fw=open('/home/f/Desktop/reviewsmovies.txt','w')
driver = webdriver.Firefox()
urlList=[]


with open('/home/f/Desktop/movieurl','r') as f:
    urlList=(f.readlines())

for url in urlList:
    print url
    driver.get(url)
    i = 0
    while i < 20:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i += 1
        time.sleep(3)

    arr = []
    arr = driver.find_elements_by_css_selector("div.comment-box.level1")
    for item in arr:
        attributes= item.get_attribute("id")
        paras=[]
        paras=item.find_elements_by_css_selector("#"+attributes+" p")
        review=paras[len(paras)-1];
        print review.text
        reviewutf8=(review.text).encode('utf-8')
        fw.write(reviewutf8)
        fw.write('\n')

fw.close()



