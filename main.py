# import numpy as np

# print(np.sqrt(9))
import logging
from random_word import RandomWords

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


random_words = RandomWords()

# def generate_random_words(list_length: int) -> int:
#     random_words_list=[]
#     for i in range(list_length):
#         random_words_list.append(random_words.get_random_word().upper())
#         sorted_list = sorted(random_words_list)
#     logging.info(f"Generate word list: {sorted_list}")
#     # return(', '.join(sorted_list).upper())
#     return sorted_list

# if __name__ == "__main__":
#     generate_random_words(5)

from random_word import RandomWords
random_words = RandomWords()
def generate_random_words(list_length: int) -> int:
    random_words_list=[]
    for i in range(list_length):
        random_words_list.append(random_words.get_random_word().upper())
        sorted_list = " ".join(sorted(random_words_list))
    logging.info(f"Generate word list: {sorted_list}")
    return sorted_list

if __name__ == "__main__":
    generate_random_words(5)