import unittest
import csv, operator
import smtplib
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class Cie10(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_cie10(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.implicitly_wait(10) 

        lista = []
        with open('data.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
        x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1        
            else:
                correo = linea [0]
                contrasenia = linea [1]
                cie10 = linea [2]
            # Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')
                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasenia)
                
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button').click()
                driver.implicitly_wait(2)
            
            # Fiend the button CIE10
                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[4]').click()

                # find disease
                disease = driver.find_element_by_xpath('//*[@id="search-banner"]/div/div/div/div/div/div[1]/div/input')
                disease.clear()
                disease.send_keys(cie10)

                # Button
                driver.find_element_by_xpath('//*[@id="search-banner"]/div/div/div/div/div/div[2]/button').click()

                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'CIE10'))