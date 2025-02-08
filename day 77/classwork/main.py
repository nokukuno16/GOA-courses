def get_grade(s1, s2, s3):
    s = s1+s2+s3
    score = s / 3
    if score <= 100 and score >=90:
        return "A"
    if score <= 90 and score >=80:
        return "B"
    if score <= 80 and score >=70:
        return "C"
    if score <= 70 and score >=60:
        return "D"
    if score <= 60 and score >=0:
        return "F"
    