import os
import shutil

def main():

    print('H:/Emulation/Nintendo Entertainment System')
    filePath = input("Enter the directory to move files up to: (E to exit)  ")
    if filePath is not 'E':
        for root, dirs, files in os.walk(filePath, topdown=False):
            for file in files:
                try:
                    shutil.move(os.path.join(root, file), filePath)
                except OSError:
                    pass


if __name__ == '__main__':
    main()
