import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 5 students (rows) and 4 subjects (columns)
scores = np.random.randint(50, 101, size=(5, 4))

print("Original Scores Array:\n", scores)

# 1. Score of 3rd student (index 2) in 2nd subject (index 1)
score_3_2 = scores[2, 1]

# 2. All scores of last 2 students
last_two_students = scores[-2:, :]

# 3. First 3 students, subjects 2 and 3 (indices 1 and 2)
subset = scores[:3, 1:3]

print(f"\n3rd Student, 2nd Subject: {score_3_2}")
print(f"Last 2 Students:\n{last_two_students}")
print(f"First 3 students (Subj 2 & 3):\n{subset}")

# 1. Column-wise mean (axis=0)
subject_means = np.mean(scores, axis=0).round(2)

# 2. Add curve [5, 3, 7, 2] using broadcasting
curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

# Ensure no score exceeds 100
curved_scores = np.clip(curved_scores, 0, 100)

# 3. Row-wise max (axis=1)
best_per_student = np.max(curved_scores, axis=1)

print(f"\nAverage per subject: {subject_means}")
print(f"Curved Scores (Clipped at 100):\n{curved_scores}")
print(f"Best score per student: {best_per_student}")

# 1. Min-Max Normalization per row
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

# Avoid division by zero if min == max
normalized = (curved_scores - row_min) / (row_max - row_min)

# 2. Find index of the single highest value
# argmax returns the flat index; unravel_index converts it to (row, col)
max_idx_flat = np.argmax(normalized)
student_idx, subject_idx = np.unravel_index(max_idx_flat, normalized.shape)

# 3. Boolean Masking for scores > 90
high_scores = curved_scores[curved_scores > 90]

print(f"\nNormalized Scores:\n{normalized.round(2)}")
print(f"Highest Value Location: Student {student_idx}, Subject {subject_idx}")
print(f"Scores above 90: {high_scores}")