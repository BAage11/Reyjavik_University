RANK = 0
NAME = 1
COUNTRY = 2
RATING = 3
BYEAR = 4

def get_filename_from_user(prompt):
    file_name = input(prompt)
    return file_name

def create_key(name_data):
    last_name, first_name = name_data.split(",")
    full_name = "{} {}".format(first_name.strip(), last_name.strip())
    return full_name

def process_value_data(chess_player_data):
    rank = int(chess_player_data[RANK])
    country = chess_player_data[COUNTRY].strip()
    rating = int(chess_player_data[RATING])
    birth_year = int(chess_player_data[BYEAR])
    return [rank, country, rating, birth_year]

def create_country_dict(chess_player_dict):
    country_dict = {}
    for key, value in chess_player_dict.items():
        country = value[3]              # Þessu bara breytt í 3 (var 1)
        if country in country_dict:
            country_dict[country].append(key)
        else:
            country_dict[country] = [key]
    return country_dict

def get_data_from_file(file_name):
    chess_player_dict = {}
    try:
        with open(file_name, "r") as file_content:
            for line in file_content:
                line = line.split(";")
                key = create_key(line[NAME])
                value = process_value_data(line)
                chess_player_dict[key] = value
    except FileNotFoundError:
        pass
    return chess_player_dict

def print_header(header_text):
    print(header_text)
    print("-" * len(header_text))

def get_average_for_country(names, player_dict):
    sum = 0
    for player in names:
        sum += player_dict[player][2]
    return sum / len(names)

def print_result(chess_player_dict, country_dict):
    for key, value in sorted(country_dict.items()):
        average = get_average_for_country(value, chess_player_dict)
        print("{} ({}) ({:.1f}):".format(key, len(value), average))
        for name in value:
            print("{:>40s}{:>10d}".format(name, chess_player_dict[name][2]))


def main():
    file_name = get_filename_from_user("Enter name of file: ")
    chess_player_dict = get_data_from_file(file_name)
    country_dict = create_country_dict(chess_player_dict)
    print_header("Players by country:")
    print_result(chess_player_dict, country_dict)


main()