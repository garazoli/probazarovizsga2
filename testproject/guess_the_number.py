from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")
    time.sleep(3)

    guess_button = driver.find_element_by_xpath('/html/body/div/div[2]/span/button')
    guess_field = driver.find_element_by_xpath('/html/body/div/div[2]/input')

    x = 1

    # Automatizált megoldó program:
    steps = []
    while True:
        guess_field.clear()
        guess_field.send_keys(x)
        guess_button.click()
        steps.append(x)
        x += 1
        message = driver.find_element_by_xpath('/html/body/div/p[5]')
        if message.text == 'Yes! That is it.':
            break

    # Találgatások számának ellenőrzése
    assert str(len(steps)) == driver.find_element_by_xpath('/html/body/div/div[3]/p/span').text

    # Intervallumon kívüli értékek:
    guess_field.clear()
    guess_field.send_keys('-19')
    guess_button.click()
    message = driver.find_element_by_xpath('/html/body/div/p[4]')
    assert message.text == 'Guess higher.'

    guess_field.clear()
    guess_field.send_keys('255')
    guess_button.click()
    message = driver.find_element_by_xpath('/html/body/div/p[3]')
    assert message.text == 'Guess lower.'

finally:
    driver.close()
