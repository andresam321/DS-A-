def other_string(str):
    new_str = []
    for i in range(len(str)):
        if i % 2 == 0:
            new_str.append(str[i])
    print("".join(new_str))
    return "".join(new_str)
    


other_string("house")