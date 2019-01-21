import bs4 as bs
import requests
import time
import pymysql


link=pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="e-price")

cmd=link.cursor()

pages = 1

while True: 
    #改快速搜尋的所有手機
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
    linkk = soup.find("div",{"id":"search-result"})

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

    # for EachItem in link.find_all("div",{"class":"prod-detail normal"}):
    #     # if str(EachItem["class"]).find("icon-2016-best icon-2016-best-0") ==-1:
    #     # if EachItem.find("a",{"class":"img"}) !=None:
    #     if str(EachItem["class"]).find("href") != None :
    #         for EachItem2 in EachItem.find_all("a",{"class":"img"}):
    #             # print(EachItem2["href"]) #檢查內頁的href是可以全部抓到的

    #             ContentResponse = requests.get("https://www.eprice.com.tw"+EachItem2["href"])
    #             ContentResponse.encoding = "UTF-8"
    #             soup2 = bs.BeautifulSoup(ContentResponse.text,"html.parser")
                
            #從商品集合頁面取出所有手機的ID編號 
            dataID = soup2.find("div",{"class":"gallery"})["data-id"] #<div class="gallery" data-id="5559"></div>
            # print(dataID)

            #商品名稱
            Name = soup2.find("span",{"itemprop":"name"}).text 
                
            source = requests.post('https://www.eprice.com.tw/ajax/intro/price.history.get.php',
                                   data={'lib': 'mobile', 'prod_id': dataID, 'd': '0'}).text
            source = source.replace('<![CDATA[', '').replace(']]>', '')
            soup = bs.BeautifulSoup(source, 'lxml')

            # minDate = soup.find('minx').text
            # maxDate = soup.find('maxx').text
            # minPrice = soup.find('miny').text
            # maxPrice = soup.find('maxy').text
            title = soup.find('title').text

            # NAME+歷史價格走勢
            # print(title)
            # print('{0}\t{1}'.format(minDate, maxDate))
            # print('{0}\t{1}'.format(minPrice, maxPrice))

            for data in soup.find_all('data'):
                date = data.find("date").text
                price = data.find("price").text
                ##print 在同一行的寫法 如下
                # print("{0}\t{1}\t{2}".format(Name,date, price))

                pm={"product_name":Name,
                    "price":price,
                    "price_date":date
                    }

                # print(pm)
                #-----商品價格資訊----##
                cmd.execute("INSERT INTO `e-price(history_price)`(`product_name`,`price`,`price_date`) VALUES(%(product_name)s,%(price)s,%(price_date)s)"
                    ,pm)

                link.commit()
                ##TypeError: 'NoneType' object is not callable  (link名稱去衝到)
    pages += 1
    time.sleep(random.randint(0,3))
    if pages == 7:
        break
        
link.close()