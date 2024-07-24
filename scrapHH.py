import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

url = "https://ekaterinburg.hh.ru/search/vacancy?L_save_area=true&text=%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA+sql&excluded_text=&area=3&salary=&currency_code=RUR&only_with_salary=true&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=vacancy_search_filter"
driver.get(url)

# Явное ожидание, чтобы дождаться загрузки элементов
wait = WebDriverWait(driver, 10)
vacancies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'vacancy-card')))

print(vacancies)

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except Exception as e:
        print("Произошла ошибка при парсинге:", e)
        continue
    parsed_data.append([title, company, salary, link])

driver.quit()

# Запись данных в CSV
with open("hhUP.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Компания', 'Зарплата', 'Ссылка'])
    writer.writerows(parsed_data)