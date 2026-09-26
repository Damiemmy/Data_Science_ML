import numpy as np
import pandas as pd

np.random.seed(42)

N = 100_000

departments = [
    "Computer Science",
    "Cyber Security",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Mathematics",
    "Physics",
]

# -----------------------------
# Basic student information
# -----------------------------

student_id = np.arange(100000, 100000 + N)

age = np.random.normal(21, 2.5, N).round().astype(float)

level = np.random.choice(
    [100, 200, 300, 400, 500],
    size=N,
    p=[0.22, 0.23, 0.22, 0.20, 0.13]
)

department = np.random.choice(
    departments,
    size=N
)

# -----------------------------
# Academic / behavioral data
# -----------------------------

study_hours = np.random.gamma(
    shape=3,
    scale=1.5,
    size=N
)

study_hours = np.clip(study_hours, 0, 15)

attendance_rate = np.random.normal(
    78,
    12,
    N
)

attendance_rate = np.clip(
    attendance_rate,
    0,
    100
)

previous_gpa = np.random.normal(
    2.8,
    0.7,
    N
)

previous_gpa = np.clip(
    previous_gpa,
    0,
    5
)

assignment_average = (
    45
    + previous_gpa * 8
    + np.random.normal(0, 10, N)
)

assignment_average = np.clip(
    assignment_average,
    0,
    100
)

quiz_average = (
    40
    + previous_gpa * 9
    + np.random.normal(0, 12, N)
)

quiz_average = np.clip(
    quiz_average,
    0,
    100
)

midterm_score = (
    35
    + previous_gpa * 10
    + study_hours * 1.5
    + np.random.normal(0, 10, N)
)

midterm_score = np.clip(
    midterm_score,
    0,
    100
)

internet_access = np.random.choice(
    ["Poor", "Average", "Good"],
    size=N,
    p=[0.15, 0.45, 0.40]
)

library_visits = np.random.poisson(
    4,
    N
)

sleep_hours = np.random.normal(
    6.5,
    1.2,
    N
)

sleep_hours = np.clip(
    sleep_hours,
    2,
    12
)

previous_failures = np.random.poisson(
    0.7,
    N
)

extracurricular_hours = np.random.gamma(
    2,
    1.5,
    N
)

extracurricular_hours = np.clip(
    extracurricular_hours,
    0,
    15
)

# -----------------------------
# Create target
# -----------------------------

final_score = (
    0.20 * assignment_average
    + 0.20 * quiz_average
    + 0.25 * midterm_score
    + 0.15 * attendance_rate
    + 3.0 * study_hours
    + 5.0 * previous_gpa
    + 0.5 * library_visits
    - 2.0 * previous_failures
    + 0.8 * sleep_hours
    - 0.5 * extracurricular_hours
    + np.random.normal(0, 8, N)
)

final_score = np.clip(
    final_score,
    0,
    100
)

# -----------------------------
# Build DataFrame
# -----------------------------

df = pd.DataFrame({
    "student_id": student_id,
    "age": age,
    "department": department,
    "level": level,
    "study_hours": study_hours,
    "attendance_rate": attendance_rate,
    "previous_gpa": previous_gpa,
    "assignment_average": assignment_average,
    "quiz_average": quiz_average,
    "midterm_score": midterm_score,
    "internet_access": internet_access,
    "library_visits": library_visits,
    "sleep_hours": sleep_hours,
    "previous_failures": previous_failures,
    "extracurricular_hours": extracurricular_hours,
    "final_score": final_score,
})

# -----------------------------
# Introduce realistic problems
# -----------------------------

# Missing values
for column in [
    "study_hours",
    "attendance_rate",
    "previous_gpa",
    "assignment_average",
    "quiz_average",
]:
    indexes = np.random.choice(
        df.index,
        size=int(N * 0.02),
        replace=False
    )

    df.loc[indexes, column] = np.nan


# Invalid values
invalid_indexes = np.random.choice(
    df.index,
    size=100,
    replace=False
)

df.loc[invalid_indexes[:25], "attendance_rate"] = 150
df.loc[invalid_indexes[25:50], "study_hours"] = -5
df.loc[invalid_indexes[50:75], "previous_gpa"] = 7
df.loc[invalid_indexes[75:], "age"] = 3


# Duplicate rows
duplicates = df.sample(
    500,
    random_state=42
)

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)


# Shuffle everything
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# -----------------------------
# Save
# -----------------------------

output_path = "data/raw_student_performance.csv"

df.to_csv(
    output_path,
    index=False
)

print(f"Dataset created successfully.")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_path}")