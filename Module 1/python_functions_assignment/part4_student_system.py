def get_greeting(name):
    return "Hello, " + name

def calculate_stats(scores):
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects
    return num_subjects, average_score

def check_pass_fail(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    student_name = "Atharva"
    student_scores = [80, 75, 90, 65, 85]

    greeting_msg = get_greeting(student_name)
    subjects_count, average_score = calculate_stats(student_scores)
    final_result = check_pass_fail(average_score)

    print(greeting_msg)
    print("Subjects:", subjects_count)
    print("Average Score:", average_score)
    print("Result:", final_result)

if __name__ == "__main__":
    main()
