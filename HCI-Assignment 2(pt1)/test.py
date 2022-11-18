from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import pandas as pd
import warnings
warnings.filterwarnings('ignore') 

driver = webdriver.Edge(r"C:\Users\adars\Downloads\edgedriver_win64\msedgedriver.exe")

WEBSITES = ["https://nrega.nic.in/Nregahome/MGNREGA_new/Nrega_home.aspx" , "https://www.usa.gov/","https://www.bits-pilani.ac.in/","https://medium.com/","https://www.education.gov.in/en"]




table1 = pd.DataFrame(columns=['Website', 'Link', 'Link Load Time' , 'Status', 'Link is dead/timed out'])
table2 = pd.DataFrame(columns=['Website', 'Average Link Load Time' , 'Dead Links', 'Working Links', 'Total Links', 'Score'])
for homepage in WEBSITES:
    driver.get(homepage)
    print("Website title is ",driver.title)
    print("Website URL is ",driver.current_url)
    list_links = driver.find_elements(By.TAG_NAME , "a")
    urls = []
    
    for links in list_links:
        txt = links.get_attribute('text')
        url = links.get_attribute('href')
        if(url != None and url.startswith("http")):
            urls.append(url)
    total_links = len(urls)
    dead_links = 0
    active_links = 0
    web_llt = 0
    for url in urls:
        num = 1
        avg_llt = 0
        status = 0
        print("Navigating to : " + url)
        response = requests.get(url,verify=False)
        print("STATUS : "+str(response.status_code))
        status = response.status_code
        num = 1
        while (num<=5):
            start = time.time()
            driver.get(url) 
            end = time.time()
            d = end-start
            print("Link load time " + str(num) + " : "+str(d))
            avg_llt += d
            time.sleep(5)
            driver.back()
            time.sleep(5)
            num += 1

        
        
        avg_llt = avg_llt/5.0
        print("Average Link load time(5 tries) : "+str(avg_llt))
        web_llt += avg_llt
        if(status != 200):
            dead_links += 1
            new_row1 = pd.DataFrame([{'Website':homepage, 'Link':url, 'Link Load Time':avg_llt , 'Status':status, 'Link is dead/timed out':'Y'}])
        elif(status == 200):
            active_links += 1
            new_row1 = pd.DataFrame([{'Website':homepage, 'Link':url, 'Link Load Time':avg_llt , 'Status':status, 'Link is dead/timed out':'N'}])

        table1 = pd.concat([table1,new_row1])
        break
    
    web_llt = web_llt / total_links
    new_row2 = pd.DataFrame([{'Website':homepage, 'Average Link Load Time':web_llt , 'Dead Links':dead_links,'Working Links':active_links, 'Total Links':total_links, 'Score':0}])
    table2 = pd.concat([table2,new_row2])
    break


table1.to_csv('Table1.csv')
table2.to_csv('Table2.csv')

driver.quit()