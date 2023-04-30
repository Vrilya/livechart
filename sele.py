from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import os

chrome_options = Options()
#chrome_options.add_argument('--headless')

# Byt arbetsmapp till platsen där Git-repositoryt finns
os.chdir('/home/pi/livechart/')

# Skapa en instans av webdrivrern (i detta fall Chrome)
driver = webdriver.Chrome(options=chrome_options)

# Gå till den länkade webbsidan
driver.get("https://www.nasdaqomxnordic.com/shares/listed-companies/stockholm")

time.sleep(15)


# Spara ner sidan på hårddisken
with open("stockholm.html", "w") as f:
    f.write(driver.page_source)

# Stäng webbläsaren
driver.quit()
