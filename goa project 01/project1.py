
quiz_data = {
    "1": {
        "level_name": "5-10 წლის",
        "questions": [
            {"question": "რომელია საქართველოს დედაქალაქი?", "answer": "თბილისი"},
            {"question": "რამდენი დღეა კვირაში?", "answer": "7"},
            {"question": "რა ფერისაა ცა?", "answer": "ლურჯი"},
        ]
    },
    "2": {
        "level_name": "წავა რა",
        "questions": [
            {"question": "რომელ პლანეტაზე ვცხოვრობთ?", "answer": "დედამიწა"},
            {"question": "რა არის 5 * 6?", "answer": "30"},
            {"question": "რომელ ქვეყანაშია ეიფელის კოშკი?", "answer": "საფრანგეთი"},
        ]
    },
    "3": {
        "level_name": "საკმაოდ ძლიერი",
        "questions": [
            {"question": "ვინ იყო ალბერტ ეინშტაინი?", "answer": "ფიზიკოსი"},
            {"question": "რა ქვია დედამიწის თანამგზავრს?", "answer": "მთვარე"},
            {"question": "რამდენია 12 * 12?", "answer": "144"},
        ]
    },
    "4": {
        "level_name": "გენიოსის დონე",
        "questions": [
            {"question": "რომელ წელს გამოცხადდა საქართველოს დამოუკიდებლობა?", "answer": "1918"},
            {"question": "რა არის ატომის უმცირესი ნაწილაკი?", "answer": "ელექტრონი"},
            {"question": "რა ეწოდება წყალბადის ქიმიურ სიმბოლოს?", "answer": "H"},
        ]
    }
}

def select_level():
    print("\nაირჩიე დონე:")
    for key, level in quiz_data.items():
        print(f"{key}. {level['level_name']}")
    
    choice = input("\nშეიყვანე დონის ნომერი(1-4): ")
    if choice in quiz_data:
        return choice
    else:
        print("არასწორია.")
        return select_level()

def run_quiz(level_key):
    level = quiz_data[level_key]
    print(f"\nარჩეული დონე: {level['level_name']}\n")
    score = 0

    for idx, item in enumerate(level["questions"], 1):
        print(f"კითხვა {idx}: {item['question']}")
        answer = input("თქვენი პასუხი: ").strip().lower()
        if answer == item["answer"].lower():
            print("სწორია\n")
            score += 1
        else:
            print(f"არასწორია. სწორი პასუხი იყო: {item['answer']}\n")

    print(f"შენ დააგროვე {score} ქულა {len(level['questions'])}-დან.")
    if score == len(level["questions"]):
        print("გენაცვალე")
    elif score >= len(level["questions"]) // 2:
        print("საღოლ")
    else:
        print("ისწავლე ძმაო")

def main():
    print("გაუმარჯოს თქვენ მოხვდით quiz-ში")
    level = select_level()
    run_quiz(level)

if __name__ == "__main__":
    main()
