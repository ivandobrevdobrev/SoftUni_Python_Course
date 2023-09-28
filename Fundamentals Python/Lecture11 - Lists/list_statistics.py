n = int(input())

positives = []
negatives = []
count_of_positives = 0
sum_of_negatives = 0
for _ in range(n):
    number = int(input())
    if number < 0:
        negatives.append(number)
        sum_of_negatives += number
    else:
        positives.append(number)
        count_of_positives += 1
print(positives)
print(negatives)
#print(f"Count of positives: {count_of_positives}")
print(f"Count of positives: {len(positives)}")
#print(f"Sum of negatives: {sum_of_negatives}")
print(f"Sum of negatives: {sum(negatives)}")

