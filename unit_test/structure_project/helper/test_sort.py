def is_alphabetized(value):
    return ''.join(sorted(value)) == value



if __name__ == "__main__":
    value1 = "abd"
    print(is_alphabetized(value1))
