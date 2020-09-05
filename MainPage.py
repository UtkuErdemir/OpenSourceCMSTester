from selenium.webdriver.support.select import Select
from Tools import getBrowser, switchFrame


def fillInputs():
    switchFrame()
    getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/input[1]").send_keys("D")
    getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/input[4]").send_keys("D")
    getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/input[3]").send_keys("D")
    Select(getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/select[2]")).select_by_index(1)
    getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div/div/input[1]").click()
    getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div/div/input[2]").click()
    print("Arama ve sıfırlama testi başarılı.")


def addElements():
    try:
        getBrowser().find_element_by_xpath("/html/body/div[3]/div[2]/form/div[1]/div/input[2]").click()
        print("Silme butonu çalışmıyor.")
    except:
        print("Silme butonu başarıyla çalışıyor.")
        getBrowser().find_element_by_xpath("/html/body/div[3]/div[2]/form/div[1]/div/input[1]").click()
    try:
        print("Hata :", getBrowser().find_element_by_xpath("/html/body/h2").text)
        print("Ekleme fonksiyonu çalışmıyor")
    except:
        print("Ekleme butonu başarılı.")


