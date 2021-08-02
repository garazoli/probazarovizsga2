from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")
    time.sleep(2)

    # Függvény az elemek attributumainak és az elvárt, csoport szerinti attributumok összehasonlítására:


    def hero_team_finder(hero, teams):
        hero_element = driver.find_element_by_id(hero)
        assert hero_element.get_attribute('data-teams') == teams


    # Angel (aki mindegyik csoport tagja)
    hero_team_finder('angel', 'original force factor hellfire')

    # Beast (Aki original és factor)
    hero_team_finder('beast', 'original factor')

    # Cyclops
    hero_team_finder('cyclops', 'original force factor')

    # És a többi:
    hero_team_finder('emma-frost', 'hellfire')
    hero_team_finder('iceman', 'original factor')

    # És így tovább....

finally:
    driver.close()
