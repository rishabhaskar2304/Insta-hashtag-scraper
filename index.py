import re,openpyxl,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pth = os.path.dirname(__file__)

usrnm = input("Enter the username of the page you want to crawl :")
number_post = int(input("Enter the number of posts from beginning you want to crawl :"))

hs = re.compile(r'#\w+')

wb = openpyxl.Workbook()
sheet = wb.active

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

driver.implicitly_wait(6)
driver.find_element_by_name('username').send_keys('YOUR_USERNAME')
driver.find_element_by_name('password').send_keys('YOUR_PASSWORD')

driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button").click()

driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div').click()

driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(usrnm)

driver.implicitly_wait(11)
driver.find_element_by_css_selector("a[href='/" + usrnm + "/']").click()


driver.implicitly_wait(6)
driver.find_element_by_css_selector("article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a").click()
cpt = []

for i in range(0,number_post):
    print(i)
    driver.implicitly_wait(13)            
    x = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span').text
    s = hs.findall(x)   
    cpt.extend(s)
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()

d = {}

for item in cpt:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
x = 1
for i in d.items():
    sheet.cell(row=x , column=1).value = i[0]
    sheet.cell(row=x , column=2).value = i[1]
    x += 1
wb.save(r"{}/hashtags.xlsx".format(pth))
