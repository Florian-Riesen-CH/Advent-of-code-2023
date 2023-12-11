import math
multiper  = 2
rowEmpty = list()
colsEmpty = list()

def print_matrice(matrice):
    for i in matrice:
        for y in i:
            if y == '#':
                print("\033[33m#\033[0m", end='')
            else:
                print("\033[34m.\033[0m", end='')
        print()
def dedoubler_line_cols_sans_hashtag(grille):
    for i in range(len(grille)):
        grille[i] = grille[i].replace('\n','')
    for row in range(len(grille)):
        if grille[row].count('#') == 0:
            rowEmpty.append(row)
            
    # Convertir les lignes de la grille en liste de colonnes
    colonnes = [''.join(ligne[i] for ligne in grille) for i in range(len(grille[0]))]
    # Détecter les colonnes sans #
    #colonnes_a_copier = [i for i, col in enumerate(colonnes) if '#' not in col]
    # Copier les colonnes identifiées un million de fois
    for i in range(len(colonnes)):
        if colonnes[i].count('#') == 0:
            colsEmpty.append(i)
    return grille
def find_all_hashtag(grille):
    all_hash_tag = list()
    for x in range(len(grille)):
        for y in range(len(grille[x])):
            if grille[x][y] == '#':
                all_hash_tag.append((x,y))
    return all_hash_tag
def calcul_distance(from_x, from_y,to_x, to_y):
    min_x = min(from_x,to_x)
    max_x = max(from_x,to_x)
    min_y = min(from_y, to_y)
    max_y = max(from_y, to_y)
    range_x = [i for i in range(min_x+1,max_x+1)]
    range_y = [i for i in range(min_y+1,max_y+1)]
    interval_x = set(range_x) & set(rowEmpty)
    interval_y = set(range_y) & set(colsEmpty)
    distance_x = len(range_x)+ (len(interval_x) * (multiper-1))
    distance_y = len(range_y)+ (len(interval_y) * (multiper-1))
    distance = distance_x + distance_y
    return distance
def calcul_all_distance(hash_tag_list):
    index = 1
    total = 0
    tested_path = list()
    for from_hash in hash_tag_list:
        for to_hash in hash_tag_list:
            if from_hash != to_hash:
                if not (to_hash[0], to_hash[1], from_hash[0], from_hash[1]) in tested_path:
                    print(index)
                    distance = calcul_distance(from_hash[0], from_hash[1], to_hash[0], to_hash[1])
                    tested_path.append((from_hash[0], from_hash[1], to_hash[0], to_hash[1]))
                    total += distance
                    index += 1
    return total

print("lecture du fichier")
file = open("input.txt", "r").readlines()
print("Extension de l'univers")
dedoubler_line_cols_sans_hashtag(file)
print_matrice(file)
print("Recherche des #")
hash_tag_list = find_all_hashtag(file)
print("Calcul des distances #")
total = calcul_all_distance(hash_tag_list)
print(total)
