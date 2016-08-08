while 1:
    try:
        FizzDivider = int(input("Input Fizz dividor: "))
        BuzzDivider = int(input("Input Buzz dividor: "))
        break
    except ValueError:
        print("Please enter an integer")
        continue
def FizzBuzz(n):
    if n % FizzDivider == 0 and n % BuzzDivider == 0:
        return 'FizzBuzz'
    elif n % FizzDivider == 0:
        return 'Fizz'
    elif n % BuzzDivider == 0:
        return 'Buzz'
    else:
        return str(n)
print("\n")
for n in range(1, 21):
    print(FizzBuzz(n))