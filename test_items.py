import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207//"


def test_can_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    word = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary")
    assert word, f'Отсутствует кнопка добавить в корзину'