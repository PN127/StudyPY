from typing import List

def avg(numbers: List[int|float]) -> float:
    sum = 0
    count = 0
    for number in numbers:
        sum+=number
        count +=1
    return sum/count

def main():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,13]
    print(avg(numbers))

main()