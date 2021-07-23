import json
import os
import sys
from factory.input_processor_factory import InputProcessorFactory

def _load_config(path: str):
    """
    コンフィグファイルを読み込む
    Load config file
    """
    with open(path, 'r', encoding='utf-8') as f:
        config = json.load(f)
        return config

def load_url_config():
    """
    URLのコンフィグファイルを読み込む
    Load URL config file
    """
    return _load_config('..\\conf\\url.json')

def load_item_id_config():
    """
    項目のID設定ファイルを読み込む
    Load item id config file
    """
    return _load_config('..\\conf\\item_id.json')

def load_my_setting():
    """
    個人設定ファイルを読み込む
    Load my setting config file
    """
    return _load_config('..\\conf\\my_setting.json')

def fetch_type(argv):
    """
    引数から、タイプを取得する
    """
    if (len(argv) != 2):
        raise ValueError('Illegale Argument: Argument size should be 1.')
    return argv[1]


if __name__ == "__main__":

    setting_type = fetch_type(sys.argv)
    item_id_config = load_item_id_config()
    url_config = load_url_config()
    my_setting = load_my_setting()

    print('My setting:')
    print(json.dumps(my_setting, indent=2, ensure_ascii=False))

    proc_factory = InputProcessorFactory(url_config, item_id_config, my_setting)
    processor = proc_factory.create(setting_type)
    processor.execute()
