scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
best_student = max(scores, key=scores.get)
print("Najwyższy wynik ma:", best_student)