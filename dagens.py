from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = '/usr/bin/chromium-browser'

# Skapa en instans av webdrivrern (i detta fall Chrome)
driver = webdriver.Chrome(options=chrome_options)


# Öppna sidan du vill ladda ner html-koden för
driver.get('https://www.livechart.me/timetable')

# Vänta tills popup-fönstret för tidszonen har laddats in och klicka sedan på "Yes"
try:
    time.sleep(10)
    popup_yes_button = driver.find_element_by_xpath('//button[contains(@class,"expanded") and contains(text(),"Yes")]')
    time.sleep(5) # Vänta i 5 sekunder efter att popup-fönstret har laddats in
    popup_yes_button.click()
    
    print("Button clicked")
    driver.implicitly_wait(10) # Vänta i 10 sekunder på att sidan laddas
except:
    pass

# Vänta i 5 sekunder innan du hämtar html-koden och sparar den till en fil
time.sleep(5)
html = driver.page_source
with open('/mnt/pi/livechart/livechart.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML saved")

# Stäng webbläsaren
driver.quit()
