import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
import csv, operator
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class UpdatePatients(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        

    #unit tests  
    def test_patients(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.maximize_window()
        driver.implicitly_wait(1)
      
        lista = []
        with open('data_patients.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
           
        x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1
            else:
                nombre = linea [0]
                apellido_p = linea[1]
                apellido_m = linea [2]
                correo = linea [3]
                # telefono_cel = linea [4]
                fecha_nacimiento = linea [5]               
                sexo = linea[6]
                correo_p = linea [7]
                tipo_sangre = linea[8]
                curp = linea [9]
                calle = linea [10]
                colonia = linea [11]
                numero_inte = linea [12]
                numero_ext = linea [13]
                cp = linea [14]
                municipio = linea [15]
                localidad = linea [16]
                estado = linea [17]
                telefono_casa = linea [18]
                telefono_ofi = linea [19]
                telefono_cel = linea[20]
                entidad_nac = linea [21]
                entidad_act = linea [22]
                nivel_socioe = linea [23]
                tipo_vivienda = linea [24]
                discapacidad = linea [25]
                grupo_etni = linea [26]
                reli = linea [27]
                ocupacion = linea [28]
                tipo_domicilio = linea [29]
                numero_exp = linea [30]
                contrasenia = linea [31]

            #Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')
                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo_p)
                password.send_keys(contrasenia)
                
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button').click()
                driver.implicitly_wait(2)
                
                #share profile
                submit_botton = driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[2]').click()
                # time.sleep(2)

                #share patient
                share_patient = driver.find_element_by_xpath('/html/body/app-root/div/app-pacientes/div/div/div/div/div[2]/label/input')
                share_patient.clear()
                share_patient.send_keys(correo)

                driver.find_element_by_xpath('/html/body/app-root/div/app-pacientes/div/div/div/div/table/tbody/tr').click()

                #Update data
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/button[2]').click()

            #General
            
                # File number
                
                file_number = driver.find_element_by_xpath('//*[@id="t-pac-gral"]/input[1]')
                file_number.clear()
                file_number.send_keys(numero_exp)
            
                # Name
                name = driver.find_element_by_xpath('//*[@id="t-pac-gral"]/input[2]')
                name.clear()
                name.send_keys(nombre)

                # First name
                first_name = driver.find_element_by_xpath('//*[@id="t-pac-gral"]/input[3]')
                first_name.clear()
                first_name.send_keys(apellido_p)

                # final name 
                final_name = driver.find_element_by_xpath('//*[@id="t-pac-gral"]/input[4]')
                final_name.clear()
                final_name.send_keys(apellido_m)

                #Select sex
                select_sex = Select(driver.find_element_by_id('sexo')) 
                select_sex.select_by_visible_text(sexo)
                
                #Born
                date_born = driver.find_element_by_id('date')
                date_born.send_keys(fecha_nacimiento)

                #select type blood
                select_type_blood = Select(driver.find_element_by_id('sangrePaciente')) 
                select_type_blood.select_by_visible_text(tipo_sangre)
                
                #Curp
                idcurp = driver.find_element_by_xpath('//*[@id="t-pac-gral"]/input[6]')
                idcurp.clear()
                idcurp.send_keys(curp)

                self.assertTrue(idcurp.is_enabled()) 

            #Adrees
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ul/li[2]/a').click()              
                #Street
                street = driver.find_element_by_xpath('//*[@id="t-pac-dir"]/input[1]')
                street.clear()
                street.send_keys(calle)

                #suburb
                suburb = driver.find_element_by_xpath('//*[@id="t-pac-dir"]/input[2]')
                suburb.clear()
                suburb.send_keys(colonia)

                #interior_number
                interior_number = driver.find_element_by_xpath('//*[@id="t-pac-dir"]/input[3]')
                interior_number.clear()
                interior_number.send_keys(numero_inte)   

                #Outdoor number
                outdoor_number = driver.find_element_by_xpath('//*[@id="t-pac-dir"]/input[4]')
                outdoor_number.clear()
                outdoor_number.send_keys(numero_ext)  

                #Postal code
                postal_code = driver.find_element_by_xpath('//*[@id="t-pac-dir"]/input[5]')
                postal_code.clear()
                postal_code.send_keys(cp)
                
                #Municipality
                municipality = driver.find_element_by_xpath('//*[@id="t-pac-dir"]/input[6]')
                municipality.clear()
                municipality.send_keys(municipio)

                #location
                location = driver.find_element_by_xpath('//*[@id="t-pac-dir"]/input[7]')
                location.clear()
                location.send_keys(localidad)

                #State
                state = driver.find_element_by_xpath('//*[@id="t-pac-dir"]/select')
                state.send_keys(estado)

                self.assertTrue(street.is_enabled() 
                and suburb.is_enabled()
                and interior_number.is_enabled()
                and outdoor_number.is_enabled()
                and postal_code.is_enabled()
                and municipality.is_enabled()
                and location.is_enabled()
                and state.is_enabled())
            #Phone
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ul/li[3]/a').click()

                #Home Phone 
                home_phone = driver.find_element_by_xpath('//*[@id="t-pac-con"]/input[1]')
                home_phone.clear()
                home_phone.send_keys(telefono_casa)

                #Office phone
                office_phone = driver.find_element_by_xpath('//*[@id="t-pac-con"]/input[2]')
                office_phone.clear()
                office_phone.send_keys(telefono_ofi)

                # Cell phone    
                cell_phone = driver.find_element_by_xpath('//*[@id="t-pac-con"]/input[3]')
                cell_phone.clear()
                cell_phone.send_keys(telefono_cel)

                self.assertTrue(home_phone.is_enabled() 
                and office_phone.is_enabled()
                and cell_phone.is_enabled())

            #Extra information
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ul/li[4]/a').click()

                #Birth Entity
                select_birth_entity = driver.find_element_by_xpath('//*[@id="t-pac-otro"]/select[1]')
                select_birth_entity.send_keys(entidad_nac)

                # Current Entity
                select_current_entity = driver.find_element_by_xpath('//*[@id="t-pac-otro"]/select[2]')
                select_current_entity.send_keys(entidad_act)

                # Socioeconomic level
                socioeconomic = driver.find_element_by_xpath('//*[@id="t-pac-otro"]/input[1]')
                socioeconomic.clear()
                socioeconomic.send_keys(nivel_socioe)

                # Home Type
                home_type = driver.find_element_by_xpath('//*[@id="t-pac-otro"]/input[2]')
                home_type.clear()
                home_type.send_keys(tipo_vivienda)

                # Disability
                disability = driver.find_element_by_xpath('//*[@id="t-pac-otro"]/input[3]')
                disability.clear()
                disability.send_keys(discapacidad)

                # Ethnic group
                ethnic_group = driver.find_element_by_xpath('//*[@id="t-pac-otro"]/input[4]')
                ethnic_group.clear()
                ethnic_group.send_keys(grupo_etni)

                # Religion
                religion = driver.find_element_by_xpath('//*[@id="t-pac-otro"]/input[5]')
                religion.clear()
                religion.send_keys(reli)  

                # Occupation
                occupation = driver.find_element_by_xpath('//*[@id="t-pac-otro"]/input[6]')
                occupation.clear()
                occupation.send_keys(ocupacion)

                # home type
                home_type = driver.find_element_by_xpath('//*[@id="t-pac-otro"]/input[7]')
                home_type.clear()
                home_type.send_keys(tipo_domicilio)

                self.assertTrue(socioeconomic.is_enabled()
                and home_type.is_enabled()
                and disability.is_enabled()
                and ethnic_group.is_enabled()
                and religion.is_enabled()
                and occupation.is_enabled()
                and home_type.is_enabled())            
            # Button update     
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/button').click() 

            # Button
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/button[1]').click()

            # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()



if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Actulizar_Datos_Paciente'))  