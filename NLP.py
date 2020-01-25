    import re
    import pandas as pd
    import re
    import nltk
    stopword = nltk.corpus.stopwords.words('english')
    index_su = -1
    index_sy = -1
    index_md = -1
    s = "patients name is saraj sharma  He is 25  years old and was born on 28th february 1999 he has acute bronchitis He is having symptoms which are dry cough for the last 3 days no fever and running nose he has the following medicines prescribed  azithromycin 500 mg once a day for 3 days and robitussin 5 ml thrice a day for 5 days he is advised to drink warm water and he is not allowed to eat grapes"
    s = s.lower()
    z = re.split(' he ',s)
    if(len(z)<2):
        z = re.split(' she ', s)
        GEN = "FEMALE"
    else:
        GEN = "MALE"

    data = pd.DataFrame(z)
    data.columns = ['body']
    print(data['body'])
    def tokenize(text):
        tokens = re.split('\W+',text)
        return tokens
    data['body_text_clean'] = data['body'].apply(lambda x: tokenize(x.lower()))
    def remove_stopwords(list):
        text = [word for word in list if word not in stopword]
        return text
    data['body_text'] = data['body_text_clean'].apply(lambda x: remove_stopwords(x))
    for e in range(0,len(data['body_text'])-1):
            if(data['body'][e].find('suf') > 0):
                index_su = e
            if(data['body'][e].find('sym') > 0):
                index_sy = e
            if(data['body'][e].find('med') > 0 or data['body'][e].find('take') > 0 ):
                index_md = e
    if(index_su == -1):
        for e in range(0,len(data['body_text'])-1):
            if(data['body'][e].find('has') >= 0):
                index_su = e
                break
    S = ' '.join(data['body_text'][0]) ## NAmE
    Name = re.split('name',S)[1]   ## NAmE
    if(len(Name)<2):
        Name = S[0] + S[1]
    Age = re.findall(' \d\d ',s)[0]  ## AGE
    ## SAME INDEX of BOTH SYMPTOMS and SUFFERINGS
    if(index_su == index_sy):
        comm = ' '.join(data['body_text'][index_su])
        S2 = re.split('sufferings*', comm)
        Symptoms1 = re.split('symptoms*', S2[1])
        S3 = S2[0]
    else:
        Suffer = ' '.join(data['body_text'][index_su])
        S3 = re.split('sufferings*', Suffer)
        Symp = ' '.join(data['body_text'][index_sy])
        Symptoms1 = re.split('symptoms*', Symp)
    ## SAME COMMOM PROCESSING FOR ABOVE
    if (len(S3) < 2):
        S2 = re.split('has', Suffer)
    b = len(S3)
    S4 = S3[b-1]
    Symptoms = Symptoms1[1]

    Med1 = " ".join(data['body_text_clean'][index_md])
    Med2 = re.split('medicines*',Med1)[1]
    if(len(Med2)<2):
        Med2 = re.split('takes*', Med1)[1]
    Med3 = re.split(' and ',Med2)
    Advice = ""
    for i in range(5, len(z)):
        Advice1 = ' '.join(data['body_text_clean'][i])
        Advice += " " + Advice1
    print('Name: '+Name + "\n")
    print('Age: '+Age + "\n")
    print('Gender: '+GEN + "\n")
    print('Diagnosis: ' + S4 + "\n")
    print('Symptoms: '+ Symptoms + "\n")
    print('Medicine: ')
    for i in range(0,len(Med3)):
        print(i+1)
        print(" " + Med3[i] + "\n")
    print('Advice: '+Advice)