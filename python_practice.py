def main():
    sum_3_nums = add_nums(1, 2, 3)
    print("Sum is {}".format(sum_3_nums))
    quotient = divide_by_three(sum_3_nums)
    print("Sum divided by 3 is {}".format(quotient))


def add_nums(num1, num2, num3):
    """add_nums(num1, num2, num3) returns the sum of num1, num2, and num3.
    """
    return num1 + num2 + num3


def divide_by_three(num):
    """divide_by_three(num) returns num divided by 3.
    """
    return num/3


if __name__ == "__main__":
    main()
