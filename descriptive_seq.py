# Author: Minci Zhou
# Date: 2020-05-03


# function that returns the self-descriptive sequence of num
def gen_self_seq(num):
    num_string = str(num)
    pair_store = []
    temp = []
    for i in range(len(num_string)):
        if not temp:
            temp = [1, num_string[i]]
        elif num_string[i] == temp[1]:
            temp[0] += 1
        else:
            pair_store.append(temp)
            temp = [1, num_string[i]]
    pair_store.append(temp)
    return_string = ""
    for pair in pair_store:
        current_pair = str(pair[0]) + str(pair[1])
        return_string += current_pair
    # print(return_string)
    return int(return_string)


# function that returns the Nth self-descriptive sequence of the first entry
def descriptive_seq(first_entry, N):
    counter = 0
    next_entry = first_entry
    while counter < N:
        next_entry = gen_self_seq(next_entry)
        counter += 1
    return next_entry


print(descriptive_seq(2, 15))
