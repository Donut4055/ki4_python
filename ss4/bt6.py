student = {
    "name": "Lan",
    "scores": {
        "math": 9,
        "english": 8,
        "history": 7
    }
}

print(student['scores']['english'])

scores = student['scores'].values()
average_score = sum(scores) / len(scores)
print(average_score)
