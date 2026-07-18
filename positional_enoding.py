import numpy as np

def postional_encoding_word(sequence_of_tokens):
    dim = np.zeros(len(sequence_of_tokens))
    PE_matrix = np.zeros((len(sequence_of_tokens) , len(sequence_of_tokens)))
    for i in range(len(sequence_of_tokens)):
        pos = i
        for j in range(len(sequence_of_tokens)):
            if j % 2 == 0:
                dim[i] = np.sin((pos / 1000**(2*j/len(dim))))
                PE_matrix[pos,j] = dim[i]
        else:
            dim[i] = np.cos((pos / 1000**(2*j/len(dim))))
            PE_matrix[pos,j] = dim[i]

        return PE_matrix


tokens = ["le" , "chat" , "dore" , "bien"]
PE = postional_encoding_word(sequence_of_tokens=tokens)
print(PE)

