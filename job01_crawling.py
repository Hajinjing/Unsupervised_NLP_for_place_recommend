# crawling 작업
from selenium import webdriver
import pandas as pd
import time

option = webdriver.ChromeOptions()
#options.add_argument('headless')
option.add_argument('lang=ko_KR')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=option)
driver.implicitly_wait(1)

tour_page_url = 'https://terms.naver.com/list.naver?cid=42856&categoryId=42856&page={}'
#1page에서는 div[5], 나머지 페이지는 div[4]
#1페이지용 xpath
tour_click_xpath1 = '//*[@id="content"]/div[5]/ul/li[{}]/div[2]/div[1]/strong/a[1]'
tour_click_xpath4 = '//*[@id="content"]/div[5]/ul/li[{}]/div/div[1]/strong/a[1]'
#2페이지부터 xpath, 사진있는 경우 xpath2, 없는 경우 xpath3
tour_click_xpath2 = '//*[@id="content"]/div[4]/ul/li[{}]/div[2]/div[1]/strong/a[1]'
tour_click_xpath3 = '//*[@id="content"]/div[4]/ul/li[{}]/div/div[1]/strong/a[1]'
#여행지명
tour_title_xpath = '//*[@id="content"]/div[2]/div[1]/h2'
#여행지내용
tour_contents_xpath = '//*[@id="size_ct"]'

titles = []
contents = []

driver = webdriver.Chrome('./chromedriver', options=option)
driver.implicitly_wait(1)
# driver.get(url)
time.sleep(0.2)
#2페이지~950페이지
for i in range(2,951):
    url = tour_page_url.format(i)
    driver.get(url)
    #게시글은 한 페이지에 15게
    for j in range(1, 16):
        #에러나는 부분은 여행지링크 클릭할때, xpath2와 xpath3으로 구분
        try:
            driver.find_element_by_xpath(tour_click_xpath2.format(j)).click()
        except:
            #그래도 에러나는 경우
            try:
                driver.find_element_by_xpath(tour_click_xpath3.format(j)).click()
            except:
                break
        time.sleep(0.2)
        title = driver.find_element_by_xpath(tour_title_xpath).text
        title = title.replace(',', ' ')
        content = driver.find_element_by_xpath(tour_contents_xpath).text
        content = content.replace(',', ' ')
        titles.append(title)
        contents.append(content)
        driver.back()
    df = pd.DataFrame({'title':titles, 'contents':contents})
    df.to_csv('./crawling_data/tour.csv', index=False)
print('head:', df.head(2))
print('tail:', df.tail(2))
driver.close()
driver.quit()












