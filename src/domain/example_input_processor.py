import chromedriver_binary
import datetime
from selenium import webdriver
from domain.abstract_input_processor import AbstractInputProcessor

class ExampleInputProcessor(AbstractInputProcessor):
    """
    入力プロセッサー
    """

    def __init__(self, driver: webdriver, url: str, item_id_config: str, my_setting: str):
        """
        コンストラクタ (Constructor)
        """
        super().__init__(driver, url)
        self.item_id_config = item_id_config
        self.my_setting = my_setting

    def execute(self):
        super().execute()
        super()._auto_input_choice(self.item_id_config["Choice"], self.my_setting["Choice"])
        super()._auto_input_text(self.item_id_config["Text"], self.my_setting["Text"])
        super()._auto_input_rating(self.item_id_config["Rating"], self.my_setting["Rating"])
        super()._auto_input_date(self.item_id_config["Date"], self.my_setting["Date"])
        super()._auto_input_ranking(self.item_id_config["Ranking"], self.my_setting["Ranking"])
        super()._auto_input_likert(self.item_id_config["Likert"], self.my_setting["Likert"])
        super()._auto_input_net_promoter_score(self.item_id_config["Net Promoter Score"], self.my_setting["Net Promoter Score"])
