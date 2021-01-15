import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
import csv, operator
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class ShowStudies(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        

    #unit tests  
    def test_studies(self):
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

                # show element schedule studies
                driver.find_element_by_xpath('/html/body/app-root/div/app-menu-promociones/html/body/div/div/app-navbar/div/div[1]/div[2]/nav/ul/li[2]/div/a[1]').click()
                # show input 
                show_studies = driver.find_element_by_xpath('/html/body/app-root/div/app-menu-lista/html/body/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/input')  
                show_studies.send_keys(prueba)
                self.assertTrue(show_studies.is_enabled())
                
                #show botton shedule studies
                driver.find_element_by_xpath('/html/body/app-root/div/app-menu-lista/html/body/div/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/button').click()
                
                #show botton shedule
                driver.find_element_by_xpath('/html/body/app-root/div/app-menu-lista/html/body/div/div/div/div/div/div[2]/div[2]/div/article/button[2]').click()
                driver.implicitly_wait(1)
                
                #next first
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[2]/button').click()              
                driver.implicitly_wait(1)

                #next second
                select_type_quote = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[4]/select'))

                #type quote
                select_type_quote.select_by_visible_text('Cita Agendada')

                #third next
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[4]/button[2]').click()

                #Choose a branch
                select_office = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[6]/div/select'))
                select_office.select_by_visible_text(sucursal)

                #Fourth next
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[6]/button[2]').click()

                # Select the day 
                date = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[8]/div/form/input')
                date.send_keys(fecha_prue)
                # fifth next
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[8]/div/button').click()
                
                # Select the schedule
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div/blockquote').click()
                driver.implicitly_wait(2)
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[8]/button[2]').click()

                #Add shopping cart
                driver.find_element_by_xpath('//*[@id="collapseFive"]/div[3]/button[1]').click()
                         
                #Search promotions
                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[1]').click()

                #delate studie
                driver.find_element_by_xpath('/html/body/app-root/div/app-menu-promociones/html/body/div/div/app-navbar/div/div[1]/div[2]/nav/ul/li[5]').click()
                driver.implicitly_wait(2)
                driver.find_element_by_xpath('/html/body/app-root/div/app-menu-carrito/html/body/div/div/div/div/table/tbody/tr/td[5]/button/i').click()

                #Get out
                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[9]').click()

                

                      
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Agendar_estudio'))
