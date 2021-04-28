from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def autorize(email, password):
    email_input = driver.find_element_by_name("email")
    email_input.clear()
    email_input.send_keys(email)
    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys(password)
    submit = driver.find_element_by_id("sign-in-button")
    submit.click()

def search(max_price, location):
    link = driver.find_element_by_link_text('Advanced search')
    link.click()
    location_input = driver.find_element_by_name("search")
    location_input.clear()
    location_input.send_keys(location)
    max_price_input = driver.find_element_by_name("max_rent")
    max_price_input.clear()
    max_price_input.send_keys(max_price)
    submit = driver.find_element_by_id("search-button")
    submit.click()
    results = driver.find_elements_by_class_name('listing-results')
    return results

def save(results):
    with open('rooms.txt', 'w') as f:
        for result in results:
            f.write(result.text)


if __name__ == '__main__':
    email = input('Введите логин: ')
    password = input('Введите пароль: ')
    max_price = '500'
    location = 'Brooklyn, Brooklyn, NY'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    site = "https://www.spareroom.com/roommate/logon.pl?loginfrom_url=%2Froommates"
    driver.get(site)
    autorize(email, password)
    results = search(max_price, location)
    save(results)
    driver.close()
