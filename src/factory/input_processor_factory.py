from selenium import webdriver
import chromedriver_binary
from domain.example_input_processor import ExampleInputProcessor

class InputProcessorFactory:
    """
    自動入力プロセッサーのファクトリー
    Factory class for automatic input processor
    """

    def __init__(self, url_config, item_id_config, my_setting):
        """
        コンストラクタ (Constructor)
        """
        self.url_config = url_config
        self.item_id_config = item_id_config
        self.my_setting = my_setting

    def create(self, setting_type: str):
        """
        設定タイプに応じて、プロセッサーを返却する
        Create automatic input processor depending on setting_type
        """
        driver = webdriver.Chrome()
        if (setting_type == 'example'):
            return ExampleInputProcessor(driver, self.url_config[setting_type], self.item_id_config[setting_type], self.my_setting[setting_type])
        else:
            raise ValueError("setting_type doesn't match")
