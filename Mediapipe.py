import json
import math
import cv2
import array as arr
import mediapipe as mp
import _json
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

brojac =0

def calcSometing(path):
 IMAGE_FILES = [path]
 with mp_pose.Pose(
    static_image_mode=True,
    model_complexity=2,
    min_detection_confidence=0.5) as pose:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    image_height, image_width, _ = image.shape
    # Convert the BGR image to RGB before processing.
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    #if not results.pose_landmarks:
     # continue
    pose_landmarks = results.pose_landmarks
    if pose_landmarks is not None:

      assert len(pose_landmarks.landmark) == 33, 'Unexpected number of predicted pose landmarks: {}'.format(
          len(pose_landmarks.landmark))
      points = pose_landmarks.landmark

      x_data = []
      y_data = []
      z_data = []

      #return [x_data, y_data, z_data]
      for i in range(len(points)):
          # j = i + 1
          j = i
          if (j == 0  or j >= 11 and j <= 12 or j >= 13 and j <= 14 or j >= 15 and j <= 16):
              x_data.append(points[i].x)
              y_data.append(points[i].y)
              z_data.append(points[i].z)


              numbers_list = [195,81,147,169,277,192]
              numbers_array = arr.array('i', numbers_list)
              print(numbers_list[1])

              i += 1

    # Draw pose landmarks on the image.
    annotated_image = image.copy()
    mp_drawing.draw_landmarks(
       annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imwrite(str(brojac) + str(idx) + '.jpg', annotated_image)
    #print(results.pose_landmarks)




    #cv2.imwrite(str(indx) + '.jpg',annotated_image )

    # Plot pose world landmarks.
    #mp_drawing.plot_landmarks(
     #   results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)



    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow('MediaPipe Pose', image)




def concat0(i):
    fullName = str(i)
    return fullName.zfill(6)

#f = open('Portfolio2.json', "r")

f = open('database.json', "r")
data = json.load(f)
#for i in data['frames']:
#   brojac += 1
#   directory = r'C:\Users\fesb4920\PycharmProjects\zed-lab\project-usporedba\GT_frames\-osma2n86oA'
#   calcSometing(directory + r'\frame_' + concat0(i) + '.jpg')
#   print((directory + r'\frame_' + concat0(i) + '.jpg'))

# Analiziramo i-th video
for video in data:
    print("_______________________________")
    directory = r'C:\Users\fesb4920\PycharmProjects\zed-lab\project-usporedba\GT_frames' + "\\" + video["videoname"]

    video["media_locs"] = []
    video["media_locs"][0] = []
    video["media_locs"][1] = []


    for frameIndex in range(0, len(video["frameids"])):
        framepath = directory + r'\frame_' + concat0(video["frameids"][frameIndex]) + '.jpg'

        media_locs = calcSometing(framepath)

        video["media_locs"][0].push(media_locs[0])
        video["media_locs"][1].push(media_locs[1])
        video["media_locs"][2].push(media_locs[2])




        for locPos in range(0, len(video["label_names"])):
            print(video["label_names"][locPos])
            print("X")
            print(video["locs"][0][locPos][frameIndex])
            print("Y")
            print(video["locs"][1][locPos][frameIndex])


cv2.waitKey(0)

