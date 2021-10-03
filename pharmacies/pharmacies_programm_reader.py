# coding: utf-8

from datetime import datetime
import json

def get_today_pharm_programm(programm_file_path: str):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(programm_file_path, 'r') as programm:
        d = json.load(programm)
        return d[today]

# test
if __name__ == "__main__":
     print(get_today_pharm_programm(r'pharmacies_programm.json'))