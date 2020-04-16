import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        #inst.driver = webdriver.Firefox("C:\Users\Milica\PycharmProjects\FirstSeleniumTest\firefoxDriver\geckodriver.exe")

        inst.driver = webdriver.Chrome(
            "C:\\Users\\Milica\\PycharmProjects\\FirstSeleniumTest\\Drivers\\chromedriver.exe")
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()


    def test_search_by_name(self):
        self.driver.get("https://www.etsy.com/?ref=lgo")

        # adding product to favorites

        eleShowMsgBtn = self.driver.find_element_by_class_name(
            'wt-btn.wt-btn--small.wt-btn--transparent.wt-mr-xs-1.inline-overlay-trigger.signin-header-action.select-signin')
        eleShowMsgBtn.click()

        # get the user name box
        search_field = self.driver.find_element_by_id("join_neu_email_field")
        status = search_field.is_displayed()
        search_field.clear()
        search_field.send_keys("etsynalogzatest@gmail.com")

        search_field = self.driver.find_element_by_id('join_neu_password_field')
        status = search_field.is_displayed()
        search_field.clear()
        search_field.send_keys("etsynalog")

        checkboxBtn = self.driver.find_element_by_class_name('checkbox-label')
        checkboxBtn.click()

        eleShowMsgBtn = self.driver.find_element_by_class_name('btn.btn-large.width-full.btn-primary')
        eleShowMsgBtn.click()
        sleep(5)

        search_field = self.driver.find_element_by_id("global-enhancements-search-query")
        search_field.clear()
        search_field.send_keys("tv")

        searchboxBtn = self.driver.find_element_by_class_name('etsy-icon.wt-nudge-b-1')
        searchboxBtn.click()
        sleep(5)

        searchboxBtn = self.driver.find_element_by_class_name('favorite-listing-button-icon-container.icon-circle-container.bg-white.icon-group.p-xs-1')
        searchboxBtn.click()

        sleep(2)

        # see comments about product

        search_field = self.driver.find_element_by_id("global-enhancements-search-query")
        search_field.clear()
        search_field.send_keys("ring")

        searchboxBtn = self.driver.find_element_by_class_name('etsy-icon.wt-nudge-b-1')
        searchboxBtn.click()
        sleep(5)

        searchboxBtn = self.driver.find_element_by_class_name('width-full.wt-height-full.display-block.position-absolute')
        searchboxBtn.click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[-1])
        title = self.driver.title

        sleep(5)
        self.driver.execute_script("window.scrollTo(0,1000)")
        sleep(3)
        self.driver.execute_script("window.scrollTo(1000,0)")

        #review notifications

        notifBtn = self.driver.find_element_by_class_name("notifications-nav.has-sub-nav")
        notifBtn.click()
        sleep(5)

        notific = self.driver.find_element_by_xpath('//*[@id="sub-nav-notification-navigation"]/div/div/div[2]/a[1]/div/div[2]')
        notific.click()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # bed in special price
        search_field = self.driver.find_element_by_id("global-enhancements-search-query")
        search_field.clear()
        search_field.send_keys("bed")

        searchboxBtn = self.driver.find_element_by_class_name('etsy-icon.wt-nudge-b-1')
        searchboxBtn.click()
        sleep(5)

        searchboxBtn.select_by_visible_text('USD 25 to USD 50')
        searchboxBtn.select_by_value('25_50')
        sleep(5)

        #women jumpers

        clothindendshoes = self.driver.find_element_by_css_selector("#catnav-primary-link-10923")

        action = ActionChains(self.driver)
        action.move_to_element(clothindendshoes).perform()
        sleep(5)
        jumpers = self.driver.find_element_by_id("catnav-l4-10932")
        jumpers.click()

        sleep(6)
        self.driver.refresh()

        sleep(5)

        # scroll
        country = self.driver.find_element_by_xpath("//*[@id='ship_to_select']")
        self.driver.execute_script("arguments[0].scrollIntoView();", country)

        sleep(5)

        #dropbox
        element = self.driver.find_element_by_name('ship_to')
        element.click()
        element.send_keys("Serbia")

        sleep(4)

        clickonphoto = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/ul/li[11]/div/a/div[1]/div[1]/div[1]/div/div/div/img')
        clickonphoto.click()

        sleep(6)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        choose = self.driver.find_element_by_xpath("//*[@id='variations']/div[1]/div[1]")[0]
        choosee = self.driver.find_element_by_xpath("//*[@id='variations']/div[2]/div[1]")[0]

        if choose.is_enabled():
            choose.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER)
            sleep(3)
        elif choosee.is_enabled():
            choose.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER)
            sleep(3)
        else:
            addtobasket = self.driver.find_element_by_class_name('wt-btn.wt-btn--filled.wt-width-full')
            addtobasket.click()
            sleep(5)

        Bucketbtn = self.driver.find_element_by_class_name("etsy-icon.icon-b-4")
        Bucketbtn.click()
        sleep(5)



    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()
