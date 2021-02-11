import sys
import time

from selenium import webdriver
from selenium.common.exceptions import * 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

url="https://www.facebook.com/"

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
#options.add_argument('--user-data-dir=<Put your Chrome App Data dir>')
options.add_argument('--profile-directory=Default')
  
driver = webdriver.Chrome('C:\\Users\\mudit\\Desktop\python_codes\python_automation\chromedriver.exe', chrome_options=options)
driver.maximize_window()
driver.get(url)

time.sleep(2)

usrnm = 'firstlastdot.fl@gmail.com'
paswrd = 'RameshKatiyar@1234'

def show_exception(e) :
    print(e)
    driver.quit()
    sys.exit()

def login_fb(username,pswrd) :
    try :
        driver.find_element_by_id('email').send_keys(username)
        time.sleep(1)
        driver.find_element_by_id('pass').send_keys(pswrd)
        time.sleep(1)
        driver.find_element_by_id('u_0_d').click()
        print('Logged in succesfully')
    except NoSuchElementException as e :
        show_exception(e)
    except Exception as e :
        show_exception(e)
    time.sleep(7)

login_fb(usrnm,paswrd)

def profile_page() :
    try : 
        btn_xpath = '//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]'
        account_btn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, btn_xpath)))
        time.sleep(2)
        account_btn.click()
        print('account btn clicked')
        me_xpath = '//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[1]/a'
        me_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, me_xpath)))
        time.sleep(5)
        me_btn.click()
        print('me btn clicked')
        
    except NoSuchElementException as e :
        show_exception(e)
    except Exception as e :
        show_exception(e)


friends = '100008889526122'
try :

    url = 'https://www.facebook.com/{}'
    driver.get(url.format(friends))
    time.sleep(5)
    print('visited profile of mudit kumar')
        
    add_xpath = '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/div'
    add_btn = driver.find_element_by_xpath(add_xpath)
    add_btn.click()
    time.sleep(5)
    print('add friend clicked')

    driver.back()
    time.sleep(5)
    print('back1')
    driver.back()
    time.sleep(5)
    print('back2')
    
    
    #create story
    print('now creating story')
    story_xpath = '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/a'
    story_btn = driver.find_element_by_xpath(story_xpath)
    story_btn.click()
    time.sleep(5)
    print('story btn clicked')
    
    txtstory_xpath ='//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]'
    txtstory_btn = driver.find_element_by_xpath(txtstory_xpath)
    txtstory_btn.click()
    time.sleep(5)
    print('story txt btn selected')
    
    mssg = driver.find_element_by_tag_name('textarea')
    msgvalue = 'Hii !, I Am Your Bot'
    mssg.send_keys(msgvalue)
    time.sleep(5)
    print('story mssg typed')
    
    share_xpath = '//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/div'
    share_btn = driver.find_element_by_xpath(share_xpath)
    share_btn.click()
    time.sleep(5)
    print('story share btn clicked')
    
    driver.refresh()
    time.sleep(10)
    print('story shared')
    
    home_xpath = '//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a'
    home_btn = driver.find_element_by_xpath(home_xpath)
    home_btn.click()
    time.sleep(5)
    print('home btn clicked')
    

    #posting on timeline of a random friend
    print('posting on timeline of a random friend')
    profile_page()
    print('profile page opened using profile_page method')
    time.sleep(15)
    

    driver.get('https://www.facebook.com/rames.katiyar.9/friends')
    print('friends tab opened by driver')
    time.sleep(10)
    
    
    golu_name = '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[3]/div[3]/div[1]/a'
    golu = driver.find_element_by_xpath(golu_name)
    golu.click()
    time.sleep(20)
    print('Golu selected as the third random friend')
    lpp = '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div[1]/div/div/div/form/div/div/div[2]/div/div/div/div/span'
    latest_post = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,lpp)))
    cmnt = 'Hii Golu Gupta!...I am mudit\'s Bot'
    latest_post.send_keys(cmnt)
    time.sleep(5)
    print('comment entered')
    latest_post.send_keys(Keys.ENTER)
    print('ENTER pressed....sleeping for 20sec')
    time.sleep(60)
    driver.close()
    

        
except NoSuchElementException as e :
    show_exception(e)
except Exception as e :
    show_exception(e)
    