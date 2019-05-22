import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_name", )
parser.add_argument("-ww", "--width", type=int, default = 640)
parser.add_argument("-hh", "--height", type=int, default = 480)
args = parser.parse_args()

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(args.file_name,fourcc, 20.0, (args.width,args.height))
print("Press 'q' to quit")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
