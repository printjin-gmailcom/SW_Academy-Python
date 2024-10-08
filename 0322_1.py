from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome()
driver.get('https://lms.sunde41.net')

wait = WebDriverWait(driver, 10, .1, [ec.visibility_of, ec.element_to_be_clickable])

from selenium import *

from selenium.webdriver.common.by import By

driver.find_elements(By.CSS_SELECTOR, '.dropdown-item')

from selenium.webdriver.common.by import By

a = driver.find_elements(By.CSS_SELECTOR, '.dropdown-item')

from selenium.webdriver.common.by import By

driver.find_elements(By.CSS_SELECTOR, 'tr.dropdown-item')[0].is_displayed()

a = driver.find_elements(By.CSS_SELECTOR, 'tr .dropdown-item')

# Selenium => Browser => Render Tree => ... =>
# sleep X, wait(Expicit => 대상의 상태를 기다려주는것, Implicit => 로드)

# driver.implicitly_wait

# wait.until(ec.visibility_of(a))

wait.until(ec.element_to_be_clickable(a))

driver.window_handles

# lms와 https://blog.naver.com/bap1234/223390929815 오픈된 상태

driver.switch_to.window(driver.window_handles[-1]) #switch_to

driver.find_element(By.CSS_SELECTOR, '#SE-972e5cb2-b0d6-4c62-a58f-cd094fe20d47')



from bs4 import BeautifulSoup

dom = BeautifulSoup(driver.page_source, 'html.parser')
dom.body # https://blog.naver.com/bap1234/223390929815 에서

frame = driver.find_element(By.CSS_SELECTOR, '#mainFrame')

driver.switch_to.frame(frame)

driver.find_element(By.CSS_SELECTOR, '#SE-972e5cb2-b0d6-4c62-a58f-cd094fe20d47')

driver.find_element(By.CSS_SELECTOR, '#SE-972e5cb2-b0d6-4c62-a58f-cd094fe20d47').text

dom = BeautifulSoup(driver.page_source, 'html.parser')
dom.body

# 같은 페이지이만 다른 돔이 뜨는 상황 발생

driver.switch_to.default_content()

driver.find_element(By.CSS_SELECTOR, '#SE-972e5cb2-b0d6-4c62-a58f-cd094fe20d47')

# 또 기존으로 돌아갔다오면 dom을 또 못 찾음

# driver.execute_script() # 이거로 자바 스크립트 사용해도 됨.

