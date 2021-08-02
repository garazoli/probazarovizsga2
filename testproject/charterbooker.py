from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
    time.sleep(3)

    # Első oldal:
    driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select').send_keys('3')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button').click()

    # Második oldal:
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/input').send_keys('2021-12-12')
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select').send_keys('Morning')
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select').send_keys('5')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button').click()

    # Harmadik oldal:
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[1]/input').send_keys('Garamvölgyi Zolika')
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[2]/input').send_keys('garazoli@gmail.com')
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[3]/textarea').send_keys('Lorem ipsum')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button').click()
    time.sleep(2)

    assert driver.find_element_by_xpath(
        '//*[@id="booking-form"]/h2').text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."

    # Invalid email:

    driver.refresh()
    time.sleep(2)

    # Oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
    time.sleep(3)

    # Első oldal:
    driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select').send_keys('3')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button').click()

    # Második oldal:
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/input').send_keys('2021-12-12')
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select').send_keys('Morning')
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select').send_keys('5')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button').click()

    # Harmadik oldal:
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[1]/input').send_keys('Garamvölgyi Zolika')
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[2]/input').send_keys(
        'garazolivgmail.com')  # Nem megfelelő email formátum.
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[3]/textarea').send_keys('Lorem ipsum')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button').click()
    time.sleep(2)

    assert driver.find_element_by_id('bf_email-error').text == 'PLEASE ENTER A VALID EMAIL ADDRESS.'

finally:
    pass
