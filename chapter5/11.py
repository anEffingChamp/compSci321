# author Jonathan Smalls
# computer science 321
# two highest scores
studentCount = eval(input('Please input the number of students: '))
studentScore = []
for count in range(0, studentCount):
    studentScore.append(eval(input('Please input the score for student ' + str(count + 1) + ': ')))

scoreFirst = max(studentScore)
studentScore.remove(scoreFirst)
scoreSecond = max(studentScore)
print('The high scores are ' + str(scoreFirst) + ' and ' + str(scoreSecond))
