from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html")
    time.sleep(3)


    with open('data.txt', 'r') as f:
        line = int(f.readline())
        periodic_list = f.readline().split('/n')


    # Sajna lejárt az időm...

finally:
    pass
