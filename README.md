# Prettify JSON

Скрипт запрашивает строку с путём к файлу, где лежит json-строка, а затем выводит в читаемом виде.

# Quickstart

Скрипт получает на вход из терминала строку, содержащую путь к файлу. 

Пример работы скрипта на Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
# [
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            ...
     },
    "global_id": 14371450
    },
    "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
    "Number": 1
},

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
