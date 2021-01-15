import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
import csv, operator
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        

    #unit tests  
    def test_login(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.maximize_window()
        driver.implicitly_wait(5)
      
        lista = []
        with open('data.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
            # red lines
            # file = open('registro.csv') 
            # numline = len(file.readlines()) 
            # print (numline) 
        x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1
            else:
                correo = linea [3]
                contrasenia = linea [7]

                # Share items

                email = driver.find_element_by_id('email')
                email.send_keys(correo)
                
                password = driver.find_element_by_id('password')
                password.send_keys(contrasenia)

                self.assertTrue(email.is_enabled() 
                and password.is_enabled()) 

                submit_botton = driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button')            
    
                # driver.implicitly_wait('30')
                submit_botton.click()

                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[9]').click()
                # driver.implicitly_wait('40')  
     
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Login'))
