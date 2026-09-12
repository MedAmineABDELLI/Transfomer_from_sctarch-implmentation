import numpy as np
tokenised_texte = ["the" , "cat" , "is" , "so" ]
d_model = len(tokenised_texte)
def Postionnal_encoding_word(tokenised_test,word_postion):
    dinominator = []
    PE_arrray = []
    index = 0
    for i in range(0,len(tokenised_texte),2):
        k = 2*index / d_model
        denom = 1000**k
        dinominator.append(denom)
        index = index + 1
    index = 0
    for j in range(0,len(tokenised_texte)):
        if j % 2 == 0:
            PE_arrray.append(np.sin(word_postion) / dinominator[index])
        if j % 2 != 0:
            PE_arrray.append(np.cos(word_postion) / dinominator[index])
            index = index + 1


    for i in range(0,len(PE_arrray)):
        PE_arrray[i] = float(PE_arrray[i])


    return PE_arrray

def generate_postionnal_encoding_matrix(tokenised_texte):
    PE_matrix = []
    for i in range(0,len(tokenised_texte)):
        index = 0
        for j in range(0,len(tokenised_texte)):
            word_embdeing_vector = Postionnal_encoding_word(tokenised_texte,word_postion=index)
            #print(word_embdeing_vector)
            PE_matrix.append(word_embdeing_vector)
            index = index + 1

        return PE_matrix




