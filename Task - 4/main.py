import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_train = pd.read_csv('twitter_training.csv', header=None, on_bad_lines='skip')
df_train.columns = ['ID', 'Topic', 'Sentiment', 'Tweet']

df_val = pd.read_csv('twitter_validation.csv', header=None, on_bad_lines='skip')
df_val.columns = ['ID', 'Topic', 'Sentiment', 'Tweet']

df = pd.concat([df_train, df_val], ignore_index=True)

df.drop_duplicates(subset=['Tweet'], keep=False, inplace=True)
df.reset_index(drop=True, inplace=True)

sentiment_counts = df['Sentiment'].value_counts()

plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
plt.title('Sentiment Distribution in Social Media Data')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.show()

topic_sentiment = df.groupby(['Topic', 'Sentiment']).size().unstack(fill_value=0)

topic_sentiment_percentage = topic_sentiment.div(topic_sentiment.sum(axis=1), axis=0)

topic_sentiment_percentage.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')
plt.title('Sentiment Proportions by Topic')
plt.xlabel('Topic')
plt.ylabel('Proportion')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Sentiment')
plt.show()