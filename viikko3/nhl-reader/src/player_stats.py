from player import Player
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self.player_reader.get_players()
        players = filter(lambda p: p['nationality'] == nationality, players)
        players = sorted(players, key=lambda p: p['goals'], reverse=True)
        return players
