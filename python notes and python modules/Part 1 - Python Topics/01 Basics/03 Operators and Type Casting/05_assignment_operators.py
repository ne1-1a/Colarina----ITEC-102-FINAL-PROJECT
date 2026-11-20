# Example 5 (Intermediate): Assignment operators - a game score tracker
score = 100
print("Start         :", score)

score += 50       # score = score + 50
print("Found a coin  :", score)

score -= 30       # score = score - 30
print("Hit by enemy  :", score)

score *= 2        # score = score * 2
print("Double points :", score)

score //= 3       # score = score // 3
print("Split in 3    :", score)

score %= 50       # score = score % 50
print("Wrap at 50    :", score)

score **= 2       # score = score ** 2
print("Squared       :", score)

score /= 4        # score = score / 4  (becomes a float!)
print("Divided by 4  :", score, type(score).__name__)
