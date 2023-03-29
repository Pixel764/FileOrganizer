from organizer import organize


def start():
    while True:
        path = str(input('Full path: '))
        if path.lower() == 'q':
            break
        else:
            print(organize(path))


if __name__ == '__main__':
    start()
