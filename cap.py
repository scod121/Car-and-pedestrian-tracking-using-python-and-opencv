# import cv2

# # our image
# img_file = 'images.jpg'

# # our pre-trained classifier
# classifier_file = 'cars.xml'

# # create opencv image
# img = cv2.imread(img_file)

# # convert to grayscale (needed for haar cascade)
# black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # create car classifier
# car_tracker = cv2.CascadeClassifier(classifier_file)

# # detect cars
# cars = car_tracker.detectMultiScale(black_n_white)
# print(cars)

# # draw rectangle around the cars
# for (x, y, z, w) in cars:
#     cv2.rectangle(img, (x, y), (x+w, y+z), (0, 0, 255), 2)

# # display the image with the faces spotted
# cv2.imshow('Clever Programmer Car Detector', img)

# # don't auto closed (wait here in the code and listen for a key press)
# cv2.waitKey()



# print("code competed")




import cv2
# load some pre-trained data on car rear ends (haar cascade algorithm)
car_tracker = cv2.CascadeClassifier('cars.xml')
pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# get car footage
video= cv2.VideoCapture('india.mp4')

# itrate forever over frames
while True:
    # read the current frame
    read_successful, frame = video.read()

    # safe codes
    if read_successful:
        # must convert to greyscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect cars
    cars = car_tracker.detectMultiScale(grayscaled_frame)#, scaleFactor = 1.1, minNeighbors=2)

    # detect pedestrians
    pedestrains = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    # Draw rectangles around the cars
    for (x, y, z, w) in cars:
        cv2.rectangle(frame, (x, y), (x+z, y+w), (0, 0, 255), 2)

    # Draw rectangles around the pedestrains
    for (x, y, z, w) in pedestrains:
        cv2.rectangle(frame, (x, y), (x+z, y+w), (0, 255, 255), 2)

    #cv2.startWindowThread()
    #cv2.namedWindow("preview")
    #cv2.imshow("preview", frame)

    # display the image with the faces spotted
    cv2.imshow('Clever Programmer Car Detector', frame)

    # don't auto closed (wait here in the code and listen for a key press)
    cv2.waitKey(1)

