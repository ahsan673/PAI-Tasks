import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv(r'C:\Users\SANDHU PC\Desktop\PAI Lab 9(NLP)\emails.csv')

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['category'], test_size=0.2, random_state=42)

model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('nb', MultinomialNB())
])
model.fit(X_train, y_train)
joblib.dump(model, 'email_classifier.pkl')
print("✅ Model trained and saved as email_classifier.pkl")
