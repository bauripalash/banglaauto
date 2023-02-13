from logging import error
from time import sleep
import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
import random

class RkDd:
    def __init__(self) -> None:
        self.url = ""
        options = webdriver.ChromeOptions()
        
        options.add_experimental_option("debuggerAddress" , "127.0.0.1:9222")

        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
    def setup_url(self , url : str):
        self.url = url
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def dowork(self , idx  : str):
        #self.driver.
        
        self.driver.get(self.url)
        self.driver.set_window_size(1536, 935)
        elm = self.driver.find_element(By.ID , "student_code") 
        elm.click()
        for k in idx:
            elm.send_keys(k)

        submitbtn = self.driver.find_element(By.ID , "submit1")
        submitbtn.click()
        
        editelm = WebDriverWait(self.driver , 10).until(EC.presence_of_element_located((By.CLASS_NAME , 'box-title')))
        #l = editelm.get_attribute('href')
        #self.driver.get(l)

        lnks = self.driver.find_elements(By.TAG_NAME , 'a')
        for lnk in lnks:
            try:
                if lnk.get_attribute("href").endswith("add_edit_status=1"):
                    lnk.click()
            except:
                pass
        


        relitem = WebDriverWait(self.driver , 10).until(EC.presence_of_element_located((By.ID, "religion_code_fk")))
        relitem.click()
        dropdown = Select(self.driver.find_element(By.ID, "religion_code_fk"))
        dropdown.select_by_value("0")

        self.driver.find_element(By.ID, "bpl_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "bpl_y_n"))
        dropdown.select_by_value("2")

        self.driver.find_element(By.ID, "disadvantaged_group_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "disadvantaged_group_y_n"))
        dropdown.select_by_value("2")

        self.driver.find_element(By.ID, "out_of_sch_child_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "out_of_sch_child_y_n"))
        dropdown.select_by_value("2")

        self.driver.find_element(By.ID, "guardian_family_income").click()
        dropdown = Select(self.driver.find_element(By.ID, "guardian_family_income"))
        dropdown.select_by_value("1")

        self.driver.find_element(By.ID, "guardian_qualification").click()
        dropdown = Select(self.driver.find_element(By.ID, "guardian_qualification"))
        dropdown.select_by_value("2")

        self.driver.find_element(By.ID, "status_pre_year").click()
        dropdown =  Select(self.driver.find_element(By.ID, "status_pre_year"))
        dropdown.select_by_value("1")

        self.driver.find_element(By.ID, "prev_class_appeared_exam").click()
        dropdown = Select(self.driver.find_element(By.ID, "prev_class_appeared_exam"))

        dropdown.select_by_value("1")
        self.driver.find_element(By.ID, "prev_class_exam_result").click()
        dropdown = Select(self.driver.find_element(By.ID, "prev_class_exam_result"))
        dropdown.select_by_value("1")

        #self.driver.find_element(By.ID, "prev_class_marks_percent").click()
        num_marks : int = random.randint(60 , 70) 
        marks = "{}".format(int(num_marks))
        
        elms = WebDriverWait(self.driver , 1).until(EC.presence_of_element_located((By.ID , "prev_class_marks_percent"))) 
        elms.send_keys(Keys.CONTROL , "a")
        elms.send_keys(Keys.CONTROL , 'x')
        for m in marks:
            elms.send_keys(m)
            #sleep(0.3)

        #self.driver.find_element(By.ID, "attendention_pre_year").click()

        num_days : int = random.randint(85 , 92)
        days = "{}".format(num_days)
        elm = self.driver.find_element(By.ID, "attendention_pre_year")
        elm.send_keys(Keys.CONTROL , "a")
        elm.send_keys(Keys.CONTROL , 'x')
        #sleep(1.0)
        for c in days:
            elm.send_keys(c)
            #sleep(0.3)

        self.driver.find_element(By.ID, "facilities_provided_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "facilities_provided_y_n"))
        dropdown.select_by_value("1")

        self.driver.find_element(By.ID, "free_uniform_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "free_uniform_y_n"))
        dropdown.select_by_value("1")

        self.driver.find_element(By.ID, "free_transport_facility_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "free_transport_facility_y_n"))
        dropdown.select_by_value("2")

        self.driver.find_element(By.ID, "free_escort_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "free_escort_y_n"))
        dropdown.select_by_value("2")

        self.driver.find_element(By.ID, "free_hostel_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "free_hostel_y_n"))
        dropdown.select_by_value("2")

        dropdown = Select(self.driver.find_element(By.ID, "free_cycle_y_n"))
        dropdown.select_by_value("2")

        self.driver.find_element(By.ID, "free_shoe_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "free_shoe_y_n"))
        dropdown.select_by_value("1")

        self.driver.find_element(By.ID, "complete_set_of_free_books_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "complete_set_of_free_books_y_n"))
        dropdown.select_by_value("1")

        self.driver.find_element(By.ID, "free_exercise_book_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "free_exercise_book_y_n"))

        dropdown.select_by_value("2")
 
        self.driver.find_element(By.ID, "central_scholarship_rcv_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "central_scholarship_rcv_y_n"))

        dropdown.select_by_value("2")
        #WebDriverWait(self.driver , 1)
        sleep(1)


        #self.driver.find_element(By.ID, "state_scholarship_rcv_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "state_scholarship_rcv_y_n"))

        dropdown.select_by_value("2")
        sleep(1)
        try:
            elm = self.driver.find_element(By.ID , "state_scholarship_amount")
            elm.send_keys("0")
        except:
            pass

        self.driver.find_element(By.ID, "other_scholarship_rcv_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "other_scholarship_rcv_y_n"))
        dropdown.select_by_value("2")
        sleep(1)

        self.driver.find_element(
            By.ID, "screened_for_attention_deficit_hyperactive_disorder_y_n"
        ).click()
        dropdown = Select(self.driver.find_element(
            By.ID, "screened_for_attention_deficit_hyperactive_disorder_y_n"
        ))
        dropdown.select_by_value("2")
 
        self.driver.find_element(By.ID, "extracurricular_activity_involved_y_n").click()
        dropdown = Select(self.driver.find_element(
            By.ID, "extracurricular_activity_involved_y_n"
        ))
        dropdown.select_by_value("2")
 
        dropdown = Select(self.driver.find_element(
            By.NAME, "participated_in_nurturance_camps_y_n"
        ))
        dropdown.select_by_value("2")
    
        dropdown = Select(self.driver.find_element(
            By.NAME, "appeared_state_olympiads_national_level_competition_y_n"
        ))
        dropdown.select_by_value("2")

        dropdown = Select(self.driver.find_element(
            By.NAME, "participate_in_ncc_nss_scouts_guides_y_n"
        ))
        dropdown.select_by_value("2")

        self.driver.find_element(By.NAME, "free_education_as_per_rte_act_y_n").click()
        dropdown = Select(self.driver.find_element(
            By.NAME, "free_education_as_per_rte_act_y_n"
        ))
        dropdown.select_by_value("1")
 
        self.driver.find_element(By.ID, "child_homeless").click()
        dropdown = Select(self.driver.find_element(By.ID, "child_homeless"))
        dropdown.select_by_value("999")
  
        self.driver.find_element(By.ID, "special_training_facility_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "special_training_facility_y_n"))
        dropdown.select_by_value("2")
    
        self.driver.find_element(By.ID, "exposure_vocational_activities_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "exposure_vocational_activities_y_n"))
        dropdown.select_by_value("2")

        self.driver.find_element(By.ID, "undertake_vocational_course_y_n").click()
        dropdown = Select(self.driver.find_element(By.ID, "undertake_vocational_course_y_n"))
        dropdown.select_by_value("2")
        #self.driver.find_element(By.ID, "stu_contact_panchayat").click()
        mm = "MANGALDA MOUTORH"
        elm = self.driver.find_element(By.ID, "stu_contact_panchayat")
        elm.send_keys(Keys.CONTROL , "a")
        elm.send_keys(Keys.CONTROL , 'x')
        for m in mm:
            elm.send_keys(m)
            #sleep(0.3)
        mm = "MANGALDA"
        
        elm = self.driver.find_element(By.ID, "stu_contact_address")
        elm.send_keys(Keys.CONTROL , "a")
        elm.send_keys(Keys.CONTROL , 'x')
        for m in mm:
            elm.send_keys(m)

#stu_contact_address

        g_phone = self.driver.find_element(By.ID , "guardian_mobile_no")
        gpno : str = g_phone.get_attribute("value")


        stu_contact = self.driver.find_element(By.ID , "stu_mobile_no")
        stu_contact.send_keys(Keys.CONTROL , 'a')
        stu_contact.send_keys(gpno)
        same_addr = self.driver.find_element(By.ID , "address_equal")
        if not same_addr.is_selected() :
            same_addr.click()

        submitbtn = self.driver.find_element(By.NAME , "submit1")
        submitbtn.click()

        self.done(idx=idx)

    def done(self , idx : str):
        st = "Student Details Sucessfully updated."
        if st in self.driver.page_source:
            print("success -> " + idx)
        else:
            print("failed -> " + idx)
            exit()

if __name__ == "__main__":
    idlist = []
    url = "https://banglarshiksha.gov.in/Student_update_ep/student_update" 

    for idx in idlist:
        d = RkDd()
        d.setup_url(url)
        d.dowork(idx)
