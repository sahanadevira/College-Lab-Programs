
match_list = {}

number_of_matches = int(input("Enter the number of matches: "))

for i in range (number_of_matches):
   match_number = input("Enter match number(eg:match_1):")
   total_players = {}
   number_of_players = int(input("Enter the number of players: "))

   for i in range (number_of_players):
      player_name = input("Enter player name:")
      player_score = input("Enter player score:")

      total_players[player_name] = player_score
   print(total_players)

   match_list[match_number] = total_players
print(match_list)

single_dict = {}

for players in match_list.values():
    for name, score in players.items():
        # 1. Convert the string score to an integer for calculation
        score_int = int(score)

        # 2. Add the score to the existing total, or start at 0 if new
        if name in single_dict:
            single_dict[name] += score_int
        else:
            single_dict[name] = score_int

print("Total Scores per Player:", single_dict)
# Find the player with the highest score
max_player = max(single_dict, key=single_dict.get)
max_score = single_dict[max_player]

print(f"The top player is {max_player} with a score of {max_score}!")

