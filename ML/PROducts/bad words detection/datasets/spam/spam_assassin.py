import pandas as pd

special = []
df = pd.read_csv('spam_data.csv')

for index, row in df.iterrows():
    text = row['text']

    if text is not None and text != '' and 'Subject: ' in text:
        subject = text.split("""
Subject: """)[1]
        
        if '\n' in subject:
            subject = subject.split("\n")[0].strip()
        elif '\r' in subject:
            subject = subject.split("\r")[0].strip()
        else:
            raise Exception('No newline found in subject: ' + str(text))
        content = text.split("""

""")[1:]
        content = """

""".join(content)
        
        text = subject + """

""" + content
        
        df.at[index, 'text'] = text
    else:
        special.append({'text': text, 'is_spam': row['is_spam']})

df.to_csv('spam_data_clean.csv', index=False)
pd.DataFrame(special).to_csv('special.csv', index=False)