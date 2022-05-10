import os
import time

import pandas as pd
#import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager import chrome

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

import warnings
warnings.filterwarnings('ignore')

#uc.TARGET_VERSION = '99'


def post_scraper(driver, wait, actions, test_post):
    all = []

    #author
    try:
        author = test_post.find_element_by_class_name("qzhwtbm6.knvmm38d").text
    except:
        author = "NOT FOUND"
    all.append(author)

    #author link posts
    try:
        author_link_posts = test_post.find_element_by_tag_name("a").get_attribute("href")
    except:
        author_link_posts = "NOT FOUND"
    all.append(author_link_posts)

    # post content
    try:
        content = test_post.find_element_by_tag_name("div[dir=auto][class]").text.replace("\n"," ")
    except:
        content = "NOT FOUND"   
    all.append(content)

    #images
    try:
        images = [v.get_attribute('src') for v in test_post.find_element_by_class_name("do00u71z.ni8dbmo4.stjgntxs.l9j0dhe7").find_elements_by_tag_name("img")]
    except:
        images = "NOT FOUND"
    all.append(images)

    # Product price if exist
    try:
        price = test_post.find_elements_by_css_selector(".ojkyduve div")[0].text.split("\n")[0]
    except:
        price = "PRICE NOT FOUND"
    all.append(price)

    # location product if it exist
    try:
        location = test_post.find_elements_by_css_selector(".ojkyduve div")[0].text.split("\n")[1].split("· ")[1]
    except:
        location = "LOCATION NOT FOUND"
    all.append(location)

    # Product title if exist
    try:
        ProductTitle = test_post.find_elements_by_css_selector(".ojkyduve div")[1].text
    except:
        ProductTitle = "TITLE NOT FOUND"
    all.append(ProductTitle)

    # Number of rections
    try:
        NumberOfReactions = test_post.find_element_by_css_selector('.ja2t1vim .pcp91wgn').text +" reaction"
    except:
        try:
            NumberOfReactions = test_post.find_element_by_class_name('bzsjyuwj.ni8dbmo4.stjgntxs.ltmttdrg.gjzvkazv').text +" reaction"
        except:
            NumberOfReactions  = "0 reaction"
    all.append(NumberOfReactions)

    #Number of comments
    try:
        Ncomments = test_post.find_element_by_class_name("bp9cbjyn.j83agx80.pfnyh3mw.p1ueia1e").find_element_by_tag_name("span").text
    except:
        Ncomments = "0 comments"
    all.append(Ncomments)

    # hover over Link/Date selectors
    elem = test_post.find_element_by_class_name("oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw")
    actions.move_to_element(elem).perform()
    time.sleep(1)
    elem = test_post.find_element_by_class_name("oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw")

    # Post link
    try:
        post_link = test_post.find_element_by_class_name("oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw").get_attribute('href')
        if(len(post_link) < 65):
            time.sleep(1)
            elem = test_post.find_elements_by_css_selector(".b1v8xokw")[2]
            actions.move_to_element(elem).perform()
            post_link = test_post.find_element_by_class_name("oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw").get_attribute('href')
            #post_link = elem.get_attribute("href")
    except:
        post_link = "NOT FOUND"
    all.append(post_link)

    return all




if __name__ == '__main__':

    print("\n\t*********************************")
    print("\n\tWelcome to the FB-group scraper !")
    print("\n\t*********************************")

    """print("\nUploading data...")
    data = pd.read_csv('data.csv')
    print("Data uploaded succefully!")"""

    print("\nReading Inputs ...")
    # The neccesary inputs
    #grp_link = {"https://www.facebook.com/groups/solcellersolenergi"
    #            "https://www.facebook.com/groups/kopochsaljistockholm",

    grp_link = str(input("\n\t--> Enter the group link you want to scrape : "))
    while("https://www.facebook.com/groups/" not in grp_link):
        print("\nInvalid link !")
        grp_link = str(input("\n\t--> Enter a valid group link you want to scrape : "))

    NpostswantedToscrape = int(input("\n\t--> Enter the number of posts you want to scrape : "))
    while(NpostswantedToscrape <= 0):
        print("\nInvalid Number!")
        NpostswantedToscrape = int(input("\n\t--> Enter a valid number of posts you want to scrape : "))

    option = webdriver.ChromeOptions() 
    #option = uc.ChromeOptions() 

    # Handling of Allow Pop Up In Facebook
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-notifications")

    """
        remove the " # " in the line 112 so it will be headless (that means the code will run and do the work whithout opening the browser)
    """
    #option.add_argument("--headless") 
    print("\nOpening the browser...")
    
    #driver = uc.Chrome(options=option)
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)

    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    print("Browser opened succefully")
    time.sleep(1)
    driver.maximize_window()

    #enter to facebook login page
    print("\nLogin to facebook ...")
    url = "https://www.facebook.com"
    time.sleep(1)
    driver.get(url)

    #connecting to the account
    time.sleep(2)
    usr = "info@macserver.se"
    pwd = "1234@Free"

    elem = driver.find_element(By.ID,"email")
    elem.send_keys(usr)

    # Enter user password
    elem = driver.find_element(By.ID,"pass")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)

    time.sleep(3)
    print("Login to Facebook succefully")

    
    driver.get(grp_link)
    time.sleep(2)

    
    posts = []
    OldlistLength = 0
    All = []


    while(len(All) < NpostswantedToscrape ):
        
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        posts = driver.find_elements_by_class_name("du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0")

        if (len(posts) <= NpostswantedToscrape):
            Newlist = posts[OldlistLength:len(posts)]
        elif(len(posts) > NpostswantedToscrape):
            Newlist = posts[OldlistLength:NpostswantedToscrape]
        
        for i in range(len(Newlist)):
            print("\nCollecting posts....")
            time.sleep(1)
            actions.move_to_element(Newlist[i]).perform()
            All.append(post_scraper(driver,wait,actions,Newlist[i]))
        
        
        OldlistLength = len(posts)
        time.sleep(2.5)
    print(f"\n {len(All)} post collected !")
    driver.close()

    # save it in an Excel file
    # Write the data in a well structured way 
    df = pd.DataFrame(All,columns = ['Author','Author link','Description','Images','Price (for products)','Location (for products)','Title (for products)','Reactions','comments','Post link'])

    print("\n Saving the Data in an Excel file\n")
    file_name = grp_link.split("groups/")[-1] + "_group.xlsx"

    # Check if the group is scraped before 
    path1 = f"{os.getcwd()}\Groups data"
    if (file_name in os.listdir(path1)):
        old_df  = pd.read_excel(f'Groups data\{file_name}')
        new_df = pd.concat([df,old_df])
        df.to_excel(f'Groups data\{file_name}')
    else:
        df.to_excel(f'Groups data\{file_name}')

    

