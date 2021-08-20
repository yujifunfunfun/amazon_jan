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


def main(keyword,job,location,income,new,csv):
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

    # 職種選択
    driver.find_element_by_xpath("//*[@id='form4']/div[2]/div/div[1]").click()
    if job == '営業職':
        driver.find_element_by_xpath("//*[@id='form4']/div[2]/div/div[2]/div/div/div[2]").click()
    elif job == '企画・管理':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[3]').click()
    elif job == '事務・アシスタント':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[4]').click()
    elif job == '販売・サービス':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[5]').click()
    elif job == '専門職':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[6]').click()
    elif job == '金融系専門職':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[7]').click()
    elif job == '公務員・教員・農林水産関連職':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[8]').click()
    elif job == '技術職（SE・インフラエンジニア・Webエンジニア）':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[9]').click()
    elif job == '技術職（機械・電気）':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[10]').click()
    elif job == '技術職（組み込みソフトウェア）':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[11]').click()
    elif job == '技術職・専門職（建設・建築・不動産・プラント・工場）':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[12]').click()
    elif job == '技術職（化学・素材・化粧品・トイレタリー）':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[13]').click()
    elif job == '技術職（食品・香料・飼料）':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[14]').click()
    elif job == '医療系専門職':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[15]').click()
    elif job == 'クリエイター・クリエイティブ職':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[16]').click()

    # 都道府県選択
    driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[1]').click()
    if job == '北海道':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[2]').click()
    elif job == '青森':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[3]').click()
    elif job == '岩手':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[4]').click()
    elif job == '宮城':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[5]').click()
    elif job == '秋田':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[6]').click()
    elif job == '山形':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[7]').click()
    elif job == '福島':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[8]').click()
    elif job == '茨城':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[9]').click()
    elif job == '栃木':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[10]').click()
    elif job == '群馬':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[11]').click()
    elif job == '埼玉':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[12]').click()
    elif job == '千葉':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[13]').click()
    elif job == '東京':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[14]').click()
    elif job == '神奈川':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[15]').click()
    elif job == '新潟':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '富山':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '石川':
        driver.find_element_by_xpath('//*[@id="form4"]/div[2]/div/div[2]/div/div/div[16]').click()
    elif job == '福井':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '山梨':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '長野':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '岐阜':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '静岡':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '愛知':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '三重':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '滋賀':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '京都':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '大阪':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '兵庫':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '奈良':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '和歌山':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '鳥取':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '岡山':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '広島':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '山口':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '徳島':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '香川':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '愛媛':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '高知':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '福岡':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '佐賀':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '長崎':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '熊本':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '大分':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '宮崎':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '鹿児島':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '沖縄':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()
    elif job == '海外':
        driver.find_element_by_xpath('//*[@id="form4"]/div[3]/div/div[2]/div/div/div[16]').click()

    #年収選択
    driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[1]').click()
    if job == '200万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[2]').click()
    elif job == '250万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[3]').click()
    elif job == '300万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[4]').click()
    elif job == '350万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[5]').click()
    elif job == '400万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[6]').click()
    elif job == '450万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[7]').click()
    elif job == '500万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[8]').click()
    elif job == '550万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[9]').click()
    elif job == '600万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[10]').click()
    elif job == '700万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[10]').click()
    elif job == '800万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[10]').click()
    elif job == '900万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[10]').click()
    elif job == '1000万円～':
        driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[10]').click()
    
    # 新着のみ
    if new == 'yes':
        driver.find_element_by_id("quick_op1").click()


    # 検索ボタンクリック
    driver.find_element_by_id("quick_search").click()
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="form4"]/div[4]/div/div[2]/div/div/div[10]').click()


    
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
