import requests
import bs4 as bs
import pymysql
import time

link=pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="e-price")

cmd=link.cursor()


import requests

pages = 1

while True: 
    cookies = {
    '__auc': '98d0c910167ab3cc1fee2387b41',
    '_ga': 'GA1.4.222844041.1544766145',
    '__gads': 'ID=ae1f772a79be81e6:T=1544766142:S=ALNI_MYPaagAqSAUBpZZhdNQgQf7Sj5w8g',
    '__atuvc': '103%7C50%2C102%7C51%2C7%7C52',
    'PHPSESSID': 'jc7jm7f8c52qrt16e5cd71k4c7',
    '_gid': 'GA1.4.419790188.1545634106',
    '__asc': '5dbf54c2167e038f9dbc7732201',
    '__atuvs': '5c20d33d36736467001',
    '_td': '2fcf51a3-75f6-46ce-b301-6fbe94cb0546',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',}

    params = (
        ('post', 'NzVwWVRvek16cDdjem8wT2lKdFlXNTFJanR6T2pFNklqQWlPM002TnpvaWMzUmhkSFZ6TVNJN2N6b3hPaUl4SWp0ek9qYzZJbk4wWVhSMWN6SWlPM002TVRvaU1TSTdjem8yT2lKemVYTjBaVzBpTzNNNk1Eb2lJanR6T2pjNkluTjVjM1JsYlRJaU8zTTZNRG9pSWp0ek9qSTZJbTl6SWp0ek9qQTZJaUk3Y3pveE1Ub2ljMk55WldWdVgzTnBlbVVpTzNNNk1Eb2lJanR6T2pVNkluQnlhV05sSWp0ek9qQTZJaUk3Y3pveE1Ub2lZMkZ0WlhKaFgzSmxjekVpTzNNNk1Eb2lJanR6T2pFeE9pSmpZVzFsY21GZmNtVnpNaUk3Y3pvd09pSWlPM002TXpvaWJtWmpJanR6T2pBNklpSTdjem8wT2lKallYSmtJanR6T2pBNklpSTdjem94TWpvaVltRjBkR1Z5ZVY5MGVYQmxJanR6T2pBNklpSTdjem94TVRvaWJXRjRYMkpoZEhSbGNua2lPM002TURvaUlqdHpPakV3T2lKM1lYUmxjbkJ5YjI5bUlqdHpPakE2SWlJN2N6bzRPaUoyYVdSbGIxODBheUk3Y3pvd09pSWlPM002TlRvaVkyOXlaVFFpTzNNNk1Eb2lJanR6T2pVNkltTnZjbVU0SWp0ek9qQTZJaUk3Y3pveE1qb2laSFZoYkY5emNHVmhhMlZ5SWp0ek9qQTZJaUk3Y3pvMk9pSnNjbWR5WVcwaU8zTTZNRG9pSWp0ek9qTTZJbTlwY3lJN2N6b3dPaUlpTzNNNk5Ub2labWR3Y25RaU8zTTZNRG9pSWp0ek9qUTZJbmRzWTJjaU8zTTZNRG9pSWp0ek9qRXdPaUppWVc1a05HZGZZMmgwSWp0ek9qQTZJaUk3Y3pveE1Eb2lZbUZ1WkRSblgyWmxkQ0k3Y3pvd09pSWlPM002TVRBNkltSmhibVEwWjE5MGQyMGlPM002TURvaUlqdHpPakV5T2lKaVlXNWtOR2RmZEhOMFlYSWlPM002TURvaUlqdHpPakV4T2lKaVlXNWtOR2RmWVhCMFp5STdjem93T2lJaU8zTTZNVG9pYkNJN2N6b3hPaUl3SWp0ek9qRTZJbk1pTzNNNk1Ub2lOQ0k3Y3pveU9pSnpaQ0k3Y3pveE9pSXdJanR6T2pFNkluQWlPM002TVRvaU1TSTdjem94T2lKcklqdHpPakE2SWlJN2ZRPT1vNTk='),
        ('sort', '1'),
        ('l', '0'),
        ('page', pages),)

    response = requests.get('https://www.eprice.com.tw/mobile/buyerguide/', headers=headers, params=params, cookies=cookies)

    response.encoding = "UTF-8"
    soup = bs.BeautifulSoup(response.text,"html.parser")

    #要排除的連結清單(未上市的手機會放在頁面中造成爬取中斷)
    exclude_list=["#","/mobile/intro/c01-p5838-sugar-y8-max/","/mobile/intro/c01-p6001-razer-razer-phone-2/","/mobile/intro/c01-p5627-meitu-t8/"]

    for EachItem in soup.select("#search-result div.normal"): #class='prod-detail normal'
        for EachItem2 in EachItem.find_all("a",{"class":"img"}):
            con = EachItem2["href"]
            if con in exclude_list: #######list 要用in 才會一個一個尋訪 ##########  不能用 == exclude_list 會以為要一次找整個list全部的值
                continue
            # print(con) #檢查內頁的href是可以全部抓到的
            ContentResponse = requests.get("https://www.eprice.com.tw"+con)
            ContentResponse.encoding = "UTF-8"
            soup2 = bs.BeautifulSoup(ContentResponse.text,"html.parser")
            
            Name = soup2.find("span",{"itemprop":"name"}).text #商品名稱
            # OriginalPrice = soup2.find("span",{"class":"msrp"}).text #原價
            OriginalPrice = soup2.find("span",{"class":"msrp"})
            if OriginalPrice != None:
                OriginalPrice = soup2.find("span",{"class":"msrp"}).text.replace("$","").replace(",","")
            else:
                OriginalPrice = ""

            # RecentPrice = soup2.find("a",{"class":"price-1st has-price-empty"}).text#目前價格 <<<檢查type <class 'str'>可以直接.text改文字>>> 
            RecentPrice = soup2.find("a",{"class":"price-1st has-price-empty"})
            if RecentPrice != None:
                RecentPrice = soup2.find("a",{"class":"price-1st has-price-empty"}).text.replace("$","").replace(",","")
            else:
                RecentPrice = ""
            
            #上方產品特色
            up_system =        soup2.select(".speclist li")[8].text.replace("作業系統:","").replace("作業系統","").strip()          
            up_how_many_cpu =  soup2.select(".speclist li")[9].text.strip()
            up_screen =        soup2.select(".speclist li")[10].text.replace("螢　　幕:","").strip() 
            up_cpu_name =      soup2.select(".speclist li")[11].text.strip()
            # up_screen_pixel =  soup2.select(".speclist li")[12].text.replace("螢幕解析度","").replace("pixels","").strip()

            up_screen_pixel =  soup2.select(".speclist li")[12]
            if up_screen_pixel != None:
                up_screen_pixel = soup2.select(".speclist li")[12].text.replace("螢幕解析度","").replace("pixels","").strip() 
            else:
                up_screen_pixel = ""
            
            up_ram_rom =       soup2.select(".speclist li")[13].text.replace("記憶體:","").strip()
            up_main_cammera =  soup2.select(".speclist li")[14].text.replace("主要相機:主相機","").strip()
            up_front_cammera = soup2.select(".speclist li")[16].text.replace("前置相機:前相機","").strip()
            up_battry =        soup2.select(".speclist li")[15].text.replace("電　　池:","").strip()
            up_launch =        soup2.select(".last-line")[1].text.replace("上市","").strip()

            #下方規格表內容#<<<ck type <class 'list'> 需指定index值後 才能.text>>>
            size = soup2.select(".size")[0].text.strip()                 #尺寸
            weight = soup2.select(".weight")[0].text.strip()             #重量
            sim = soup2.select(".sim")[0].text.strip()                   #卡
            ipx = soup2.select(".ipx")[0].text.strip()                   #防水防塵
            screen = soup2.select(".screen")[0].text.strip()             #螢幕技術(多列)
            os = soup2.select(".os")[0].text.strip()                     #作業系統
            cpu = soup2.select(".cpu")[0].text.strip()                   #cpu
            ram = soup2.select(".ram1")[0].text.replace("RAM","").replace("GB","").strip()  #記憶體
            rom = soup2.select(".rom")[0].text.replace("(實際可用空間較此值少)","").replace("GB","").strip() #儲存空間
            dual_standby = soup2.select(".dual_standby")[0].text.strip()  #雙卡雙待
            camera = soup2.select(".camera")[0].text.strip()             #相機功能(多列)
            multimedia = soup2.select(".multimedia")[0].text.strip()     #多媒體(多列)
            network = soup2.select(".network")[0].text.strip()           #連結與網路(多列)
            sensor = soup2.select(".sensor_extra")[0].text.strip()    #感應器(多列)
            fingerprint = soup2.select(".fingerprint")[0].text.strip()   #指紋辨識
            battery = soup2.select(".battery")[0].text.strip()           #電池
            color = soup2.select(".color")[0].text.strip()               #顏色
            special = soup2.select(".special")[0].text.strip()        #其他
            #html裡面的 井字號是錨點  CSS裡面的井字是ID
            #有指定li的話才可以指定index 是多少 (".special")[0] 的寫法就是print出special底下的所有文字

            # print(Name,"*",OriginalPrice,"*",RecentPrice)
            # print(Name,OriginalPrice,RecentPrice,up_launch)

            pm={"Name":Name,
                "OriginalPrice":OriginalPrice,
                "RecentPrice":RecentPrice,
                "up_system":up_system,
                "up_how_many_cpu":up_how_many_cpu,
                "up_screen":up_screen,
                "up_cpu_name":up_cpu_name,
                "up_screen_pixel":up_screen_pixel,
                "up_ram_rom":up_ram_rom,
                "up_main_cammera":up_main_cammera,
                "up_front_cammera":up_front_cammera,
                "up_battry":up_battry,
                "up_launch":up_launch,
                "size":size,
                "weight":weight,
                "sim":sim,
                "ipx":ipx,
                "screen":screen,
                "os":os,
                "cpu":cpu,
                "ram":ram,
                "rom":rom,
                "dual_standby":dual_standby,
                "camera":camera,
                "multimedia":multimedia,
                "network":network,
                "sensor":sensor,
                "fingerprint":fingerprint,
                "battery":battery,
                "color":color,
                "special":special
                }


            ## ----商品主檔----##
            cmd.execute("INSERT INTO `e-price(product_file)`(`Name`,`OriginalPrice`,`RecentPrice`,`up_system`,`up_how_many_cpu`,`up_screen`,`up_cpu_name`,`up_screen_pixel`,`up_ram_rom`,`up_main_cammera`,`up_front_cammera`,`up_battry`,`up_launch`,`size`,`weight`,`sim`,`ipx`,`screen`,`os`,`cpu`,`ram`,`rom`,`dual_standby`,`camera`,`multimedia`,`network`,`sensor`,`fingerprint`,`battery`,`color`,`special`) VALUES(%(Name)s,%(OriginalPrice)s,%(RecentPrice)s,%(up_system)s,%(up_how_many_cpu)s,%(up_screen)s,%(up_cpu_name)s,%(up_screen_pixel)s,%(up_ram_rom)s,%(up_main_cammera)s,%(up_front_cammera)s,%(up_battry)s,%(up_launch)s,%(size)s,%(weight)s,%(sim)s,%(ipx)s,%(screen)s,%(os)s,%(cpu)s,%(ram)s,%(rom)s,%(dual_standby)s,%(camera)s,%(multimedia)s,%(network)s,%(sensor)s,%(fingerprint)s,%(battery)s,%(color)s,%(special)s)"
                ,pm)

            ##-----商品價格資訊----##
            # cmd.execute("INSERT INTO `e-price(product_price)`(`Name`,`RecentPrice`) VALUES(%(Name)s,%(RecentPrice)s)"
            #     ,pm)

            link.commit()

    pages += 1
    time.sleep(2)
    if pages == 7:
        break
link.close()
