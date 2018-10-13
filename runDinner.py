from selenium import webdriver
import os.path
import time

if __name__ == '__main__':
    currentFolder = os.path.split(os.path.realpath(__file__))[0]
    driver = webdriver.Chrome(executable_path=os.path.join(currentFolder, 'depends/chromedriver/chromedriver.exe'))
    driver.get("http://uih-office/MealSubsidies/Apply/")
    driver.implicitly_wait(10)

    driver.find_element_by_id("submit").click()
    time.sleep(3)
    driver.quit()