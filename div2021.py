if __name__ == "__main__":
    target = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
    print(target)
