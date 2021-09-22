import os

def get_path():
    path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return path

if __name__ == '__main__':
    print(get_path())


