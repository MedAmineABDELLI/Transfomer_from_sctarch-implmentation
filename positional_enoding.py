import numpy as np

def postional_encoding_word(word , sequence_of_tokens):
    dim = np.zeros(len(sequence_of_tokens))
    for i in range(len(sequence_of_tokens)):
        if word == sequence_of_tokens[i]:
            pos = i
            break
    for i in range(len(sequence_of_tokens)):
        if i % 2 == 0:
            dim[i] = np.sin((pos / 1000**(2*i/len(dim))))
        else:
            dim[i] = np.cos((pos / 1000**(2*i/len(dim))))

def postional_encoding_sentence(dim):
    

