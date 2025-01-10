# 1. Import Required Libraries
    # cv2: OpenCV library, used here for handling video input/output and image processing.
    # mediapipe: A library by Google for machine learning solutions, including pose detection.
import cv2
import mediapipe as mp

# 2. Initialize MediaPipe Pose model
    # mp_pose.Pose: Loads the MediaPipe pose estimation model.
    # static_image_mode=False: Optimized for video input (continuously detecting poses in a video stream).
    # model_complexity=2: Specifies a high-complexity model for better accuracy at the cost of computational speed.
    # smooth_landmarks=True: Enables smoothing of landmarks to make movements appear less jittery.
    # enable_segmentation=True: Enables body segmentation (e.g., distinguishing the subject from the background).
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, model_complexity=2, smooth_landmarks=True, enable_segmentation=True)

# 3. Drawing Utilities
    #   drawing_utils: Contains functions to visualize the detected landmarks on the image.
mp_drawing = mp.solutions.drawing_utils

# 4. Video Capture Setup
    # cv2.VideoCapture(0): Opens the default webcam (device 0).
cap = cv2.VideoCapture(0)  # Use webcam

# 5. Main Loop
    # The loop reads video frames from the webcam until the video source is closed.
    # cap.read(): Captures a single frame.
    # ret: Boolean indicating if the frame was read successfully.
    # frame: The captured image.
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 6. Flip and Convert Frame
        # cv2.flip(frame, 1): Flips the image horizontally for a selfie-view effect.
        # cv2.cvtColor: Converts the image from OpenCV's default BGR color space to RGB, as required by MediaPipe.
        # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 7. Pose Estimation
        # pose.process(): Processes the RGB image and returns detected pose landmarks.
        # Process the frame and get pose landmarks
    results = pose.process(rgb_frame)

    # 8. Draw Landmarks
        # Checks if pose landmarks are detected:
        # results.pose_landmarks: Contains 3D coordinates of detected landmarks if available.
        # draw_landmarks: Draws landmarks and connections (skeleton) on the original frame.
        # If landmarks are detected, draw them on the frame
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 9. Debugging: Print Landmarks
            # Iterates through the detected landmarks:
            # landmark.x, landmark.y, landmark.z: 3D coordinates normalized to the image dimensions.
            # landmark.visibility: Confidence score (how visible the landmark is in the frame).
            # Print the 3D landmarks coordinates (for debugging)
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            print(f"Landmark {idx}: x={landmark.x}, y={landmark.y}, z={landmark.z}, visibility={landmark.visibility}")

    # 10. Display and Exit
        # cv2.imshow: Displays the processed frame with pose landmarks.
        # cv2.waitKey(1): Waits for a key press. If 'q' is pressed, the loop breaks and the program exits.
        # Show the image with pose landmarks
    cv2.imshow("3D Pose Estimation", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 11. Release Resources
    # cap.release(): Releases the webcam.
    # cv2.destroyAllWindows(): Closes all OpenCV windows.
    # Release resources
cap.release()
cv2.destroyAllWindows()


