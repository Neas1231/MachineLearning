import pandas as pd


df = pd.read_csv('enron_spam_data.csv')

data = []
for index, row in df.iterrows():
    message = row['Message']
    subject = row['Subject']
    if not message or type(message) == float:
        message = subject
        subject = ''
    elif not subject or type(subject) == float:
        subject = message
        message = ''
    spam_ham = row['Spam/Ham']
    is_spam = 1 if spam_ham.lower() == 'spam' else 0
    text = (str(subject) + """

""" + str(message)).strip()
    data.append({'text': text, 'is_spam': is_spam})

df = pd.DataFrame(data)
df.to_csv('enron_spam_clean.csv', index=False)