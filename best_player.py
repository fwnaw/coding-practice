players = [
    {"name": "Magnus", "rating": 2850},
    {"name": "Hikaru", "rating": 2800},
    {"name": "Fabiano", "rating": 2780}
]

def best_player(players):
    best = players[0]
    for player in players:
         if player['rating'] > best['rating']:
           best = player
    return(best)
    
result = best_player(players)
print(f"{result['name']} is the best player with a rating of {result['rating']}")
