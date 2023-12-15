
D = open('input.txt').read().strip()
L = D.split('\n')
legth = 100

def fall_rocks(line):
    falling_line = list()
    part_line = ''.join(line).split('#')
    for part in part_line:
        list_part = [i for i in part]
        for i in range(len(list_part)):
            if list_part[i] == 'O':
                for index in range(i,0,-1):
                    if list_part[index-1] == 'O':
                        break
                    list_part[index-1] = 'O'
                    list_part[index] = '.' 
        falling_line.extend(list_part)
        falling_line.append('#')
    del falling_line[-1]
    return falling_line

def convert_in_cols(array):
    # Déterminez le nombre de colonnes en utilisant la première ligne
    num_columns = len(array[0])
    # Créez une liste vide pour chaque colonne
    columns = [[] for _ in range(num_columns)]
    # Parcourez chaque ligne et chaque caractère pour remplir les colonnes
    for line in array:
        for col_idx, char in enumerate(line):
            columns[col_idx].append(char)
    return columns

def convert_in_row(columns_final):
    lines = []
    num_rows = len(columns_final[0])
    # Parcourez les lignes
    for row_idx in range(num_rows):
        row = ""
        for col in columns_final:
            row += col[row_idx]
        lines.append(row)
    return lines

def calcul_score(lines):
    count_total = 0
    for i in range(0,legth):
        nb_O = lines[i].count('O')
        count_total += nb_O * (legth-i)
    return count_total

def North_gravity(array):
    columns = convert_in_cols(array)
    columns_final = list()
    # Affichez le contenu de chaque colonne
    for col_idx, column in enumerate(columns):
        falling_line = fall_rocks(columns[col_idx])
        columns_final.append(falling_line)

    lines = convert_in_row(columns_final)
    return lines

def west_gravity(array):
    columns_final = list()
    # Affichez le contenu de chaque colonne
    for col_idx, column in enumerate(array):
        falling_line = fall_rocks(array[col_idx])
        columns_final.append(falling_line)
    return columns_final

def south_gravity(array):
    columns = convert_in_cols(array)
    columns_reverse = [sous_liste[::-1] for sous_liste in columns]
    columns_final = list()
    # Affichez le contenu de chaque colonne
    for col_idx, column in enumerate(columns_reverse):
        falling_line = fall_rocks(columns_reverse[col_idx])
        columns_final.append(falling_line)

    columns_reverse_reverse = [sous_liste[::-1] for sous_liste in columns_final]
    lines = convert_in_row(columns_reverse_reverse)
    return lines

def east_gravity(array):
    columns_reverse = [sous_liste[::-1] for sous_liste in array]
    columns_final = list()
    # Affichez le contenu de chaque colonne
    for col_idx, column in enumerate(columns_reverse):
        falling_line = fall_rocks(columns_reverse[col_idx])
        columns_final.append(falling_line)
    columns_reverse_reverse = [sous_liste[::-1] for sous_liste in columns_final]
    lines = columns_reverse_reverse
    return lines


def display_array(array):
    for i in range(legth):
        for y in range(legth):
            print(array[i][y], end='')
        print()
    print('\n')

def format_array(array):
    val = ''
    for i in array:
        val += ''.join(i)
        val += '\n'
    return val

def sont_identiques(liste1, liste2):
    flag = False
    for i in range(len(liste1)):
        for y in range(len(liste1[0])):
            if liste1[i][y] != liste2[i][y]:
                return False
    return True

lines = L.copy()

history = list()
for i in range(1000000001):
    lines = North_gravity(lines)
    if i == 0:
        print('Part 1:', calcul_score(lines))
    lines = west_gravity(lines)
    lines = south_gravity(lines)
    lines = east_gravity(lines)
    str_array = format_array(lines)
    if str_array in history:
        #print('Previous', history.index(str_array), ' actual', i)
        calcul = (1000000000-i) // (i-history.index(str_array))
        #print(calcul)
        calcul = calcul * (i-history.index(str_array)) + i
        #print(calcul)
        diff = 1000000000 - calcul
        index_final = history.index(str_array) + diff
        #print(index_final)
        lines = history[index_final-1]
        break 
    
    history.append(str_array)

count_total = calcul_score(lines.split('\n'))
print('Part 2:', count_total)
