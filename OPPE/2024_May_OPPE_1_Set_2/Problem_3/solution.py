from collections import defaultdict


def top_k_teams(batsmen: list, k: int) -> list:
    '''
    Given a list of dictionaries with batsman names, runs, and team names,
    Create a list with the top k teams in terms of total runs
    starting from the highest to the lowest runs.

    Assume no two teams have the same number of runs.
    '''
    runs_dict = defaultdict(int)
    for data in batsmen:
        runs_dict[data['team']]  += data['runs']
    return sorted(runs_dict, key=runs_dict.get, reverse=True)[:k]
