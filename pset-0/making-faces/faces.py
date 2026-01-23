def main():
    print(convert(input()))


def convert(user_input):
    return user_input.replace(":)", "🙂").replace(":(", "🙁")
    

main()