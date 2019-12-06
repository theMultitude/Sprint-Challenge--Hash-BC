#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i, weight in enumerate(weights):
        num_to_limit = limit - weight  #grab difference in weight
        num_to_limit_index = hash_table_retrieve(ht, num_to_limit) #get the index of that difference

        #check for None and make sure values are in proper order
        if num_to_limit_loc is not None:
            if (i > num_to_limit_index):
                return (i, num_to_limit_index)
            else:
                return (num_to_limit_index, i)
        else:
            hash_table_insert(ht, weight, i)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
