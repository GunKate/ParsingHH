import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://ekaterinburg.hh.ru/search/vacancy?L_save_area=true&text=%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA+sql&excluded_text=&area=3&salary=&currency_code=RUR&only_with_salary=true&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=vacancy_search_filter"

driver.get(url)

time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')

print (vacancies)

parsed_data = []

for vacancy in vacancies:
  try:
    title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
    company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
    salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
    link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('herf')
  except:
    print ("произошла ошибка при парсинге")
    continue
  parsed_data.append([title, company, salary, link])

driver.quit()


with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
  writer = csv.writer(file)
  writer.writerows(['Название вакансии', 'Компания', 'Зарплата', 'Ссылка'])
  writer.writerows(parsed_data)