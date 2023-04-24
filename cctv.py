import cv2
import datetime
import time


# Initialize the camera
cap = cv2.VideoCapture(0)

# Set the camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1050)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

# Set the font and color for date and time display
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 255, 0)  # green color

# Set the timer for 10 seconds
timer = 3600
start_time = time.time()

# Create a VideoWriter object to save the video to a file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    # Capture the frame from the camera
    ret, frame = cap.read()

    # Display the current date and time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.date.today().strftime("%B %d, %Y")
    cv2.putText(frame, current_time, (20, 50), font, 0.45, color, 2, cv2.LINE_AA)
    cv2.putText(frame, current_date, (20, 100), font, 0.45, color, 2, cv2.LINE_AA)

    # Display the timer countdown
    elapsed_time = int(time.time() - start_time)
    time_left = max(timer - elapsed_time, 0)
    cv2.putText(frame, "Timer: {}".format(time_left), (20, 150), font, 0.45, color, 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Camera', frame)

    # Write each frame to the video file
    out.write(frame)

    # Exit the loop after the timer expires
    if elapsed_time >= timer:
        break

    # Wait for a key press
    key = cv2.waitKey(1)

    # Exit the loop if 'q' is pressed
    if key == ord('q'):
        break

# Release the camera and close the window
cap.release()
out.release()
cv2.destroyAllWindows()
