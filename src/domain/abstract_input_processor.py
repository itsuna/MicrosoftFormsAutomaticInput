from abc import ABCMeta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AbstractInputProcessor(metaclass=ABCMeta):
    """
    自動入力プロセッサーの基底クラス
    Abstract class for automatic input processor
    """

    def __init__(self, driver: webdriver, url: str):
        """
        コンストラクタ (Constructor)
        """
        super().__init__()
        self.url = url
        self.driver = driver

    def execute(self):
        """
        自動入力を実行する
        Execute auto input
        """
        self.driver.get(self.url)
        self.__wait_until_onload()

    def _auto_input_choice(self, id, choice):
        """
        Choice形式のフォームを自動入力する
        Input choice form automatically
        """
        self.__input_choice(id, choice)

    def _auto_input_text(self, id, text):
        """
        Text形式のフォームを自動入力する
        Input text form automatically
        """
        self.__input_textarea(id, text)

    def _auto_input_rating(self, id, rating):
        """
        Rating形式のフォームを自動入力する
        Input rating form automatically
        """
        # TODO
        print("TODO")

    def _auto_input_date(self, id, date):
        """
        Date形式のフォームを自動入力する
        Input date form automatically
        """
        self.__input_text(id, date)

    def _auto_input_ranking(self, id, ranking):
        """
        Ranking形式のフォームを自動入力する
        Input ranking form automatically
        """
        # TODO
        print("TODO")

    def _auto_input_likert(self, id, likert):
        """
        Likert形式のフォームを自動入力する
        Input likert form automatically
        """
        # TODO
        print("TODO")

    def _auto_input_net_promoter_score(self, id, net_promoter_score):
        """
        NetPromoterScore形式のフォームを自動入力する
        Input net promoter score form automatically
        """
        # TODO
        print("TODO")

    def __input_choice(self, id: str, choice: str):
        """
        ラジオボタンを自動入力する
        Select radio button automatically
        """
        answer_block = self.__query_answer_block(id)
        answer_elem = answer_block.find_element_by_css_selector("input[type='radio'][value='" + choice + "']")
        answer_elem.click()

    def __input_text(self, id: str, text: str):
        """
        テキストを自動入力する
        Input text automatically
        """
        answer_block = self.__query_answer_block(id)
        answer_elem = answer_block.find_element_by_tag_name('input')
        answer_elem.send_keys(text)

    def __input_textarea(self, id: str, text: str):
        """
        テキストエリアを自動入力する
        Input textarea automatically
        """
        answer_block = self.__query_answer_block(id)
        answer_elem = answer_block.find_element_by_tag_name('textarea')
        answer_elem.send_keys(text)

    def __wait_until_onload(self):
        """
        MicrosoftFormが読み込まれるまで、待機する
        Wait until MicrosoftForm loaded
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'form-container')))

    def __query_answer_block(self, id: str):
        """
        質問のタイトルのIDに対し、隣接するdiv要素を取得する
        Select adjacent div element from xpath of question title
        """
        xpath = '//*[@id="' + id + '"]/following-sibling::div'
        return self.driver.find_element_by_xpath(xpath)
