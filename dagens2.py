from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

chrome_options = Options()
chrome_options.add_argument('--headless')

# Byt arbetsmapp till platsen där Git-repositoryt finns
os.chdir('/home/pi/livechart/')

# Skapa en instans av webdrivrern (i detta fall Chrome)
driver = webdriver.Chrome(options=chrome_options)

# Öppna sidan med länken du vill hämta information från
driver.get('https://vrilya.github.io/livechart/sida.html')

# Vänta tills länken laddas in
wait = WebDriverWait(driver, 10)
link = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/shares/listed-companies/stockholm")]')))

# Klicka på länken
link.click()

# Vänta i 5 sekunder innan du hämtar html-koden och sparar den till en fil
time.sleep(5)
html = driver.page_source
with open('nasdaq.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML saved")

# Stäng webbläsaren
driver.quit()

# Pusha ändringarna till din Git-repo på GitHub
#os.system('git add .')
#os.system('git commit -m "Uppdaterar nasdaq.html"')
#os.system('git push -u origin master')
