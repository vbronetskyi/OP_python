p_1 = int(input())
p_2 = int(input())
p_3 = int(input())
p_4 = int(input())
p_5 = int(input())

if (0 <= p_1 <= 100)&(0 <= p_2 <= 100)&(0 <=p_3 <= 100)&(0 <= p_4 <= 100)&(0 <= p_5<= 100):
    percent_grade = (p_1 + p_2 + p_3 + p_4 + p_5) / 5
    letter_grade = None
    if percent_grade >= 90:
        letter_grade = 'A'
    elif percent_grade >= 82:
        letter_grade = 'B'
    elif percent_grade >= 75:
        letter_grade = 'C'
    elif percent_grade >= 67:
        letter_grade = 'D'
    elif percent_grade >= 60:
        letter_grade = 'E'
    else:
        letter_grade = 'F'
    if percent_grade==0:
        print("Average grade =", round(percent_grade), "->", letter_grade)
    else:
        print("Average grade =", round(percent_grade, 2), "->", letter_grade)
else:
    print(None)

