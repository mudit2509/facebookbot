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

usrnm = ''
paswrd = ''

def show_exception(e) :
    print(e)
    driver.quit()
    sys.exit()

def login_fb(username,pswrd) :
    try :
        driver.find_element_by_id('email').send_keys(username)
        time.sleep(1)
        driver.find_element_by_id('pass').send_keys(pswrd)
        time.sleep(6)
        #s=input("press a key")
        driver.find_element_by_name('login').click()
        print('Logged in succesfully')
        
    except NoSuchElementException as e :
        show_exception(e)
    except Exception as e :
        show_exception(e)
    time.sleep(3)

login_fb(usrnm,paswrd)

def profile_page() :
    try : 
        btn_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]'
        account_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, btn_xpath)))
        time.sleep(5)
        account_btn.click()
        print('account btn clicked')
        me_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[1]/a'
        me_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, me_xpath)))
        time.sleep(5)
        me_btn.click()
        print('me btn clicked')
        
    except NoSuchElementException as e :
        show_exception(e)
    except Exception as e :
        show_exception(e)


friends = '100006757126835'
try :
    
    url = 'https://www.facebook.com/{}'
    driver.get(url.format(friends))
    time.sleep(5)
    print('visited profile of a friend')
        
    add_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/div'
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
    story_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]/div/a'
    story_btn = driver.find_element_by_xpath(story_xpath)
    story_btn.click()
    time.sleep(5)
    print('story btn clicked')
    
    txtstory_xpath ='/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]'
    txtstory_btn = driver.find_element_by_xpath(txtstory_xpath)
    txtstory_btn.click()
    time.sleep(5)
    print('story txt btn selected')
    
    mssg = driver.find_element_by_tag_name('textarea')
    msgvalue = 'Hii !, I Am Your Bot mudit'
    mssg.send_keys(msgvalue)
    time.sleep(5)
    print('story mssg typed')
    
    share_xpath = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/div'
    share_btn = driver.find_element_by_xpath(share_xpath)
    share_btn.click()
    time.sleep(5)
    print('story share btn clicked')
    
    driver.refresh()
    time.sleep(10)
    print('story shared')
    
    home_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]'
    home_btn = driver.find_element_by_xpath(home_xpath)
    home_btn.click()
    time.sleep(5)
    print('home btn clicked')
    

    #posting on timeline of a random friend
    print('posting on timeline of a random friend')
    profile_page()
    print('profile page opened using profile_page method')
    time.sleep(10)
    
    x = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//a[@href="https://www.facebook.com/rames.katiyar.9/friends"]')))
    x.click()
    #driver.find_element_by_xpath('//a[@href="https://www.facebook.com/rames.katiyar.9/friends"]').click()
    print('friends tab opened by xpath and href value')
    time.sleep(10)
    
    
    golu_name = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[3]/div[4]/div[1]/a'
    golu = driver.find_element_by_xpath(golu_name)
    golu.click()
    time.sleep(20)
    print('Golu selected as the third random friend')
    lpp = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div/span'
    latest_post = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lpp)))
    #driver.
    #document.querySelector("#mount_0_0_Su > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.d2edcug0.hpfvmrgz.gile2uim.buofh1pr.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5 > div:nth-child(3) > div:nth-child(3) > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div:nth-child(1) > div > div.ozuftl9m.tvfksri0 > div > div:nth-child(2) > div")
    print('latest post grabbed')
    cmnt = 'nice one!'
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
    
