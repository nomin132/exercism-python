"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """

    rounded_scores=[] 
    while student_scores: 
        score=student_scores.pop()
        #pop removes score from every loop until there is nothing left. 
        rounded_scores.append(round(score))
    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
#set a counter variable starting from 0 
#check each score one by one
#increase the list if value is <=40
    failed_scores=0
    for score in student_scores:
        if score<=40: 
            failed_scores=failed_scores+1
    return failed_scores


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    """create emty list to store scores that pass
    write for loop to examine each score in list student scores 
    inside loop write if statement to check if score is >= threshold variable 
    if condition satisfies, append new score to list
    after loop return to new list"""
    passed_scores=[]
    for scores in student_scores: 
        if scores>=threshold:
            passed_scores.append(scores)
    return passed_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    """calculate step_size using //
    use range() to generate threshold and arguments for conditions
    convert range to list then return"""
    step_size=(highest-40)//4
    step_size=list(range(41, highest, step_size))
    return step_size


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """

    '''initialize empty list for rankings 
    loop using enumerate(student names) to get index and name get matching scores from student_scores(index)
    format using the string f"{index+1}. {name}:{score} then append to list return list'''
    rankings=[]
    for index, names in enumerate(student_names): 
        rankings.append(f"{index+1}. {names}: {student_scores[index]}")
    return rankings


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """

    """look thru student_info unpacking name and score check if score is 100 
    then if it is return [name, 100] if loop ends without finding anyone return []"""
    for name, score in student_info:
        perfect_list=[name, score]
        if score==100:
            return[name, score]
    return []