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

class TestMmt():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mmt(self):
    self.driver.get("https://www.makemytrip.com/")
    self.driver.set_window_size(1846, 1053)
    element = self.driver.find_element(By.LINK_TEXT, "Trains")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Trains").click()
    element = self.driver.find_element(By.ID, "fromCity")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".activeWidget").click()
    self.driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input").send_keys("de")
    self.driver.find_element(By.CSS_SELECTOR, "#react-autowhatever-1-section-0-item-0 .searchedResult > .sr_city").click()
    self.driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input").send_keys("hy")
    self.driver.find_element(By.CSS_SELECTOR, "#react-autowhatever-1-section-0-item-0 p:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".DayPicker-Month:nth-child(1) .DayPicker-Week:nth-child(4) > .DayPicker-Day:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".travelForPopup > li:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".primaryBtn").click()
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    self.driver.find_element(By.CSS_SELECTOR, ".justify-center:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".justify-center:nth-child(3)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".justify-center:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".justify-center:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".single-train-detail:nth-child(3) .flex-column:nth-child(1) > .card").click()
    self.driver.find_element(By.CSS_SELECTOR, ".textRight").click()
    self.driver.execute_script("window.scrollTo(0,0)")
  