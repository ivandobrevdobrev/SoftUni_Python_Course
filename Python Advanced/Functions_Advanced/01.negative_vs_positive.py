def print_numbers(nums):
    positive_sum = sum(el for el in nums if el > 0)
    negative_sum = sum(el for el in nums if el < 0)

    print(negative_sum)
    print(positive_sum)
    if positive_sum > abs(negative_sum):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
print_numbers(numbers)
