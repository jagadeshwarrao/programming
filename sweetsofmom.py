def solve(score,is_birthday):
    # write your code from here
    if(is_birthday):
        if(score <= 60):
            score = score+5
        elif(score >= 61 and score <= 80):
            score = score+5
        else:
            score=score+5
    if(score <= 60):
        print(0)
    elif(score >= 61 and score <= 80):
          print(1)
    else:
          print(2)