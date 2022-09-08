import random
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from bs4 import BeautifulSoup
import pycurl
import tldextract
import pymongo
myclient = pymongo.MongoClient("mongodb+srv://dev:goodguydev@cluster0.kv1z6.mongodb.net/?retryWrites=true&w=majority")

mydb = myclient["leads"]
mycol = mydb["allleads"]

filedoftech="real+estate"

def getRealDomainOnly(link):
    full = tldextract.extract(link)
    # print(full)
    if full.domain !="google":
        domain= full.domain+"."+full.suffix
        return domain
    else:
        return link
    

def renderURl(url):
    try:
        # print('\n url before', url)
        
        conn = pycurl.Curl()
        conn.setopt(pycurl.URL, url)
        conn.setopt(pycurl.FOLLOWLOCATION, 1)
        conn.setopt(pycurl.CUSTOMREQUEST, 'HEAD')
        conn.setopt(pycurl.NOBODY, True)
        conn.perform()
        target =conn.getinfo(pycurl.EFFECTIVE_URL)
        # print('\n url after', target)
        return target


        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('user-agent='+user_agent)
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--log-level=3')
        # # chrome_options.add_argument(configuracion['idioma'])
        # s=Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=s, options=chrome_options)
        # driver.maximize_window()

        # driver.get(url)
        # time.sleep(4)
        # target = driver.current_url
        # driver.quit()
    except Exception as e:
        print("url rendering faild ",e)
        return "faild"



allAgents= [
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
          "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"
        ]


user_agent = random.choice(allAgents)
def dump_jsonl(data, output_path, append=False):
    """
    Write list of objects to a JSON lines file.
    """
    mode = 'a+' if append else 'w'
    with open(output_path, mode, encoding='utf-8') as f:
        for line in data:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')
#     print('Wrote {} records to {}'.format(len(data), output_path)) 





def buscar_xpath( xpath):
    try:
        resultado =driver.find_element_by_xpath(xpath).text
        return resultado
    except:
        return ''

import redis

client = redis.Redis(host='localhost', port=6379, db=1)
allkeysList=[]
allkeys= client.keys()
for k in allkeys:
    allkeysList.append(k.decode("utf-8"))

for sk in allkeysList:
    # randomurl=(client.srandmember(sk)).decode("utf-8") 
    dbState=sk
    print(dbState)
    allcities = client.smembers(sk)
    for city in allcities:
        dbCity=city.decode("utf-8")
        print("   - ",dbCity)
        try:
            retryCounter=6
            loopFlag = True

            while(loopFlag):

                chrome_options = webdriver.ChromeOptions()
                # chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('user-agent='+user_agent)
                chrome_options.add_argument('--disable-dev-shm-usage')
                chrome_options.add_argument('--log-level=3')
                # chrome_options.add_argument(configuracion['idioma'])
                s=Service(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=s, options=chrome_options)
                driver.maximize_window()

                driver.get('https://www.google.com/maps/search/'+filedoftech+'+companies+in+'+dbCity+'+'+dbState)
                print(('https://www.google.com/maps/search/'+filedoftech+'+companies+in+'+dbCity+'+'+dbState))
                inputBox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchboxinput"]')))
                pyautogui.sleep(random.randint(3, 7))
                # title = driver.find_element(By.CLASS_NAME, 'NrDZNb')
                # title= title.text


                divDomains = driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')

                pyautogui.sleep(random.randint(3, 7))
                
                for i in range(0,25):
                    pyautogui.moveTo(470,1375)
                    pyautogui.click()
                    pyautogui.sleep(random.randint(3, 7))



                divDomains = driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
                from bs4 import BeautifulSoup
                # html = driver.page_source
                elementHTML = divDomains.get_attribute('outerHTML') #gives exact HTML content of the element
                soup = BeautifulSoup(elementHTML,'html.parser')
                # soup = BeautifulSoup(html)
                count=0
                allurls=[]
                for a in soup.find_all('a', href=True):
                    count+=1
                    # print(a['href'])
                    allurls.append(a['href'])
                    # if "https://www.google.com/maps/"  in str(a['href']): 

                print(count)


                driver.quit()
                time.sleep(3)
                allgoglelinks=[]
                alldomainlink=[]
                # for u in allurls:
                #     if u.startswith('/') or u.startswith('https://www.google.com/'):
                #         allgoglelinks.append(u)
                #     else:
                #         alldomainlink.append(u)
                

                # searchedDomains=[]

                # for i in allgoglelinks:
                #     try:
                #         if i.startswith('/'):

                #             # resp = renderURl("https://www.google.com"+i)
                #             resp = i
                #             # print(i)
                #             searchedDomains.append(str(resp))
                #         else:
                #             # resp = renderURl(i)
                #             resp = i
                #             searchedDomains.append(str(resp))
                #         # print(resp)
                #     except Exception as e:
                #         print("url rendeing in loop faild ",e)

                # for searchedD in searchedDomains:
                #     if searchedD.startswith("https://www.google.com/maps/place/"):
                #         pass
                #     else:
                #         searchedD=searchedD.replace('https://www.google.com/url?q=',"")
                #         # domm = getRealDomainOnly(searchedD)
                #         domm = searchedD
                #         alldomainlink.append(domm)


                # redisp = client.srem(dbState,dbCity)
                # print("redis rmover ",redisp)
                loopFlag=False

                # alldomainlinkUniq = set(alldomainlink)
                alldomainlinkUniq = set(allurls)  
                alldomainlinkUniq = list(alldomainlinkUniq)
                # print("all google dmains  ",searchedDomains)
                print(dbState,dbCity," all direct domains  ",alldomainlinkUniq)
                try:
                    leadObj = {}
                    leadObj['state']=dbState
                    leadObj['city']=dbCity
                    leadObj['websites']=alldomainlinkUniq
                    mydict =leadObj

                    x = mycol.insert_one(mydict)
                except Exception as e:
                    print("db insert faild ",e) 

                print("success! sleep a little")
                time.sleep(100)   

        except Exception as e:
            
            retryCounter=retryCounter-1
            if retryCounter==0:
                loopFlag=False



            print('Error with the Chrome Driver ',e)
            time.sleep(60)
            driver.quit()
