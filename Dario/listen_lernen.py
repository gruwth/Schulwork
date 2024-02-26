def get_names():
    names = []
    for i in range(5):
        names.append(input(f"Enter name {i+1}: "))
    return names

def reverse_list(list):
    return list[::-1]

def is_in_list(list, name):
    return name in list


def main():
    names = get_names()
    print(reverse_list(names))
    print(is_in_list(names, input("Enter a name to check:")))


main()

