questions = [
    {
        "question": "რომელია საქართველოს დედაქალაქი?",
        "options": ["A) ბათუმი", "B) ქუთაისი", "C) თბილისი", "D) რუსთავი"],
        "answer": "C"
    },
    {
        "question": "რამდენი წელი შეადგენს ათწლეულს?",
        "options": ["A) 5", "B) 10", "C) 50", "D) 100"],
        "answer": "B"
    },
    {
        "question": "რომელია ყველაზე დიდი ოკეანე?",
        "options": ["A) ატლანტის", "B) ინდოეთის", "C) წყნარი", "D) არქტიკის"],
        "answer": "C"
    }
]

score = 0
question_number = 1

print("კეთილი იყოს თქვენი მობრძანება Quiz თამაშში! 🧠")
print("გთხოვთ პასუხები ჩაწეროთ ზუსტად ასოებით: A, B, C ან D (დიდი ასოებით)\n")

for q in questions:
    print(f"კითხვა {question_number}: {q['question']}")
    for option in q["options"]:
        print(option)

    user_answer = input("შეიყვანე პასუხი: ") 

    if user_answer == q["answer"]:
        print("სწორია! ✅\n")
        score += 1
    else:
        print(f"არასწორია ❌ სწორი პასუხი იყო: {q['answer']}\n")

    question_number += 1

print(f"თამაში დასრულდა! თქვენი ქულაა: {score} / {len(questions)}")

if score == len(questions):
    print("გილოცავთ! სრულყოფილი შედეგია! 🎉")
elif score >= len(questions) // 2:
    print("კარგად იმუშავე! ")
else:
    print("არაუშავს, სცადე თავიდან და გააუმჯობესე შედეგი! ")