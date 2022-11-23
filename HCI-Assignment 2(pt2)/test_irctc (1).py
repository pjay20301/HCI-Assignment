# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestIrctc():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_irctc(self):
    self.driver.get("https://www.irctc.co.in/nget/train-search")
    self.driver.set_window_size(1440, 900)
    self.driver.find_element(By.LINK_TEXT, "LOGIN").click()
    self.driver.find_element(By.ID, "7095926").send_keys("Amanjham1")
    self.driver.find_element(By.ID, "7631263").send_keys("Aman@123")
    element = self.driver.find_element(By.CSS_SELECTOR, ".ui-inputgroup-addon strong")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "nlpAnswer").click()
    self.driver.find_element(By.ID, "nlpAnswer").send_keys("kh3s")
    self.driver.find_element(By.CSS_SELECTOR, "span > .search_btn").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "span > .search_btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(1) > .btn").click()
    self.driver.find_element(By.ID, "disha-banner-close").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c57-8 > .ui-inputtext").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c57-8 > .ui-inputtext").send_keys("alwar")
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c57-8 > .ui-inputtext").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c57-9 > .ui-inputtext").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c57-9 > .ui-inputtext").send_keys("sc")
    self.driver.find_element(By.CSS_SELECTOR, "#p-highlighted-option > .ng-tns-c57-9").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c58-10 > .ui-inputtext").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.LINK_TEXT, "5").click()
    self.driver.find_element(By.CSS_SELECTOR, ".train_Search").click()
    self.driver.find_element(By.CSS_SELECTOR, ".train_Search").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c57-8 > .ui-inputtext").click()
    self.driver.find_element(By.CSS_SELECTOR, "#p-highlighted-option > .ng-star-inserted").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c57-8 > .ui-inputtext").click()
    self.driver.find_element(By.CSS_SELECTOR, "#p-highlighted-option > .ng-star-inserted").click()
    self.driver.find_element(By.LINK_TEXT, "5").click()
    self.driver.find_element(By.CSS_SELECTOR, ".train_Search").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".train_Search")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Click here to login.").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c57-8 > .ui-inputtext").click()
    self.driver.find_element(By.CSS_SELECTOR, "#p-highlighted-option > .ng-star-inserted").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-next").click()
    self.driver.find_element(By.LINK_TEXT, "5").click()
    self.driver.find_element(By.CSS_SELECTOR, ".train_Search").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".train_Search")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.execute_script("window.scrollTo(0,1577)")
    self.driver.execute_script("window.scrollTo(0,1862)")
    self.driver.execute_script("window.scrollTo(0,2996)")
  