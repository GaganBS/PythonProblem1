from mymodule.process_input import Process
import sys


def main():
    res = Process.file_content(sys.argv[-1])
    result_string = Process.process_secret_message(res)
    if len(result_string.split(' ')) > 3:
        print(result_string)
    else:
        print('None')


if __name__ == '__main__':
    sys.exit(main())
