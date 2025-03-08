def countWins(winner_list, country):
    return sum(1 for winner in winner_list if winner['country'] == country)
