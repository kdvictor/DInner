from selenium import webdriver
from time import time, localtime, strftime
import os.path

# Modify the booking day reference the anatation
# bookingday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
bookingday = ['TUE', 'WED', 'THU', 'SAT']

def logger(msg, folder, filename):
    try:
        f = open(os.path.join(folder, filename), 'a')
        f.write(msg)
        f.write('\n')
    finally:
        if f:
            f.close()
           
if __name__ == '__main__':
    cur_folder = os.path.split(os.path.realpath(__file__))[0]
    output_folder = os.path.join(cur_folder, 'output')
    t = localtime(time())
    
    driver = webdriver.Chrome(executable_path=os.path.join(cur_folder, 'depends/chromedriver/chromedriver.exe'))
    driver.get("http://uih-office/MealSubsidies/Apply/")
    driver.implicitly_wait(10)

    driver.save_screenshot(os.path.join(output_folder, 'screem_beg.png'))
    
    meals = driver.find_elements_by_tag_name('input')
    
    weekday = strftime('%a', t)
    WEEKDAY = weekday.upper()
    if WEEKDAY in bookingday:
        if WEEKDAY == 'SAT':
            for meal in meals:
                if (meal.get_attribute('value') == '晚餐'):
                    meal.click() 
        
    driver.find_element_by_id('submit').click()
    driver.save_screenshot(os.path.join(output_folder, 'screem_end.png'))
    driver.quit()

    day = strftime('%Y/%m/%d \t%H:%M:%S \t', t)
    msg = day + 'Apply Dinner Done!'
    logger(msg, output_folder, 'logger.txt')