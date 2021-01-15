import unittest
import random
# import smtplib
import csv, operator
import time
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

#unit tests
#Cases of test
class RegisterNewPatient(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_new_patient(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.implicitly_wait(10) 
        
        lista = []
        with open('datosp.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
        x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1        
            else:
                #Variables
                nombre = linea [0]
                apellido_p = linea[1]
                apellido_m = linea [2]
                correo = linea [3]
                telefono = linea [4]
                fecha= linea[5]               
                sexo = linea[6]
               
                #Share items
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[3]/div[1]/a').click()

                email = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[1]/input')
                email.send_keys(correo)

                #generate new password
                rando = random.randrange(10, 100)
                passwordd = nombre[0:2] + correo [0:3] + fecha [0:2] + telefono [0:2]
                # print(password)

                password = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[2]/input')
                password.send_keys(passwordd)

                confirm_password = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[3]/input')
                confirm_password.send_keys(passwordd)

                name=driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[4]/input')
                name.send_keys(nombre)

                first_name = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[5]/input')
                first_name.send_keys(apellido_p)  

                last_name = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[6]/input')
                last_name.send_keys(apellido_m)

                date = driver.find_element_by_id('date')
                date.send_keys(fecha)

                select_sex = Select(driver.find_element_by_id('sexo'))
                select_sex.select_by_visible_text(sexo)

                number = driver.find_element_by_name('telefono')
                number.send_keys(telefono)
                
                self.assertTrue(email.is_enabled()
                and password.is_enabled()
                and confirm_password.is_enabled()
                and confirm_password.is_enabled()
                and name.is_enabled()
                and first_name.is_enabled()
                and last_name.is_enabled())

                # Button Create Account
                create_account = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[10]/button')
                driver.implicitly_wait(5)
                # Finds an element that is not visible
                ActionChains(driver).move_to_element(create_account).click(create_account).perform()

                # Button Accept Terms
                accept_terms = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/button[2]')
                driver.implicitly_wait(5)
                # Finds an element that is not visible
                ActionChains(driver).move_to_element(accept_terms).click(accept_terms).perform()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes' ,report_name= 'registro_paciente'))