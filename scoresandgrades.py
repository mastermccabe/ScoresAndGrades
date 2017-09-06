
def grader(random_num):
    if random_num > 89: grade = 'A'
    elif random_num > 79: grade = 'B'
    elif random_num > 69: grade = 'C'
    elif random_num > 59: grade = 'D'
    else: grade is 'F'
    return grade

def scoresandgrades():

    import random
    grade = ''

    for i in range(10):
        random_num = random.randint(60,100)
        grade = grader(random_num)
        # if random_num > 89: grade = 'A'
        # elif random_num > 79: grade = 'B'
        # elif random_num > 69: grade = 'C'
        # elif random_num > 59: grade = 'D'
        # else: grade is 'F'

        print 'Score:', random_num,' : Your grade is', grade


# scoresandgrades.grader()
scoresandgrades()
