from selenium import webdriver


# Ange sökvägen till chromedriver
#chromedriver_path = "/path/to/chromedriver"

# Skapa en instans av Chrome webbläsaren med Chromedriver
driver = webdriver.Chrome()

# Gå till den länkade webbsidan
driver.get("https://www.nasdaqomxnordic.com/shares/listed-companies/stockholm")

# Spara ner sidan på hårddisken
with open("stockholm.html", "w") as f:
    f.write(driver.page_source)

# Stäng webbläsaren
driver.quit()
