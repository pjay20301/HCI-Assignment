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
driver.maximize_window()
driver.set_page_load_timeout(50)

WEBSITES = ["https://nrega.nic.in/Nregahome/MGNREGA_new/Nrega_home.aspx", "https://www.usa.gov/", "https://www.bits-pilani.ac.in/","https://medium.com/","https://www.education.gov.in/en"]



table1 = pd.DataFrame(columns=['Website', 'Link', 'Link Load Time' , 'Status', 'Link is dead/timed out'])
table2 = pd.DataFrame(columns=['Website', 'Average Link Load Time' , 'Dead Links', 'Working Links', 'Total Links', 'Score'])
for homepage in WEBSITES:
    driver.get(homepage)
    time.sleep(10)
    print("Website title is ",driver.title)
    print("Website URL is ",driver.current_url)
    list_links = driver.find_elements(By.TAG_NAME , "a")
    urls = []
    
    for links in list_links:
        txt = links.get_attribute('text')
        url = links.get_attribute('href')
        if(url != None and url.startswith("http")):
            print(txt + " : " + url)
            urls.append(url)
    urls  = urls[0:5]
    total_links = len(urls)
    dead_links = 0
    active_links = 0
    web_llt = 0
    url_count = 1
    for url in urls:
        num = 1
        avg_llt = 0
        status = 0
        
        print(str(url_count)+" Navigating to : " + url)
        response = requests.head(url,verify=False)
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
            time.sleep(1)
            driver.get(homepage)
            time.sleep(1)
            num += 1

        
        
        avg_llt = avg_llt/5.0
        print("Average Link load time(5 tries) : "+str(avg_llt))
        web_llt += avg_llt
        if(status >= 400):
            dead_links += 1
            new_row1 = pd.DataFrame([{'Website':homepage, 'Link':url, 'Link Load Time':avg_llt , 'Status':status, 'Link is dead/timed out':'Y'}])
        else:
            active_links += 1
            new_row1 = pd.DataFrame([{'Website':homepage, 'Link':url, 'Link Load Time':avg_llt , 'Status':status, 'Link is dead/timed out':'N'}])

        table1 = pd.concat([table1,new_row1])
        url_count += 1    
    
    web_llt = web_llt / total_links
    new_row2 = pd.DataFrame([{'Website':homepage, 'Average Link Load Time':web_llt , 'Dead Links':dead_links,'Working Links':active_links, 'Total Links':total_links, 'Score':0}])
    table2 = pd.concat([table2,new_row2])
    

llt = table2['Average Link Load Time']
llt_min = table2['Average Link Load Time'].min()
llt_max = table2['Average Link Load Time'].max()
dead_links = table2['Dead Links']
total_links = table2['Total Links']
A = (llt - llt_min)/(llt_max - llt_min)
B = dead_links/total_links
table2['Score'] = (A+B)/2.0

table1.to_csv('Table1.csv')
table2.to_csv('Table2.csv')

driver.quit()