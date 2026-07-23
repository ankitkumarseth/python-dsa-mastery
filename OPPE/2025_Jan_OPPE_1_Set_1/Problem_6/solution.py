def filter_students(data: dict, criteria: str) -> set:
    '''
    Takes a dictionary where keys are student names and values are lists of scores, filters names based on the given criteria
     - "excellent" - average score >= 85.
     - "good" - average score >= 50 and < 85.
     - "all_pass" - all scores >= 50.
     - "balanced" - difference between min and max is <= 10.
   
    Args:
        scores(dict)  : keys are student names and values are lists of scores

    Returns:
        set: Set of roll numbers matching the criteria
    '''
    ...
