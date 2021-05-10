from logging import NullHandler
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
from openpyxl import load_workbook
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


class Scrape:
    def __init__(self, url):
        # Proxy Server
        try:
            self.req_proxy = RequestProxy()
            self.proxies = self.req_proxy.get_proxy_list()
            self.proxy_list = []
            for prox in self.proxies:
                if prox.country == 'Canada':
                    self.proxy_list.append(prox)
            self.proxy = self.proxy_list[0].get_address()
            
            self.proxy_run = webdriver.DesiredCapabilities.CHROME['proxy']={
                'httpProxy': self.proxy,
                'ftpProxy': self.proxy,
                'sslProxy':self.proxy,

                "proxyType":"MANUAL",


            }
        except: 
            pass
        
        #Chromedriver
        try:
            self.chrome_options = Options()
            self.chrome_options.headless = True
            self.chrome_options.add_argument("--disable-dev-shm-usage")
            self.chrome_options.add_argument("--disable-extensions")
            self.chrome_options.add_argument("--disable-gpu")
            self.chrome_options.add_argument("--no-sandbox")
            self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
            self.actions = ActionChains(self.driver)
            self.url = url
            self.gv = None
        
        except:
            pass

        try:
            self.get_info()
        
        except:
            pass
        
        #Variables
        self.url = url
        self.gv = None

    def get_info(self):
        #Get PDP
        try:
            self.driver.get(self.url)
            self.driver.set_window_size(1440, 900)
            self.gv = True
            self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
           
        except:
            self.gv = False
            pass

        finally:
            self.driver.close()
            

            
            




    
        