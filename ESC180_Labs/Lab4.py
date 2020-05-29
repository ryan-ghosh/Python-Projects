import utilities

def parse_story(file_name):
    new_bad_list = []
    for h in range(len(utilities.BAD_CHARS)):
        new_bad_list.append(utilities.BAD_CHARS[h])
    new_bad_list.append("\n")
    file_name = open(file_name, 'r')
    contents = file_name.read()
    contents = contents.lower()
    file_name.close()
    parsed_list = []
    for i in new_bad_list:
        contents = contents.replace(i, " ")
    for j in utilities.VALID_PUNCTUATION:
        contents = contents.replace(j, " " + j + " ")
    contents1 = contents.split(" ")
    for k in range(1, len(contents1) + 1):
        if contents1[(k-1)] != "":
            parsed_list.append(contents1[(k-1)])
    return parsed_list

def get_prob_from_count(counts):
    x = 0
    prob = []
    for i in range(len(counts)):
        x += counts[i]
    for i in range(len(counts)):
        prob.append(counts[i] / x)
    return prob

def build_ngram_counts(words, n):
    d = {}
    for i in range(len(words) - n):
        unfriendly_tuple = tuple(words[i: i + n])
        if unfriendly_tuple in d:
            if words[i + n] in d[unfriendly_tuple][0]:
                index = d[unfriendly_tuple][0].index(words[i + n])
                d[unfriendly_tuple][1][index] += 1
            else:
                d[unfriendly_tuple][0].append(words[i + n])
                d[unfriendly_tuple][1].append(1)
        else:
            d[unfriendly_tuple] = [[words[i + n]]]
            d[unfriendly_tuple].append([1])
    return d

def prune_ngram_counts(ngram_counts, prune_len):
    for i in ngram_counts:
        curr_element = 1
        for j in range(len(ngram_counts[i][1])):
            while curr_element < len(ngram_counts[i][1]):
                j = curr_element
                while j > 0 and ngram_counts[i][1][j] < ngram_counts[i][1][j - 1]:
                    ngram_counts[i][1][j], ngram_counts[i][1][j - 1] = ngram_counts[i][1][j - 1], ngram_counts[i][1][j]
                    ngram_counts[i][0][j], ngram_counts[i][0][j - 1] = ngram_counts[i][0][j - 1], ngram_counts[i][0][j]
                    j -= 1
                curr_element += 1
    for i in ngram_counts:
        while len(ngram_counts[i][1]) > prune_len:
            if len(ngram_counts[i][1]) == prune_len + 1 and ngram_counts[i][1][0] == ngram_counts[i][1][1]:
                break
            else:
                index = ngram_counts[i][1].index(min(ngram_counts[i][1]))
                ngram_counts[i][1].remove(ngram_counts[i][1][0])
                ngram_counts[i][0].remove(ngram_counts[i][0][index])
    return ngram_counts

def probify_ngram_counts(ngram_counts):
    for i in ngram_counts:
        x = 0
        for j in ngram_counts[i][1]:
            x += j
        for k in range(len(ngram_counts[i][1])):
            ngram_counts[i][1][k] = ngram_counts[i][1][k] / x
    return ngram_counts

def build_ngram_model(words, n):
    x = build_ngram_counts(words, n)
    yuh = probify_ngram_counts(x)
    for i in yuh:
        curr_element = 1
        for j in range(len(yuh[i][1])):
            while curr_element < len(yuh[i][1]):
                j = curr_element
                while j > 0 and yuh[i][1][j] > yuh[i][1][j - 1]:
                    yuh[i][1][j], yuh[i][1][j - 1] = yuh[i][1][j - 1], yuh[i][1][j]
                    yuh[i][0][j], yuh[i][0][j - 1] = yuh[i][0][j - 1], yuh[i][0][j]
                    j -= 1
                curr_element += 1
    return yuh

def gen_bot_list(ngram_model, seed, num_tokens):
    hard_in_da_paint = []
    bruh = []
    for i in range(len(seed)):
        bruh.append(seed[i])
    if len(seed) > num_tokens:
        for i in range(num_tokens):
            hard_in_da_paint.append(seed[i])
    elif len(seed) <= num_tokens:
        if seed not in ngram_model:
            for i in range(len(seed)):
                hard_in_da_paint.append(seed[i])
        elif seed in ngram_model:
            for i in range(len(bruh)):
                hard_in_da_paint.append(bruh[i])
            for i in range(num_tokens - len(bruh)):
                hard_in_da_paint.append(utilities.gen_next_token(tuple(bruh), ngram_model))
                bruh = hard_in_da_paint[-(len(bruh)):len(hard_in_da_paint)]
    return hard_in_da_paint

def gen_bot_text(token_list, bad_author):
    if bad_author == True:
        string = ' '.join(token_list)
    if bad_author == False:
        new_list = [token_list[0].capitalize()]
        for x in token_list:
            if x is not token_list[0] and x not in utilities.VALID_PUNCTUATION:
                if new_list[(len(new_list) - 1)] in utilities.END_OF_SENTENCE_PUNCTUATION:
                    new_list.append(" " + x.capitalize())
                elif x.capitalize() in utilities.ALWAYS_CAPITALIZE:
                    x = x.capitalize()
                    new_list.append(" " + x)
                else:
                    new_list.append(" " + x)
            if x in utilities.VALID_PUNCTUATION:
                new_list.append(x)

        string = ''.join(new_list)
    return string

def write_story(file_name, text, title, student_name, author, year):
    return 'cmon bro u know i aint getting this'
if __name__ == "__main__":
    ngram_counts = {('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 20, 10, 2]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]], ('toronto', 'is'): [['six', 'drake', 'smell', 'bad'], [2, 2, 3, 4, 5, 6, 6]]}
    words = ['the', 'child', 'will', 'the', 'child', 'can', 'the', 'child', 'will', 'the', 'child', 'may', 'go', 'home', '.']
    seed = ('the', 'child')
    token_list = ['this', 'is', 'a', 'string', 'of', 'text', '.', 'which', 'needs', 'to', 'be', 'created', '.']
    ngram_model = {('the', 'child'): [['will', 'can', 'may'], [0.5, 0.25, 0.25]], ('child', 'will'): [['the'],[1.0]], ('will', 'the'): [['child'], [1.0]], ('can', 'the'): [['child'], [1.0]], ('child', 'may'): [['go'], [1.0]], ('may', 'go'): [['home'], [1.0]], ('go', 'home'): [['.'], [1.0]]}
#    print(parse_story('file_example.txt'))
#    print(get_prob_from_count([10, 20, 40, 30]))
#    print(probify_ngram_counts(ngram_counts))
#    print(build_ngram_counts(words, 2))
#    print(prune_ngram_counts(ngram_counts, 3))
#    print(build_ngram_model(words, 2))
    print(gen_bot_list(ngram_model, seed, 5))
#    print(gen_bot_text(token_list, False))
#    print(write_story('file_example.txt', 'YERRRRR', 'Ryan Ghosh', 'Ryan', 'boi', '2019'))