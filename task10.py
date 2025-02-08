import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'events.json'
data = pd.read_json(file_path, encoding='utf-8')

# Parsing data in a DataFrame.
df = pd.json_normalize(data['events'])

# Distribution of events by type.
event_distribution = df['signature'].value_counts()
print(event_distribution)

# Visualization.
event_distribution_df = event_distribution.reset_index()
event_distribution_df.columns = ["signature", "count"]

plt.figure(figsize=(12, 6))
sns.barplot(data=event_distribution_df, x='signature', y='count')

plt.title('Распределение типов событий информационной безопасности', fontsize=16)
plt.xlabel('Тип события (signature)', fontsize=12)
plt.ylabel('Количество событий', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()

