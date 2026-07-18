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

def postional_encoding_sentence(dim,sequence_of_tokens):
    PE_matrix = np.array(dim , dim)
    for i in sequence_of_tokens:
        PE_matrix[dim:] = postional_encoding_word(i,sequence_of_tokens)
    return PE_matrix



sequence_cleaned_tokens = ["le" , "chat" , "dort", "bien"]
PE = postional_encoding_sentence(len(sequence_cleaned_tokens) ,  sequence_of_tokens=sequence_cleaned_tokens  )
print(PE)

