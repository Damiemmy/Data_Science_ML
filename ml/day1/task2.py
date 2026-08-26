scores = [70, 65, 90, 80, 75]

# Find:
# Total
# Average
# Highest score
# Lowest score

# Then print:
# "Excellent" if average >= 70
# "Needs Improvement" otherwise

total = sum(scores)
average =total/len(scores)
highest_score=max(scores)
lowest_score=min(scores)
print("Average", average)

if average >=70:
    result="Excellent"
else:
    result="Needs Improvement"

print("Result", result)