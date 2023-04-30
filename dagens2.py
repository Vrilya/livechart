from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import os

chrome_options = Options()
chrome_options.add_argument('--headless')

# Byt arbetsmapp till platsen där Git-repositoryt finns
os.chdir('/home/pi/livechart/')

# Skapa en instans av webdrivrern (i detta fall Chrome)
driver = webdriver.Chrome(options=chrome_options)

# Öppna sidan du vill ladda ner html-koden för
driver.get('https://www.nasdaqomxnordic.com/shares/listed-companies/stockholm')

# Vänta i 5 sekunder innan du hämtar html-koden och sparar den till en fil
time.sleep(5)
html = driver.page_source
with open('nasdaq.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML saved")

# Stäng webbläsaren
driver.quit()

# Pusha ändringarna till din Git-repo på GitHub
os.system('git add .')
os.system('git commit -m "Uppdaterar nasdaq.html"')
os.system('git push -u origin master')
