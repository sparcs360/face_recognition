#!/usr/bin/python3
import face_recognition

#image = face_recognition.load_image_file("/mnt/c/Users/Lee/OneDrive/Pictures/IMG_20170608_194402702.jpg")
image = face_recognition.load_image_file("./IMG_20170608_194402702.jpg")

face_locations = face_recognition.face_locations(image)
print(face_locations)

face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)
