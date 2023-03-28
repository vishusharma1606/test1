# from selenium.webdriver.common.by import By

class LoginPage():
    # locators of all the elements
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "//button[@type='submit']"
    link_profile_xpath = "//img[@src='/static/media/NewAvatar.9ac40ba1.svg']"
    link_logout_xpath = "//li[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('id', self.textbox_password_id ).clear()
        self.driver.find_element('id', self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_profile(self):
        self.driver.find_element(By.XPATH, self.link_profile_xpath).click()

    def click_profile(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

