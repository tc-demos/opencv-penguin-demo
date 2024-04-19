from funcs import *


def main():
    lfuncs = [
        {"title": "EXIT", "fn": None},
        {"title": "Basic test", "fn": testFn},
        {"title": "Test image display", "fn": testImageDisplay},
        {"title": "Image as an array", "fn": imageAsAnArray},
        {"title": "Image reading modes", "fn": imageReading},
        {"title": "Grayscale image from rand bytes", "fn": rawBytes},
        {"title": "Color image from random bytes", "fn": rawBytesColor},
        {"title": "Image as an array", "fn": imageAsAnArray2},
        {"title": "Region of interest", "fn": regionOfInterest},
    ]

    while True:
        print(f"\n{'-' * 15}Action Menu{'-' * 15}")
        for i in range(len(lfuncs)):
            print(i, lfuncs[i]["title"])
        print()

        choice = -1

        while choice < 0 or choice >= len(lfuncs):
            msg = f"Enter your choice (0-{str(len(lfuncs) - 1)}): "
            choice = int(input(msg))

        print()

        if choice != 0:
            lfuncs[choice]["fn"]()
        else:
            break


if __name__ == '__main__':
    main()
