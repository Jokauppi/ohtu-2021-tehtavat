class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = {
            "name": player1_name,
            "score": 0
            }
        self.player2 = {
            "name": player2_name,
            "score": 0
            }

    def won_point(self, player_name):
        if self.player1["name"] == player_name:
            self.player1["score"] += 1
        else:
            self.player2["score"] += 1


    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1["score"] == self.player2["score"]:
            return self.get_equal_score_string()
        elif max(self.player1["score"], self.player2["score"]) >= 4:
            return self.get_advantage_string()
        else:
            return self.get_standard_score_string()
    
    def get_score_string(self, player):
        
        scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

        return scores[player["score"]]

    def get_equal_score_string(self):

        if self.player1["score"] > 3:
            return "Deuce"
        else:
            return f"{self.get_score_string(self.player1)}-All"

    def get_advantage_string(self):

        difference = abs(self.player1["score"] - self.player2["score"])

        if self.player1["score"] > self.player2["score"]:
            winning_player = self.player1
        else:
            winning_player = self.player2

        if difference == 0:
            return self.get_equal_score_string()
        elif difference >= 2:
            return f"Win for {winning_player['name']}"
        else:
            return f"Advantage {winning_player['name']}"

    def get_standard_score_string(self):
        
        return f"{self.get_score_string(self.player1)}-{self.get_score_string(self.player2)}"