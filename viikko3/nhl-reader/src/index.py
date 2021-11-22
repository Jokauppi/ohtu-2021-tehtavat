import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    nation = "FIN"
    response = requests.get(url)
    response_dict = filter(lambda x: x['nationality'] == nation, response.json())

    players = []

    for player_dict in response_dict:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games']
        )

        players.append(player)


    print(f"Players from {nation} {response.headers['Date']}")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
