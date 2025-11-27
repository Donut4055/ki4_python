# bt8
import pandas as pd
import json
from pathlib import Path
from datetime import datetime

logs_dir = Path('logs')


json_files = list(logs_dir.glob('*.json'))
for file in json_files:
    print(f"   - {file}")
print()


file_dates = {}
for file in json_files:
    date_str = file.stem.replace('log_', '')
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    file_dates[file.name] = date_obj
    print(f"   {file.name} -> {date_obj.strftime('%Y-%m-%d (%A)')}")
print()

all_data = []
for file in json_files:
    with open(file, 'r') as f:
        data = json.load(f)
        date_str = file.stem.replace('log_', '')
        for record in data:
            record['date'] = date_str
        all_data.extend(data)

df = pd.DataFrame(all_data)
print(df)
print()

daily_duration = df.groupby('date')['duration'].sum().reset_index()
daily_duration.columns = ['date', 'total_duration']
print(daily_duration)
print()

output_file = 'daily_report.csv'
daily_duration.to_csv(output_file, index=False)
print()