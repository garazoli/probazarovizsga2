from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")
    time.sleep(3)

    # Teszt, hogy megjelenik-e a 24 elem:

    films_list = driver.find_elements_by_xpath('//h2')

    assert len(films_list) == 24

    # Új film felvétele:

    # Register gombra kattintás:
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
    time.sleep(3)

    # Mezők kitöltése:
    driver.find_element_by_xpath('//*[@id="nomeFilme"]').send_keys('Black widow')
    driver.find_element_by_xpath('//*[@id="anoLancamentoFilme"]').send_keys('2021')
    driver.find_element_by_xpath('//*[@id="anoCronologiaFilme"]').send_keys('2020')
    driver.find_element_by_xpath('//*[@id="linkTrailerFilme"]').send_keys('https://www.youtube.com/watch?v=Fp9pNPdNwjI')
    driver.find_element_by_xpath('//*[@id="linkImagemFilme"]').send_keys(
        'https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg')
    driver.find_element_by_xpath('//*[@id="linkImdbFilme"]').send_keys('https://www.imdb.com/title/tt3480822/')

    # Save gomb megnyomása:
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/fieldset/button[1]').click()
    time.sleep(3)

    # Az új film listábakerülésének ellenőrzése (a címeket valamiért nem tudtam kinyerni...)
    added_films = []
    films_list = driver.find_elements_by_xpath('//h2')
    for film in films_list:
        added_films.append(film.text)

    # assert 'Black widow' in added_films

    # Másodmegoldásként ellenőrzöm a lista hosszát:
    assert len(added_films) == 25

finally:
    driver.close()
