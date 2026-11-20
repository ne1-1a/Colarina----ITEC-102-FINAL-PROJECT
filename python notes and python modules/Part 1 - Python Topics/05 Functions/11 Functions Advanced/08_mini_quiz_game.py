# Example 8 (Hard) MINI PROJECT 3: Python quiz game built from small functions


def ask(question, correct_answer, points=10):
    """Ask one question. Return the points earned (0 if wrong)."""
    answer = input(question + " ").strip().lower()
    if answer == correct_answer.lower():
        print(f"  Correct! +{points} points")
        return points
    print(f"  Wrong. The answer was: {correct_answer}")
    return 0


def get_rank(score, max_score):
    percent = score / max_score * 100
    if percent >= 90:
        return "Python Master"
    if percent >= 70:
        return "Code Ninja"
    if percent >= 40:
        return "Getting There"
    return "Keep Practicing"


def main():
    print("=== PYTHON QUIZ ===\n")
    score = 0
    max_score = 0

    score += ask("1. Which keyword defines a function?", "def")
    max_score += 10

    score += ask("2. What does 7 // 2 give?", "3")
    max_score += 10

    score += ask("3. What is the type name of 3.14?", "float")
    max_score += 10

    score += ask("4. Which keyword leaves a loop immediately?", "break", points=15)
    max_score += 15

    score += ask("5. What does len('Python') return?", "6", points=20)
    max_score += 20

    print()
    print(f"Final score: {score} / {max_score}")
    print("Rank:", get_rank(score, max_score))


main()
