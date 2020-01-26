import re
import pandas as pd
import re
import nltk
def nlp(f):
    index_su = -1
    index_sy = -1
    index_md = -1
    index_nm = -1
    stopword = nltk.corpus.stopwords.words('english')
    s = str(f)
    s = s.lower()
    z = re.split(' he ', s)
    if (len(z) < 2):
        z = re.split(' she ', s)
        GEN = "FEMALE"
    else:
        GEN = "MALE"

    data = pd.DataFrame(z)
    data.columns = ['body']

    def tokenize(text):
        tokens = re.split('\W+', text)
        return tokens

    data['body_text_clean'] = data['body'].apply(lambda x: tokenize(x.lower()))

    def remove_stopwords(list):
        text = [word for word in list if word not in stopword]
        return text

    data['body_text'] = data['body_text_clean'].apply(lambda x: remove_stopwords(x))
    for e in range(0, len(data['body_text']) - 1):
        if (data['body'][e].find('nam') > 0):
            index_nm = e
        if (data['body'][e].find('suf') > 0):
            index_su = e
        if (data['body'][e].find('sym') > 0):
            index_sy = e
        if (data['body'][e].find('med') > 0):
            index_md = e
    if (index_su == -1):
        for e in range(0, len(data['body_text']) - 1):
            if (data['body'][e].find('has') >= 0):
                index_su = e
                break
    if (index_md == -1):
        for e in range(0, len(data['body_text']) - 1):
            if (data['body'][e].find('take') >= 0):
                index_md = e
                break
    S = ' '.join(data['body_text'][0])  ## NAmE
    Name = re.split('name', S)  ## NAmE
    if (len(Name) < 2):
        Name = data['body_text'][0][0] + " " + data['body_text'][0][1]
    else:
        Name = Name[1]
    Age = re.findall(' \d\d ', s)[0]  ## AGE
    ## SAME INDEX of BOTH SYMPTOMS and SUFFERINGS
    if (index_su == index_sy):
        comm = ' '.join(data['body_text'][index_su])
        S2 = re.split('sufferings*', comm)
        Symptoms1 = re.split('symptoms*', S2[0])
        if (len(S2) < 2):
            S2 = re.split('has',comm)
        S2 = Symptoms1[0]
        S4 = S2
    else:
        Suffer = ' '.join(data['body_text'][index_su])
        S2 = re.split('sufferings*', Suffer)
        Symp = ' '.join(data['body_text'][index_sy])
        Symptoms1 = re.split('symptoms*', Symp)

        ## SAME COMMOM PROCESSING FOR ABOVE
        if (len(S2) < 2):
            S2 = re.split('has', Suffer)
        b = len(S2)
        S4 = S2[b - 1]
    Symptoms = Symptoms1[1]
    if (index_sy == index_md):
        Sym1 = re.split('medicines*', Symptoms)
        Symptoms = Sym1[0]
    Med1 = " ".join(data['body_text_clean'][index_md])
    Med2 = re.split('medicines*', Med1)
    print()
    if (len(Med2) < 2):
        Med2 = re.split('takes*', Med1)
    Med4 = Med2[1]
    Med3 = re.split(' and ', Med4)
    Advice = ""
    for i in range(index_md + 1, len(z)):
        Advice1 = ' '.join(data['body_text_clean'][i])
        Advice += " " + Advice1

    details = [Name, Age, GEN, S4, Symptoms , Med3 , Advice]
    # print('Name: '+Name + "\n")
    # print('Age: '+Age + "\n")
    # print('Gender: '+GEN + "\n")
    # print('Diagnosis: ' + S4 + "\n")
    # print('Symptoms: '+ Symptoms + "\n")
    # print('Medicine: ')
    # for i in range(0,len(Med2)):
    #     print(i+1)
    #     print(" " + Med2[i] + "\n")
    #     details.append(Med2[i])
    # print('Advice: '+Advice)
    return details