questions = [
    ["Which language was used to create fb ?", "Arbic", "French", "German", "Python", "None", 4],
    ["Captain of C-Block ?", "Chutiya", "Modi ji", "King ju piu", "Mujeeb", "Mujeeb", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money =0

i=0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\n Question for Rs.{levels[i]}")
    print(questions[i][0])
    print(f"A. {question[1]}       B.{question[2]}\nC. {question[3]}       D.{question[4]}")
    reply = int(input("Enter your answer (1-4):"))
    if(reply==question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if(i==4):
            money =10000
        elif(i==9):
            money = 320000
        elif(i==9):
            money = 10000000
    else:
        print("Wrong Answer!!!")
        break
print("Total money you win = ",money)