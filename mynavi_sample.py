import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import eel


# Chromeを起動する関数


def set_driver(driver_path, headless_flg):
    if "chrome" in driver_path:
          options = ChromeOptions()
    else:
      options = Options()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    if "chrome" in driver_path:
        return Chrome(executable_path=os.getcwd() + "/" + driver_path,options=options)
    else:
        return Firefox(executable_path=os.getcwd()  + "/" + driver_path,options=options)

# main処理


def main(keyword,csv):
    search_keyword = keyword
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    # Webサイトを開く
    driver.get("https://doda.jp/")
    time.sleep(5)

    # 検索窓に入力
    driver.find_element_by_id("k").send_keys(search_keyword)

    driver.find_element_by_xpath("//*[@id='form4']/div[2]/div/div[1]").click()

    
    driver.find_element_by_xpath("//*[@id='form4']/div[3]/div/div[1]").click()
    
    # 検索ボタンクリック
    driver.find_element_by_id("quick_search").click()
    time.sleep(3)
    # 商品URL
    url = driver.find_element_by_class_name("a-text-normal").get_attribute('href')
    # 商品名クリック
    time.sleep(3)
    driver.find_element_by_class_name("a-size-base-plus").click()
    
    time.sleep(10)
    # name = driver.find_element_by_id("title")
    price = driver.find_element_by_class_name("a-color-price")
    img = driver.find_element_by_id("landingImage").get_attribute('href')
    description =driver.find_element_by_class_name("a-unordered-list")
    category = driver.find_element_by_class_name("amabot_widget")
    ship_from = driver.find_element_by_class_name("tabular-buybox-text")

    # 空のDataFrame作成
    df = pd.DataFrame()
    df = df.append(
        {"商品名": name.text, 
         "金額": price.text,
         "画像": img,
         "URL": url,
         "説明": description.text, 
         "カテゴリ": category.text, 
         "販売元": ship_from.text}, 

        ignore_index=True)
    
    df.to_csv(csv,encoding="utf_8-sig")
    


        
# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
