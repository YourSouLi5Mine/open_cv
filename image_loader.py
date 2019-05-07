import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-p", required = True, help = "Path to the directory containing the images")
args = vars(ap.parse_args())

for x in range(0, 13):
    path = args["p"] + str(x) + ".jpg"
    image = cv2.imread(path)
    output = "processed_images/" + str(x+100) + ".jpg"
    print("Input image: " + path)
    print("width: {} pixels".format(image.shape[1]))
    print("height: {} pixels".format(image.shape[0]))
    print("channels: {}".format(image.shape[2]))
    print("Output image: " + output)
    print("===================")
    cv2.imshow("image",image)
    cv2.imwrite(output,image)
    cv2.waitKey(25)
