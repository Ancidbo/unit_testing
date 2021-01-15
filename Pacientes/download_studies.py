import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
import csv, operator
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class DownloadStudies(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        

    #unit tests  
    def test_download_studies(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.maximize_window()
        driver.window_handles
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
                # original_window = driver

            #Login

                email = driver.find_element_by_id ('email')
                email.send_keys(correo)

                password = driver.find_element_by_id('password')
                password.send_keys(contrasenia)
                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())
                
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button').click()
                driver.implicitly_wait(2)
            
                # Button Medical records
                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[6]/div/a[1]').click()

                # Button studies
                driver.find_element_by_xpath('/html/body/app-root/div/app-paciente-expediente/div/ul/li[3]').click()

                # Button table
                driver.find_element_by_xpath('//*[@id="listaEstudios"]/tbody/tr[1]').click()

                # table study
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/div/button[1]').click()
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/div/button[2]').click()

                #  Change the controller to the original window or tab    
                for h in driver.window_handles[1:]:
                    driver.switch_to_window(h) 
                    driver.close() 
                    driver.switch_to_window(driver.window_handles[0])
             
                # Button close table
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()

                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Descargar_estudios'))                  