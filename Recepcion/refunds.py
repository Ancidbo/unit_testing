import unittest
import csv, operator
import smtplib
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class Refunds(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_refunds(self):
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
            # Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')
                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasenia)
                
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button').click()
                driver.implicitly_wait(2)

                # button refunds
                driver.find_element_by_xpath('//*[@id="container-princ"]/app-citas/div[1]/div[1]/div[4]/button[5]').click()

                # Table refunds
                driver.find_element_by_xpath('//*[@id="lista"]/tbody/tr[1]').click()

                # close table
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[2]/button[1]').click()

                # close table refunds
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button').click()

                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Rembolsos'))
