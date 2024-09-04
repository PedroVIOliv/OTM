import json
import os

files = os.listdir('results')

for file in files:
    file_number = file.split('_')[3].split('.')[0]
    with open('results/' + file, 'r') as f:
        data = json.load(f)
        converted = []
        for i in range(len(data)):
            converted.append([data[i]['objective_value'], data[i]['time']])
        with open(f'converted_results/simplex-{file_number}.json', 'w') as f:
            json.dump(converted, f)