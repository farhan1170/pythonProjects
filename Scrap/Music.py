from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

fw = open('/home/f/Desktop/reviewsmusic.txt', 'a')
driver = webdriver.Firefox()
driver.get(
    "https://www.youtube.com/watch?v=6-n_szx2XRE")
i = 0
while i < 1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    i += 1

#iframes=[]
#iframes = driver.find_element_by_xpath("//div[@id='watch-discussion']//div[@class='comments.embedded']")

#iframes = driver.find_element_by_css_selector("div.comments.embedded")
#for item in iframes:
#    comment=item.find_element_by_css_selector("div.comment-text-content")
#    print comment.text
try:
    i = 0
    while i < 20:

        button=driver.find_element_by_xpath(".//*[@id='yt-comments-paginator']")
        button.click()
        time.sleep(10)
        i+=1
except Exception:
    pass


element=driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[5]/div[2]/div[1]/div/div[2]/div[5]/div[4]/div[1]')
comments=[]
comments=element.find_elements_by_css_selector("div.comment-entry")
for item in comments:
    firstdiv=item.find_element_by_css_selector("div.comment-text-content")
    print firstdiv.text
    review=(firstdiv.text).encode('utf-8')
    fw.write(review)
    fw.write('\n')
    print '---------'


fw.close()






