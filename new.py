import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import re
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def start_browser(url, keyword):
    st.success("Journey Start Just Realx Now...")

    text_box = driver.find_element('xpath','/html/body/section[2]/div/form/div/input')
    text_to_input = url
    text_box.send_keys(text_to_input)
    st.info(f"Loaded Your URL : {url}")
    st.info('This process takes a time just realx now...')

    # Find and click the submit button.
    submit_button = driver.find_element('xpath','/html/body/section[2]/div/form/div/div/button')  # Replace with the actual ID or other locator.
    submit_button.click()
    time.sleep(2)

    text_box_2 = driver.find_element('xpath','/html/body/section[3]/div/div/div[1]/div[1]/form/div/div[1]/input')
    text_box_2.send_keys(keyword)

    list_box = driver.find_element('xpath','/html/body/section[3]/div/div/div[1]/div[1]/form/div/div[2]/select')
    select = Select(list_box)
    select.select_by_visible_text('India')
    time.sleep(2)

    submit_button_2 = driver.find_element('xpath','/html/body/section[3]/div/div/div[1]/div[1]/form/div/div[3]/button')
    submit_button_2.click()

    try:
        result_element = driver.find_element('xpath','/html/body/section[3]/div/div[1]/div[1]/div[2]/div')  # Replace with the actual ID or other locator.
        result_text = result_element.text
        time.sleep(2)
        
    except:
        result_element = driver.find_element('xpath','/html/body/section[3]/div/div[1]/div[1]/div[3]/div/p')  # Replace with the actual ID or other locator.
        result_text = result_element.text
        time.sleep(2)

    rank_match = re.search(r'#(\d+)', result_text)

    if rank_match:
        rank = "#" + rank_match.group(1)
    else:
        rank = None

    st.text(result_text)

def inserting_keywords(keywords_list):
    for i in keyword_list:
        time.sleep(2)
        text_box_2 = driver.find_element('xpath','/html/body/section[3]/div/div/div[1]/div[1]/form/div/div[1]/input')
        text_box_2.clear()  # Clear the text field
        text_box_2.send_keys(i)
        
        submit_button_2 = driver.find_element('xpath','/html/body/section[3]/div/div/div[1]/div[1]/form/div/div[3]/button')
        submit_button_2.click()
        time.sleep(2)
        
        try:
            result_element = driver.find_element('xpath','/html/body/section[3]/div/div[1]/div[1]/div[2]/div')  # Replace with the actual ID or other locator.
            result_text = result_element.text
            time.sleep(2)
            
        except:
            result_element = driver.find_element('xpath','/html/body/section[3]/div/div[1]/div[1]/div[3]/div/p')  # Replace with the actual ID or other locator.
            result_text = result_element.text
            print('this is trying run try & except command')
            time.sleep(2)
                
                
        rank_match = re.search(r'#(\d+)', result_text)

        if rank_match:
            rank = "#" + rank_match.group(1)
        else:
            rank = None

        keywords.append(rank)
        ranks.append(i)
        time.sleep(2)
        st.text(f'{rank} found in google on rank {i}')

def create_csv(keyword, ranks):
    df = pd.DataFrame(list(zip(ranks, keyword)))
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv_data, file_name="ranking.csv", key='download_csv')

# def get_driver():
#         return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


st.title("SERP SEO Ranking Checker in Bulk")
url = st.text_input("Enter Full URL:")
word = st.text_input('Enter the keyword:')
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://proseotoolkit.com/tools/google-serp')
    keywords = []
    ranks = []

    result_df = pd.DataFrame(['keywords','ranks'])

    start_browser(url,word)
    df = pd.read_csv(uploaded_file)
    keyword_list = df['keyword'].tolist()
    inserting_keywords(keyword_list)
    create_csv(keywords, ranks)

    driver.quit()
