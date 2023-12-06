import logging
import sys


def save_input_to_file(s):
    with open('output.txt', 'w+') as f:
        f.write(s)
    print(f"Created output.txt file with content {s[:10]}...")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv
    if len(sys.argv) < 2:
        print("No string input was given")
        exit(1)
    save_input_to_file(args[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
