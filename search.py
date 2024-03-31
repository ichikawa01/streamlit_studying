import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_word(word):
    # WebDriverのインスタンスを作成
    driver = webdriver.Chrome()

    try:
        # Googleのトップページを開く
        driver.get('https://www.google.com')

        # 検索ボックスを見つける
        search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')

        # 検索キーワードを入力
        search_box.send_keys(str(word))

        # Enterキーを送信して検索を実行
        search_box.send_keys(Keys.RETURN)

        # 検索結果画面が表示されるまで待機
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )
        
        # 10秒間待機してユーザーが検索結果を確認できるようにする
        time.sleep(10)
    finally:
        # ブラウザを閉じる (エラーが発生しても必ず実行)
        driver.quit()

for i in range(29, 35):
    search_word(f'oggi 気温 {i}度 服装')