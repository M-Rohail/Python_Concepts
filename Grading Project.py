def get_average_score(n):
    add = sum(n)
    size = len(n)
    average = add/size
    return average


def compute_grade(G):
    if G >= 80 and G <= 100:
        result = "Grade A"
    elif G >= 60 and G < 80:
        result = "Grade B"
    elif G >= 50 and G < 60:
        result = "Grade C"
    else:
        result = "Grade F"
    return result


score = [55, 51, 66, 75, 54]
Average = get_average_score(score)
print(Average)
Grade = compute_grade(Average)
print(Grade)
