import sys 
def find_sequence(sequence, first_str, second_str): 
    i = j = 0 
    res1 = res2 = ""
    for index in range(len(sequence)): 
        first_letter = sequence[index][0] 
        second_letter = sequence[index][1]
        if first_letter == first_str[i] and second_letter == second_str[j]: 
            res1 += first_str[i] + ' '
            res2 += second_str[j] + ' '
            i += 1
            j += 1 
        elif first_letter != first_str[i] and second_letter == second_str[j]:
            while first_letter != first_str[i]: 
                res1 += first_str[i] + ' '
                res2 += '- ' 
                i+=1 
            res1 += first_str[i] + ' '
            res2 += second_str[j] + ' '
            i+=1
            j+=1
        elif second_letter != second_str[j] and first_letter == first_str[i]:
            while second_letter != second_str[j]: 
                res1 += '- ' 
                res2 += second_str[j] + ' '
                j+=1 
            res1 += first_str[i] + ' '
            res2 += second_str[j] + ' '
            i+=1
            j+=1 
        else: 
            print('violation') 
    while i < len(first_str): 
        res1 += first_str[i] + ' '
        res2 += '- ' 
        i+=1 
    while j < len(second_str): 
        res2 += second_str[j] + ' '
        res1 += '-' 
        j+= 1
    return res2,res1

def fill_in_table(in1, in2, scoring_table, look_up, levenshtein_table): 
    sequence = [] 
    has_more_than_one = False 
    for i in range(1, len(in2) + 1): 
        for j in range(1, len(in1) + 1): 
            vertical_index = look_up[in2[i-1]]
            horizontal_index = look_up[in1[j-1]]
            cell_score = scoring_table[vertical_index][horizontal_index] 
            left_score = levenshtein_table[i - 1][j] 
            top_score = levenshtein_table[i][j - 1]
            diagonal_score = cell_score + levenshtein_table[i-1][j-1]
            max_score = max(left_score, top_score, diagonal_score) 
            levenshtein_table[i][j] = max_score
            if max_score == diagonal_score and max_score != left_score and max_score != top_score:
                if has_more_than_one:
                    sequence.pop()
                    sequence.append((in2[i-1], in1[j-1]))
                else: 
                    if levenshtein_table[i][j] >= levenshtein_table[i-1][len(in1)]:
                        if len(sequence) != 0 and levenshtein_table[i][j] == levenshtein_table[i-1][len(in1)]:
                            sequence.pop()
                        sequence.append((in2[i-1], in1[j-1]))
                        has_more_than_one = True           
        has_more_than_one = False
    #print(levenshtein_table)
    #print(sequence)
    res1, res2 = find_sequence(sequence, in2, in1)
    return res1, res2, levenshtein_table[len(in2)][len(in1)]
def main(): 
    if len(sys.argv) != 2: 
        print('Usage: python3 Genes.py [in.txt]')
    file_name = sys.argv[1]
    f = open (file_name, 'r') 
    in1 = f.readline().strip() 
    in2 = f.readline().strip() 
    f.readline()
    scoring_table = [[0 for x in range(5)] for y in range(5)]
    lines = f.readlines() 
    for i in range(len(lines)): 
        line = lines[i].strip()
        components = line.split(' ') 
        
        for index in range(1, len(components)): 
            scoring_table[i][index-1] = int(components[index]) 
    look_up = {"A": 0, "C": 1, "G": 2, "T":3, "-": 4}
    levenshtein_table = [[0 for x in range(len(in1) + 1)] for y in range(len(in2) + 1)]
    str_ans_1, str_ans_2, highest_scoring = fill_in_table(in1, in2, scoring_table, 
            look_up, levenshtein_table)
    print('x:', str_ans_1)
    print('y:', str_ans_2) 
    print('Score:', highest_scoring, end='')

if __name__ == "__main__": 
    main()


