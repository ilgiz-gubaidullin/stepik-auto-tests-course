from selenium import webdriver
import time, math

    # Расчет формулы
	
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    # Забираем выражение 
	
    x_element = browser.find_element_by_css_selector(".form-group #input_value")
    x = x_element.text
    y = calc(x)
	
    #Вводим ответ в поле
	
    answer = browser.find_element_by_css_selector(".form-group #answer")
    answer.send_keys(y)
		
    #Нажимаем checkbox и radiobutton, submit
	 
    checkbox = browser.find_element_by_css_selector(".form-check-label[for='robotCheckbox']")
    checkbox.click()
	
    radiobutton = browser.find_element_by_css_selector(".form-check-label[for='robotsRule']")
    radiobutton.click()
    
    time.sleep(2)
	
    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()