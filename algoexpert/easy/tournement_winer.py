from typing import List


def tournamentWinner(competitions: List[List[str]], results: List[int]) -> str:
    dic = {}

    for i, teams in enumerate(competitions):
        home_team, away_team = teams
        if results[i] == 0:
            if away_team in dic:
                dic[away_team] = dic[away_team] + 3
            else:
                dic[away_team] = 3
        else:
            if home_team in dic:
                dic[home_team] = dic[home_team] + 3
            else:
                dic[home_team] = 3

    max_score = 0
    winner_team = ""

    print(dic)
    for team, score in dic.items():
        if score > max_score:
            winner_team = team
            max_score = score

    return winner_team


if __name__ == '__main__':
    print(tournamentWinner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1]))
    print(tournamentWinner([["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]], [0, 1, 1]))
