import cv2
import mediapipe as mp

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, model_complexity=2, smooth_landmarks=True, enable_segmentation=True)

mp_drawing = mp.solutions.drawing_utils

# Load the image or video
cap = cv2.VideoCapture(0)  # Use webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get pose landmarks
    results = pose.process(rgb_frame)

    # If landmarks are detected, draw them on the frame
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Print the 3D landmarks coordinates (for debugging)
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            print(f"Landmark {idx}: x={landmark.x}, y={landmark.y}, z={landmark.z}, visibility={landmark.visibility}")

    # Show the image with pose landmarks
    cv2.imshow("3D Pose Estimation", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

