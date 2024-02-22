#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()



# In[1]:

# In[47]:


# 1990/06/19 13:25


# In[48]:


year="1986"
month="6"
day="10"
hr="14"
minute="30"
gender="F"


# In[49]:


driver.get("https://fatew.com/star/")


# In[50]:


#full screen
driver.maximize_window()


# In[51]:


#wait untill element is loaded 


# select = Select(driver.find_element(By.NAME, "hityear"))
# select.select_by_value(year)

# select = Select(driver.find_element(By.NAME, "hitmonth"))
# select.select_by_value(month)

# select = Select(driver.find_element(By.NAME, "hitday"))
# select.select_by_value(day)

# select = Select(driver.find_element(By.NAME, "hittime"))


# In[52]:


def select_dropdown_option(driver, name, value):
    try:
        select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, name))
        )
        dropdown = Select(select)
        dropdown.select_by_value(value)
    except Exception as e:
        print(f"Failed to select option in {name} dropdown. Error: {str(e)}")


# In[53]:


select_dropdown_option(driver, "hityear", year)
select_dropdown_option(driver, "hitmonth", month)
select_dropdown_option(driver, "hitday", day)
select_dropdown_option(driver, "hittime", hr)


# In[54]:


# select.select_by_value(hr)
# select.select_by_visible_text(hr)

if gender == "M":
    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='1']").click()
elif gender =="F":
    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='0']").click()
    # "input[type='radio'][value='0']").click()


submit=driver.find_element(By.CSS_SELECTOR, "input[type='submit'][id='submitb']")
#scroll to submit button
driver.execute_script("arguments[0].scrollIntoView();", submit)

submit.click()


# In[55]:


driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://www.dearmoney.com.tw/eightwords")


# In[56]:


# # driver.switch_to.new_window('window')
# from selenium.webdriver.common.window import WindowTypes

# driver.switch_to.new_window(WindowTypes.TAB)
# driver.get("https://www.dearmoney.com.tw/eightwords")


# In[57]:


# select = Select(driver.find_element(By.NAME, "_Year"))
# select.select_by_value(year)

# select = Select(driver.find_element(By.NAME, "_Month"))
# select.select_by_value(month)

# select = Select(driver.find_element(By.NAME, "_Day"))
# select.select_by_value(day)

# select = Select(driver.find_element(By.NAME, "_Hour"))
# select.select_by_value(hr)

select_dropdown_option(driver, "_Year", year)
select_dropdown_option(driver, "_Month", month)
select_dropdown_option(driver, "_Day", day)
select_dropdown_option(driver, "_Hour", hr)

if gender == "M":
    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='M']").click()
elif gender =="F":
    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='F']").click()
    


# In[58]:


# submit=driver.find_element(By.CSS_SELECTOR, "button[type='submit'][id='btnok']")
# driver.execute_script("arguments[0].scrollIntoView();", submit)


# In[59]:


#wait untill fully loaded
time.sleep(2)

driver.execute_script("window.scrollTo(1500, 1500);")


# In[60]:


# driver.execute_script("arguments[0].scrollIntoView();", submit)
submit=driver.find_element(By.CSS_SELECTOR, "button[type='submit'][id='btnok']")
driver.execute_script("arguments[0].scrollIntoView();", submit)
#scroll to submit button
# driver.execute_script("arguments[0].scrollIntoView();", submit)
submit.click()
#scroll to bottom of page
try:
    select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit'][id='btnok']"))
    )
    submit.click()
except Exception as e:
    print(f"Failed to click")



# In[61]:


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.window import WindowTypes

# def navigate_to_date_page(year, month, day):
#     # Format the date in YYYY-MM-DD format
#     year = int(year)
#     month = int(month)
#     day = int(day)
#     date_str = f"{year}-{month:02d}-{day:02d}"
    
#     # Initialize the webdriver and navigate to the URL
#     # driver = webdriver.Chrome()
#     driver.switch_to.new_window(WindowTypes.TAB)
#     driver.get(f"http://m-mfsm.kvov.com/fx/{date_str}/")


# In[62]:


# navigate_to_date_page(year, month, day)


# In[63]:


driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://myfate.herokuapp.com/")


# In[64]:


# driver.switch_to.new_window(WindowTypes.TAB)
# driver.get(f"https://myfate.herokuapp.com/")

# select = Select(driver.find_element(By.NAME, "Year"))
# select.select_by_value(year)

# select = Select(driver.find_element(By.NAME, "Month"))
# select.select_by_value(month)

# select = Select(driver.find_element(By.NAME, "Day"))
# select.select_by_value(day)

# select = Select(driver.find_element(By.NAME, "Hour"))
# select.select_by_value(hr)

select_dropdown_option(driver, "Year", year)
select_dropdown_option(driver, "Month", month)
select_dropdown_option(driver, "Day", day)
select_dropdown_option(driver, "Hour", hr)


#select gender
# <input class="form-check-input" type="radio" id="female" name="Sex" value="0">

if gender == "M":
    driver.find_element(By.CSS_SELECTOR,"input[type='radio'][value='1']").click()
elif gender =="F":
    driver.find_element(By.CSS_SELECTOR,"input[type='radio'][value='0']").click()
#click the button
submit=driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

#scroll to submit button
driver.execute_script("arguments[0].scrollIntoView();", submit)
submit.click()


# In[65]:


driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://mingming3.com/home/life")


# In[66]:


# #select year
# select = Select(driver.find_element(By.NAME, "o_year"))
# select.select_by_value(year)

# #select month
# select = Select(driver.find_element(By.NAME, "o_month"))
# select.select_by_value(month)

# #select day
# select = Select(driver.find_element(By.NAME, "o_day"))
# select.select_by_value(day)

# #select hour
# select = Select(driver.find_element(By.NAME, "o_hour"))
# select.select_by_value(hr)

select_dropdown_option(driver, "o_year", year)
select_dropdown_option(driver, "o_month", month)
select_dropdown_option(driver, "o_day", day)
select_dropdown_option(driver, "o_hour", hr)


# \<select class="form-control gender_select" name="gender">
#                     <option value="m">男</option>
#                     <option value="f">女</option>
#                 </select>\
                    
#select gender
select = Select(driver.find_element(By.NAME, "gender"))

if gender == "M":
    select.select_by_value("m")
elif gender =="F":
    select.select_by_value("f")

# 

                
#click the button
submit=driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

#scroll to submit button
driver.execute_script("arguments[0].scrollIntoView();", submit)
submit.click()

# <div class="content-container">雖有與人合伙的緣份，但實際合作上會比較操心，亦需要自己親力親為。更易在外常有起伏，大起大落有之。擁有膽識和自信開創的你是更容易尋找新生意事業的機會，加上自身能力好。不論工作或做生意也能處於獨當一面的位置，如做人處世成熟，在整體格局上有更大成就。</div>

# get all div with class="content-container"
divs = driver.find_elements(By.XPATH, '//div[@class="content-container"]')
for d in divs:
    print("-----------------------------------------------------------------")
    print(d.text)


# In[67]:


driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://astrodoor.cc/horoscope.jsp")


# In[68]:


def enter_text_into_element(driver, selector, text):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        element.clear()
        element.send_keys(int(text))
    except Exception as e:
        print(f"Failed to enter text into element {selector}. Error: {str(e)}")


# In[69]:


# driver.switch_to.new_window(WindowTypes.TAB)
# driver.get(f"https://astrodoor.cc/horoscope.jsp")

# #input year to the box
# driver.find_element(By.CSS_SELECTOR,"input[type='text'][name='year']").send_keys(year)

# #select month
# select = Select(driver.find_element(By.NAME, "month"))

# select.select_by_value(month)

# #select day
# select = Select(driver.find_element(By.NAME, "day"))
# select.select_by_value(day)

# #select hour
# select = Select(driver.find_element(By.NAME, "hour"))
# select.select_by_value(hr)

# #select minute
# select = Select(driver.find_element(By.NAME, "minute"))
# select.select_by_value(minute)

# #select province=1
# select = Select(driver.find_element(By.NAME, "province"))
# select.select_by_value("1")

############################################

# yearbox=driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='year']")
# yearbox.clear()
# yearbox.send_keys(int(year))


year_selector = "input[type='text'][name='year']"

enter_text_into_element(driver, year_selector, int(year))


# #select month
# select = Select(driver.find_element(By.NAME, "month"))

# select.select_by_value(month)

# #select day
# select = Select(driver.find_element(By.NAME, "day"))
# select.select_by_value(day)

# #select hour
# select = Select(driver.find_element(By.NAME, "hour"))
# select.select_by_value(hr)

# #select minute
# select = Select(driver.find_element(By.NAME, "minute"))
# select.select_by_value(minute)

# #select province=1
# select = Select(driver.find_element(By.NAME, "province"))
# select.select_by_value("1")

select_dropdown_option(driver, "month", month)
select_dropdown_option(driver, "day", day)
select_dropdown_option(driver, "hour", hr)
select_dropdown_option(driver, "minute", minute)
select_dropdown_option(driver, "province", "1")



# In[70]:


driver.execute_script("window.scrollTo(1500, 1500);")


# In[72]:


submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][id='submit2']")
if submit.is_enabled():
    print("Submit button is enabled.")
    submit.click()
else:
    print("Submit button is not enabled.")


# In[ ]:


# #click the button

# #scroll to submit button
# # driver.execute_script("arguments[0].scrollIntoView();", submit)
# #scroll to bottom of page
# driver.execute_script("window.scrollTo(0,1000);")
# submit=driver.find_element(By.CSS_SELECTOR, "input[type='submit'][id='submit1']")
# submit.click()


# In[ ]:


# <a href="/exp/sun/house2.jsp" target="_blank">解釋</a>

#find all href with the text "解釋" in <a> tag
# Find all <a> tags with the text "解釋"
# //*[@id="planetHouse"]

# table = driver.find_element(By.XPATH, '//*[@id="planetHouse"]')

# links = driver.find_elements(By.XPATH, '//a[text()="解釋"]')
# print(len(links))
# # Get the href attribute value for each matching link
# hrefs = [link.get_attribute('href') for link in links]

# hrefs


# In[ ]:





# In[ ]:





# In[73]:


# driver.switch_to.new_window(WindowTypes.TAB)
# #open new tab
# driver.get(f"https://www.dearmoney.com.tw/eightwords")

driver.get(f"https://astrodoor.cc/horoscope.jsp")

# #input year to the box
# import time

# time.sleep(3)  # Waits for 3 seconds before executing the next command
# yearbox=driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='year']")
# yearbox.clear()
# yearbox.send_keys(int(year))


year_selector = "input[type='text'][name='year']"

enter_text_into_element(driver, year_selector, int(year))


# #select month
# select = Select(driver.find_element(By.NAME, "month"))

# select.select_by_value(month)

# #select day
# select = Select(driver.find_element(By.NAME, "day"))
# select.select_by_value(day)

# #select hour
# select = Select(driver.find_element(By.NAME, "hour"))
# select.select_by_value(hr)

# #select minute
# select = Select(driver.find_element(By.NAME, "minute"))
# select.select_by_value(minute)

# #select province=1
# select = Select(driver.find_element(By.NAME, "province"))
# select.select_by_value("1")


select_dropdown_option(driver, "month", month)
select_dropdown_option(driver, "day", day)
select_dropdown_option(driver, "hour", hr)
select_dropdown_option(driver, "minute", minute)
select_dropdown_option(driver, "province", "1")



# In[ ]:




