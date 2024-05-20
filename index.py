import json
import pandas as pd
import os

def csv_to_json():
    arquivo_csv = r'C:\Users\Rafael Bueno\Desktop\teste-robo-ame\enel_teste_222.csv'
    arquivo_json = r'C:\Users\Rafael Bueno\Desktop\teste-robo-ame\enelsp.json'
    with open(arquivo_csv, 'r', encoding='latin1') as csvfile:
        lines = csvfile.readlines()
        
        headers = [header.strip().replace('"', '') for header in lines[0].strip().split(',')]
        data = [[value.strip().replace('"', '') for value in line.strip().split(',')] for line in lines[1:]]
        
    json_data = []
    for line in data:
        json_data.append(dict(zip(headers, line)))
    
    with open(arquivo_json, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

csv_to_json()