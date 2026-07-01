user_str = "godfater"


movie_dict = {"The Shawshank Redemption": 9.5,
              "Pulp Fiction": 8.8,
              "The Room": 3.6,
              "The Godfather": 9.2,
              "The Godfather: Part II": 9.0,
              "The Dark Knight": 9.0,
              "12 Angry Men": 8.9,
              "Everything Everywhere All At Once": 8.9,
              "Forrest Gump": 8.8,
              "Star Wars: Episode V": 3.6}


def init_matrix( user_str, compare_str ):
    fuzzy_matrix = []
    for i in range(len(compare_str)+1):
        row = []
        for j in range(len(user_str)+1):
            if i == 0:
                row.append(j)
            else:
                if j == 0:
                    row.append(i)
                else:
                    row.append(-1)
        fuzzy_matrix.append(row)

    ## Print empty matrix as kind of table to check
    ##for i in range(len(user_str) + 1):
        ##print(fuzzy_matrix[i])

    return fuzzy_matrix


def fill_matrix(matrix, user_str, compare_str):
    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[row])):
            left_cell = matrix[row][column - 1] + 1
            top_cell = matrix[row - 1][column] + 1
            top_char = user_str[column - 1]
            left_char = compare_str[row - 1]
            if left_char != top_char:
                diagonal_value = 1
            else:
                diagonal_value = 0
            diagonal_cell = matrix[row - 1][column - 1] + diagonal_value
            matrix[row][column] = min(diagonal_cell, left_cell, top_cell)

    ## Print filled matrix as kind of table to check
    ##for i in range(len(user_str) + 1):
     ##   print(matrix[i])

    return matrix


def calc_distance(user_str, compare_str):
    matrix = init_matrix( user_str, compare_str )
    filled_matrix = fill_matrix(matrix, user_str, compare_str)
    distance = filled_matrix[-1][-1]
    return distance


suggestions_list = []
threshold = 10
for movie in movie_dict:
    distance = calc_distance(user_str, movie)
    ## print(f"{movie}: {distance}") ## just checking
    if distance <= threshold:
        suggestions_list.append(movie)

print(suggestions_list)

