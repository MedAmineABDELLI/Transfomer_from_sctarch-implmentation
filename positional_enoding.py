import numpy as np

# Sample input text and shifted input
tokenised_texte = ["the", "cat", "is", "so"]
shifted_pos_text = ["SOS", "the", "cat", "is"]

d_model = len(shifted_pos_text)  # d_model = 4


def Postionnal_encoding_word(word_postion, d_model):
    dinominator = []
    PE_array = []

    # 1. Calculate denominators for even dimensions
    index = 0
    for i in range(0, d_model, 2):
        k = (2 * index) / d_model
        denom = 10000**k  # Standard Transformer base is 10000
        dinominator.append(denom)
        index += 1

    # 2. Calculate sin/cos values for each dimension
    index = 0
    for j in range(0, d_model):
        if j % 2 == 0:
            # Division MUST be inside np.sin()
            val = np.sin(word_postion / dinominator[index])
            PE_array.append(float(val))
        else:
            # Division MUST be inside np.cos()
            val = np.cos(word_postion / dinominator[index])
            PE_array.append(float(val))
            index += 1

    return PE_array


def generate_postionnal_encoding_matrix(tokenised_texte, d_model):
    PE_matrix = []

    # Single loop over sequence positions (0, 1, 2, ... len-1)
    for pos in range(len(tokenised_texte)):
        # Pass ONLY the word_position integer and d_model
        word_embedding_vector = Postionnal_encoding_word(
            word_postion=pos, d_model=d_model
        )
        PE_matrix.append(word_embedding_vector)

    # Return AFTER the loop finishes building all rows
    return PE_matrix


# Execute function
PE_matrix = generate_postionnal_encoding_matrix(
    tokenised_texte=shifted_pos_text, d_model=d_model
)

# Print resulting Positional Encoding Matrix (4 x 4)
for row in PE_matrix:
    print([round(x, 4) for x in row])




