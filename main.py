attempt = 0
index = 0
total = 0
correct = 0
exam_id = ""
exam_name = ""
exam_author = ""
questions = []
user_name = ""


def start():
    global user_name, attempt
    user_file = open("users.txt", "r")
    users = user_file.read()
    username = input("Enter Your User Name :- ")
    password = input("Enter Your Password :- ")
    if username == "" or password == "":
        print("Enter Valid Details")
        start()
        return
    if username in users:
        password = "password(" + username + "):-" + password
        if password in users:
            print("Login Success")
            user_name = username
            show_exams()
        else:
            attempt += 1
            print("Invalid Password")
            if attempt >= 3:
                print("Attempt Limit Crossed...")
                return
            start()
    else:
        attempt += 1
        print("Invalid Username")
        if attempt >= 3:
            print("Attempt Limit Crossed...")
            return
        start()
    user_file.close()
    return


def show_exams():
    exam_details_file = open("exams.txt", "r")
    exam_details = exam_details_file.read()
    exam_details = exam_details.split("\n")
    counter = 0
    exams = []
    temp = ["", "", ""]
    while counter < len(exam_details):
        if counter % 4 == 0:
            temp[0] = exam_details[counter].replace("id:-", '')
        elif counter % 4 == 1:
            temp[1] = exam_details[counter].replace("exam(" + temp[0] + "):-", "")
        elif counter % 4 == 2:
            temp[2] = exam_details[counter].replace("author(" + temp[0] + "):-", "")
        else:
            exams.append(temp)
            temp = ["", "", ""]
        counter += 1
    print("##################################################################################################")
    print("Choose Exam From Below :- ")
    counter = 1
    for e in exams:
        print(f"{counter}. {e[1]}")
        counter += 1
    count = int(input("Enter the exam index :- "))
    global exam_id, exam_name, exam_author
    exam_id = exams[count - 1][0]
    exam_name = exams[count - 1][1]
    exam_author = exams[count - 1][2]
    load_questions()
    exam_details_file.close()
    return


def load_questions():
    global questions, total
    try:
        question_file = open("./questions/" + exam_id + ".txt", "r")
        question_details = question_file.read()
        question_details = question_details.split("\n")
        temp = ["", "", "", "", "", "", ""]
        counter = 0
        while counter < len(question_details):
            temp[counter % 7] = question_details[counter]
            if counter % 7 == 6:
                questions.append(temp)
                temp = ["", "", "", "", "", "", ""]
            counter += 1
        print("##################################################################################################")
        total = len(questions)
        start_exam()
    except Exception as ignored:
        print("Cannot Locate Questions")
    return


def start_exam():
    global questions, total, correct, exam_name, exam_id
    for q in questions:
        show_question(q)
    print(f"Result :- {correct}/{total}")
    return


def show_question(question):
    global correct
    print("##################################################################################################")
    print(f"Question No :- {int(question[0]) + 1}")
    print(f"Question :- {question[1]}")
    print(f"1. {question[2]}")
    print(f"2. {question[3]}")
    print(f"3. {question[4]}")
    print(f"4. {question[5]}")
    while True:
        choice_no = int(input("Enter Your Choice Number :- "))
        if 5 > choice_no > 0:
            if question[choice_no + 1] == question[6]:
                correct += 1
            break
        else:
            print("Enter Correct Choice in between 1 to 4")
    return


start()
