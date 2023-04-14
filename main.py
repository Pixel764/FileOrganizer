from organizer import Organizer


def start():
    while True:
        path = str(input('Full path: '))
        if path.lower() == 'q':
            break
        else:
            org = Organizer(path)
            org.organize()
            print(org.errors_logs)


if __name__ == '__main__':
    start()
