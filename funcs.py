import cv2
import numpy as np
import os


def testFn():
    print("from testFun()")


def testImageDisplay():
    image = cv2.imread("penguins.jpg")
    cv2.imshow("Penguins", image)
    print("close image to exit function")
    cv2.waitKey(0)


def imageAsAnArray():
    image = np.zeros((5, 4), dtype=np.uint8)
    print("5x4 array of uint8, all = 0")
    print(image)
    print("The shape of this image: ", image.shape)

    print("\nNow convert this to a color img")
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    print(image)
    print("The shape of this image: ", image.shape)


def imageReading():
    image = cv2.imread("Penguins.jpg")
    cv2.imshow('default', image)
    print("Default read mode. Close image to continue.")
    cv2.waitKey(0)
    modes = {
        'IMREAD_COLOR': cv2.IMREAD_COLOR,
        'IMREAD_ANYCOLOR': cv2.IMREAD_ANYCOLOR,
        'IMREAD_GRAYSCALE': cv2.IMREAD_GRAYSCALE,
        'IMREAD_ANYDEPTH': cv2.IMREAD_ANYDEPTH,
        'IMREAD_ANYDEPTH | IMREAD_COLOR': cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR,
        'IMREAD_REDUCED_GRAYSCALE_2': cv2.IMREAD_REDUCED_GRAYSCALE_2,
        'IMREAD_REDUCED_COLOR_2': cv2.IMREAD_REDUCED_COLOR_2,
        'IMREAD_REDUCED_GRAYSCALE_4': cv2.IMREAD_REDUCED_GRAYSCALE_4,
        'IMREAD_REDUCED_COLOR_4': cv2.IMREAD_REDUCED_COLOR_4,
        'IMREAD_REDUCED_GRAYSCALE_8': cv2.IMREAD_REDUCED_GRAYSCALE_8,
        'IMREAD_REDUCED_COLOR_8': cv2.IMREAD_REDUCED_COLOR_8
    }

    for modeKey in modes.keys():
        image = cv2.imread('Penguins.jpg', modes[modeKey])
        cv2.imshow(modeKey, image)
        print(modeKey, image)
        print(modeKey, 'read mode. Close image to continue.')
        cv2.waitKey(0)


def rawBytes():
    height = 300
    width = 400

    choice = -1
    while choice != 0:
        choice = -1
        while choice < 0 or choice > 6:
            print('Enter choice of operation:')
            print('1: zero pixels in lower half of image')
            print('2: zero pixels in right half of image')
            print('3: zero pixels in upper right corner of image')
            print('4: zero pixels in central circular region of image')
            print('5: zero pixels on border of image')
            print('6: zero pixels in central rectangular region of image')
            print('0: quit')
            schoice = input('')
            choice = int(schoice)

        randomByteArray = bytearray(os.urandom(height * width))

        if choice == 1:
            for i in range(height * width // 2, height * width):
                randomByteArray[i] = 0

        elif choice == 2:
            for i in range(height * width):
                row = i // width
                col = i % width
                if col >= width // 2:
                    randomByteArray[i] = 0

        elif choice == 3:
            for i in range(height * width):
                row = i // width
                col = i % width
                if row < col:
                    randomByteArray[i] = 0

        elif choice == 4:
            for i in range(height * width):
                row = i // width
                col = i % width
                ccenter = width // 2
                rcenter = height // 2
                radius = min(height, width) // 4
                if (row - rcenter) ** 2 + (col - ccenter) ** 2 < radius ** 2:
                    randomByteArray[i] = 0

        elif choice == 5:
            for i in range(height * width):
                row = i // width
                col = i % width
                border = 50
                if row < border or row > (height - border) \
                        or col < border or col > (width - border):
                    randomByteArray[i] = 0

        elif choice == 6:
            for i in range(height * width):
                row = i // width
                col = i % width
                border = 50
                if border <= row <= (height - border) \
                        and border <= col <= (width - border):
                    randomByteArray[i] = 0

        else:
            continue

        flatNumpyArray = np.array(randomByteArray)

        grayImage = flatNumpyArray.reshape(height, width)
        cv2.imshow('grayscale', grayImage)
        cv2.waitKey(0)


def rawBytesColor():
    options = [
        '1: Zero pixels in lower half',
        '2: Zero pixels in right half',
        '3: Zero pixels in upper right',
        '4: Zero pixels in central circle',
        '5: Zero pixels on border',
        '6: Zero pixels in central rectangle',
        '7: Zero red in bottom half',
        '8: Zero green in bottom half',
        '9: Zero blue in bottom half',
    ]
    numOps = len(options)

    height = 300
    width = 400

    choice = -1

    while choice != 0:
        choice = -1

        while choice < 0 or choice > numOps:
            print('Enter choice:')
            for i in range(numOps):
                print(options[i])
            print('0: Quit')
            schoice = input('')
            choice = int(schoice)

            randomByteArray = bytearray(os.urandom(height * width * 3))

            if choice == 1:
                for i in range(height * width * 3):
                    row = i // 3 // width
                    col = (i // 3) % width
                    if row >= height // 2:
                        randomByteArray[i] = 0

            elif choice == 2:
                for i in range(height * width * 3):
                    row = i // 3 // width
                    col = (i // 3) % width
                    if col >= width // 2:
                        randomByteArray[i] = 0

            elif choice == 3:
                for i in range(height * width * 3):
                    row = i // 3 // width
                    col = (i // 3) % width
                    if row < col:
                        randomByteArray[i] = 0

            elif choice == 4:
                for i in range(height * width * 3):
                    row = i // 3 // width
                    col = (i // 3) % width
                    c_center = width // 2
                    r_center = height // 2
                    radius = min(height, width) // 4

                    if (row - r_center) ** 2 + (col - c_center) ** 2 < radius ** 2:
                        randomByteArray[i] = 0

            elif choice == 5:

                for i in range(height * width * 3):
                    row = i // 3 // width
                    col = (i // 3) % width
                    border = 50
                    if row < border or row > (height - border) \
                            or col < border or col > (width - border):
                        randomByteArray[i] = 0

            elif choice == 6:

                for i in range(height * width * 3):
                    row = i // 3 // width
                    col = (i // 3) % width
                    border = 50
                    if border <= row <= (height - border) \
                            and border <= col <= (width - border):
                        randomByteArray[i] = 0

            elif choice == 7 or choice == 8 or choice == 9:

                for i in range(height * width * 3):
                    row = i // 3 // width
                    col = (i // 3) % width
                    if row >= height // 2:
                        if choice == 7:
                            if i % 3 == 2:
                                randomByteArray[i] = 0
                        elif choice == 8:
                            if i % 3 == 1:
                                randomByteArray[i] = 0
                        elif choice == 9:
                            if i % 3 == 0:
                                randomByteArray[i] = 0
            else:
                continue

            flatNumpyArray = np.array(randomByteArray)

            image = flatNumpyArray.reshape(height, width, 3)
            cv2.imshow('color', image)
            cv2.waitKey(0)


def regionOfInterest():
    image = cv2.imread('penguins.jpg')
    cv2.imshow('Penguins', image)
    print("Starting image. Close image to Continue")
    cv2.waitKey(0)

    (height, width, planes) = image.shape

    xmin = width
    xmax = 0
    ymin = height
    ymax = 0
    print("A region of interest will be defined.")
    while xmin < 0 or xmin >=width:
        msg = "Enter x_min (0-"+str(width-1)+"): "
        xmin = int(input(msg))
    while xmax < xmin or xmax >= width:
        msg = "Enter x_max ("+str(xmin)+"-"+str(width-1)+"): "
        xmax = int(input(msg))
    while ymin < 0 or ymin >= height:
        msg = "Enter y_min (0-"+str(height-1)+"): "
        ymin = int(input(msg))
    while ymax < ymin or ymax >= height:
        msg = "Enter y_max ("+str(ymin)+"-"+str(height-1)+"): "
        ymax = int(input(msg))

    roi = image[ymin:ymax+1, xmin:xmax+1]

    for i in range(xmin, xmax+1):
        image[ymin,i] = [0,0,255]
        image[ymax,i] = [0,0,255]

    for i in range(ymin, ymax+1):
        image[i,xmin] = [0,0,255]
        image[i,xmax] = [0,0,255]

    cv2.imshow('Penguins with ROI', image)
    print("Region of interest. Close image to continue.")
    cv2.waitKey(0)

    cv2.imshow('ROI extracted', roi)
    print("Extracted region of interest. Close image to continue.")
    cv2.waitKey(0)


def imageAsAnArray2():
    image = cv2.imread('Penguins.jpg')
    cv2.imshow('Penguins', image)
    print("Starting image. Close image to continue.")
    cv2.waitKey(0)

    (height, width, planes) = image.shape

    print("Some pixels will be set to white.")
    xPitch = int(input("Enter horizontal spacing of white pixels: "))
    yPitch = int(input("Enter vertical spacing of white pixels: "))
    for i in range(0, height, yPitch):
        for j in range(0, width, xPitch):
            image[i, j] = [255, 255, 255]
    cv2.imshow('white pixels', image)
    print("Some white pixels. Close image to continue.")
    cv2.waitKey(0)

    print("Some pixels will be set to black.")
    xPitch = int(input("Enter horizontal spacing of black pixels: "))
    yPitch = int(input("Enter vertical spacing of black pixels: "))
    for i in range(0, height, yPitch):
        for j in range(0, width, xPitch):
            image[i, j] = [0, 0, 0]
    cv2.imshow('white and black pixels', image)
    print("Some white and black pixels. Close image to continue.")
    cv2.waitKey(0)

    image = cv2.imread('Penguins.jpg')
    cv2.imshow('Penguins', image)
    print("Starting image. Close image to continue.")
    cv2.waitKey(0)

    print("Red, green, and blue gain will be adjusted.")
    redGain = 0
    while redGain < 0.1 or redGain > 10.0:
        redGain = float(input("Enter red gain (0.1 - 10.0): "))
    grnGain = 0
    while grnGain < 0.1 or grnGain > 10.0:
        grnGain = float(input("Enter green gain (0.1 - 10.0): "))
    bluGain = 0
    while bluGain < 0.1 or bluGain > 10.0:
        bluGain = float(input("Enter blue gain (0.1 - 10.0): "))

    for i in range(height):
        for j in range(width):
            newRed = min(255, image.item(i, j, 2) * redGain)
            newGrn = min(255, image.item(i, j, 1) * grnGain)
            newBlu = min(255, image.item(i, j, 0) * bluGain)
            image.itemset((i, j, 2), newRed)
            image.itemset((i, j, 1), newGrn)
            image.itemset((i, j, 0), newBlu)
    cv2.imshow('Gain modified', image)
    print("Gain modified penguins. Close image to continue.")
    cv2.waitKey(0)