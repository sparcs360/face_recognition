#!/usr/bin/python3
import os
import cv2

def take_snap(directory, position):

    global video_capture
    while True:

        ret, frame = video_capture.read()
        draw_caption(frame, position)
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):
            print("Click!")
            cv2.imwrite('{}/{}.jpg'.format(directory, position), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            return True
        if key == ord('q'):
            print("Aborting")
            return False

def draw_caption(frame, caption):

    global FONT, WIDTH

    cv2.rectangle(frame, (0, 0), (WIDTH, 40), (255, 0, 0), cv2.FILLED)
    cv2.rectangle(frame, (0, 0), (WIDTH, 40), (255, 255, 255), 2)
    cv2.putText(frame, caption, (3, 34), FONT, 1.0, (255, 255, 255), 1)

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="the name of the person being mugshotted")
    args = parser.parse_args()
    if not args.name:
        print("Specify the name of the person you're mugshotting")
        exit()
    print(args.name)
    
    directory = "knn_examples/train/{}".format(args.name)
    if not os.path.exists(directory):
        os.makedirs(directory)

    video_capture = cv2.VideoCapture(0)

    FONT = cv2.FONT_HERSHEY_DUPLEX
    WIDTH = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))

    if not take_snap(directory, "FULL_LEFT"):
        exit()
    if not take_snap(directory, "HALF_LEFT"):
        exit()
    if not take_snap(directory, "FRONT"):
        exit()
    if not take_snap(directory, "HALF_RIGHT"):
        exit()
    if not take_snap(directory, "FULL_RIGHT"):
        exit()

    video_capture.release()
    cv2.destroyAllWindows()
