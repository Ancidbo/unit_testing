import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
import csv, operator
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class BranchStudy(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        
    #unit tests  
    def test_schedule_branch_study(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.maximize_window()
        driver.implicitly_wait(1)
      
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
                correo = linea [3]
                contrasenia = linea [7]
                tipo_domicilio = linea [28]
                prueba = linea [29]
                fecha_prue = linea[30]
                sucursal = linea [31]

            #Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')
                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasenia)
                
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button').click()
                driver.implicitly_wait(2)
                
                # Dating history
                driver.find_element_by_xpath('/html/body/app-root/div/app-menu-promociones/html/body/div/div/app-navbar/div/div[1]/div[2]/nav/ul/li[3]').click()
                
                # Click on the table
                driver.find_element_by_xpath('/html/body/app-root/div/app-menu-estudios/html/body/div/div/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[3]/span').click()
                # driver.find_element_by_xpath('/html/body/app-root/div/app-menu-estudios/html/body/div/div/div/div[1]/div[2]/div/div/table/tbody/tr[2]/td[3]').click()
                
                # click cancel appointments
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button[2]').click()
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button[2]').click()
                
                # Cancellation request
                select_cancellation_request = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/select')
                select_cancellation_request.send_keys('Ya no requiero el estudio')               
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button[2]').click()
                
                # close the window
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button[1]').click()
                
                # Get out of the system
                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[9]').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Pago_en_sucursal'))