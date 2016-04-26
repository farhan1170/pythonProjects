from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
urlList=[]
'''
urlList.append("https://play.google.com/store/apps/details?id=com.king.candycrushsaga")
urlList.append("https://play.google.com/store/apps/details?id=com.nullapp.racer.moto3d")
urlList.append("https://play.google.com/store/apps/details?id=com.imangi.templerun2")
urlList.append("https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf")
urlList.append("https://play.google.com/store/apps/details?id=com.sbkgames.rallyracerdirt")
urlList.append("https://play.google.com/store/apps/details?id=com.atrilliongames.chessgame")
urlList.append("https://play.google.com/store/apps/details?id=com.fingersoft.hillclimb")
urlList.append("https://play.google.com/store/apps/details?id=com.bestgame.climb")
urlList.append("https://play.google.com/store/apps/details?id=com.icegame.fruitlink")
urlList.append("https://play.google.com/store/apps/details?id=com.tapinator.city.car.stunts3d")
urlList.append("https://play.google.com/store/apps/details?id=com.outfit7.mytalkingtomfree")
urlList.append("https://play.google.com/store/apps/details?id=com.miniclip.eightballpool")
urlList.append("https://play.google.com/store/apps/details?id=com.prettysimple.criminalcaseandroid")
urlList.append("https://play.google.com/store/apps/details?id=com.ansangha.drdriving")
urlList.append("https://play.google.com/store/apps/details?id=com.raptor.furious7")
urlList.append("https://play.google.com/store/apps/details?id=com.rovio.baba")
urlList.append("https://play.google.com/store/apps/details?id=air.au.com.metro.DumbWaysToDie2&hl=en")
urlList.append("https://play.google.com/store/apps/details?id=com.zapak.indiansoccer")
urlList.append("https://play.google.com/store/apps/details?id=air.com.games2win.starfashiondesigner")
urlList.append("https://play.google.com/store/apps/details?id=com.wickedwitch.jetrun")
urlList.append("https://play.google.com/store/apps/details?id=com.gamevil.zenoniaonline.android.google.global.normal")
urlList.append("https://play.google.com/store/apps/details?id=com.g5e.survivors")
urlList.append("https://play.google.com/store/apps/details?id=com.ea.gp.fifaworld")
urlList.append("https://play.google.com/store/apps/details?id=com.junglerunnazara.com.junglerun.nazara")
'''
urlList.append("https://play.google.com/store/apps/details?id=mindware.mindgamespro")
urlList.append("https://play.google.com/store/apps/details?id=com.notdoppler.earntodie")
urlList.append("https://play.google.com/store/apps/details?id=com.dreamsky.DiabloLOL")
urlList.append("https://play.google.com/store/apps/details?id=com.ea.games.nfs13_row")
urlList.append("https://play.google.com/store/apps/details?id=com.chillingo.incrediblejack.android.rowgplay1")
urlList.append("https://play.google.com/store/apps/details?id=com.FireproofStudios.TheRoom")
urlList.append("https://play.google.com/store/apps/details?id=com.jumpgames.RealSteel")
urlList.append("https://play.google.com/store/apps/details?id=com.playrisedigital.ttge")
urlList.append("https://play.google.com/store/apps/details?id=uk.co.yakuto.TableTennisTouch")
urlList.append("https://play.google.com/store/apps/details?id=com.ustwo.monumentvalley")
urlList.append("https://play.google.com/store/apps/details?id=com.rockstargames.gtavc")
urlList.append("https://play.google.com/store/apps/details?id=com.leosfortune")
urlList.append("https://play.google.com/store/apps/details?id=com.mojang.minecraftpe")
urlList.append("https://play.google.com/store/apps/details?id=com.halfbrick.fruitninja")
urlList.append("https://play.google.com/store/apps/details?id=com.rockstargames.gtasa")
urlList.append("https://play.google.com/store/apps/details?id=com.amtgames.ewtd2")



fgame=open('/home/f/Desktop/GameReviews.txt','a')
driver = webdriver.Firefox()
for url in urlList:
    time.sleep(10)
    driver.get(url)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    i = 0
    try:
        while i < 100:
            elements = []
            elements = driver.find_elements_by_css_selector("div.review-text")
            for item in elements:
                if len(item.text)>0:
                    print item.text
                    fgame.write(item.text)
                    fgame.write('\n')

            elements = driver.find_elements_by_css_selector("div.review-body")
            for item in elements:
                if len(item.text)>0:
                    print item.text
                    fgame.write(item.text)
                    fgame.write('\n')

            i += 1

            buttons=[]
            buttons=driver.find_elements_by_css_selector("button.expand-next")
            buttons[1].click()
            time.sleep(10)
    except Exception:
        pass
fgame.close()