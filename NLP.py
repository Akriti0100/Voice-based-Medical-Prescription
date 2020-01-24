import re
import pandas as pd
import re
import nltk
stopword = nltk.corpus.stopwords.words('english')

s = "patients name is saraj sharma  He is 25  years old and was born on 28th february 1999 he has acute bronchitis He is having symptoms which are dry cough for the last 3 days no fever and running nose he has the following medicines prescribed  azithromycin 500 mg once a day for 3 days and robitussin 5 ml thrice a day for 5 days he is advised to drink warm water and he is not allowed to eat grapes"
s = s.lower()
z = re.split(' he ',s)
data = pd.DataFrame(z)
data.columns = ['body']
def tokenize(text):
    tokens = re.split('\W+',text)
    return tokens
data['body_text_clean'] = data['body'].apply(lambda x: tokenize(x.lower()))
def remove_stopwords(list):
    text = [word for word in list if word not in stopword]
    return text
data['body_text'] = data['body_text_clean'].apply(lambda x: remove_stopwords(x))
S = ' '.join(data['body_text'][0])
Name = re.split('name',S)[1]
D = ' '.join(data['body_text'][1])
Age = re.findall('^\d\d',D)[0]
Suffer = ' '.join(data['body_text'][2])
S2 = re.split('suffering',Suffer)
if(len(S2)<2):
    S2 = re.split('has', Suffer)
b = len(S2)
S4 = S2[b-1]
Symp = ' '.join(data['body_text'][3])
Symptoms1 = re.split('symptoms',Symp)
Symptoms = Symptoms1[1]
Med1 = " ".join(data['body_text_clean'][4])
Med = re.split('medicine[s*]',Med1)[1]
Med2 = re.split(' and ',Med)
Advice = ""
for i in range(5, len(z)):
    Advice1 = ' '.join(data['body_text_clean'][i])
    Advice += " " + Advice1


print('Name: '+Name + "\n")
print('Age: '+Age + "\n")
print('Diagnosis: ' + S4 + "\n")
print('Symptoms: '+ Symptoms + "\n")
print('Medicine: ')
for i in range(0,len(Med2)):
    print(i+1)
    print(" " + Med2[i] + "\n")
print('Advice: '+Advice)
