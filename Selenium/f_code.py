import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:/Users/52244/Downloads/chromedriver_win32/chromedriver.exe")

driver.get('http://web.whatsapp.com')

name = {"Notas", "+52 1 244 142 8451", "Notas"}
msg = "Mensajes automatizados"
count = 1

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

for i in name:
   user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(i))
   user.click()

   msg_box = driver.find_element_by_class_name('_1Plpp')

   for i in range(count):
      msg_box.send_keys(msg)
      driver.find_element_by_class_name('_35EW6').click()
   time.sleep(5)