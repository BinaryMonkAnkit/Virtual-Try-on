

#Removed frame skipping from third code
import cv2
import numpy as np
import mediapipe as mp
import concurrent.futures

# Initialize Mediapipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Create a ThreadPoolExecutor for parallel processing
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

def process_frame(frame_data, top_garment_image_store):
    try:
        # Downsample the frame for faster processing ( to half the original size)
        np_frame = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)
        small_frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))

        if top_garment_image_store:
            # Get the latest garment image
            garment_image_key = list(top_garment_image_store.keys())[-1]
            garment_image_data = top_garment_image_store[garment_image_key]
            garment_image_array = np.frombuffer(garment_image_data, np.uint8)
            garment_img = cv2.imdecode(garment_image_array, cv2.IMREAD_UNCHANGED)

            # Resize garment to smaller frame size for faster processing
            tshirt_shoulder_width = garment_img.shape[1]

            # Convert the frame to RGB for pose detection
            small_frame_rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            result = pose.process(small_frame_rgb)

            if result and result.pose_landmarks:
                # Extract shoulder and hip landmarks
                left_shoulder = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
                right_shoulder = result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
                left_hip = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
                right_hip = result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]

                # Compute user body dimensions based on small frame size
                user_shoulder_width = int(abs(right_shoulder.x - left_shoulder.x) * small_frame.shape[1])
                user_torso_height = int(abs((left_hip.y + right_hip.y) / 2 * small_frame.shape[0] - left_shoulder.y * small_frame.shape[0]))

                # Calculate garment resizing with padding
                garment_width_with_padding = user_shoulder_width + 100  # Less padding for better speed
                scaling_factor_width = garment_width_with_padding / tshirt_shoulder_width
                scaling_factor_height = user_torso_height / garment_img.shape[0]

                scaling_factor = max(scaling_factor_width, scaling_factor_height)

                # Resize garment image
                garment_height = int(garment_img.shape[0] * scaling_factor)
                garment_width = int(garment_img.shape[1] * scaling_factor)

                # Compute position (center at shoulders)
                mid_shoulder_x = int((left_shoulder.x + right_shoulder.x) / 2 * small_frame.shape[1])
                shoulder_y = int(left_shoulder.y * small_frame.shape[0])
                x = mid_shoulder_x - garment_width // 2
                y = shoulder_y - int(garment_height * 0.15)

                resized_garment = cv2.resize(garment_img, (garment_width, garment_height), interpolation=cv2.INTER_AREA)

                # Overlay garment onto small frame
                small_frame = overlay_image(small_frame, resized_garment, x, y)

        # Upscale the processed small frame back to the original size
        final_frame = cv2.resize(small_frame, (frame.shape[1], frame.shape[0]))

        # Encode the final frame
        # _, buffer = cv2.imencode('.jpg', final_frame)
        # return buffer.tobytes()

        _, buffer = cv2.imencode('.jpg', final_frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
        return buffer.tobytes()

    except Exception as e:
        print(f"Error processing frame: {e}")
        return frame_data  # Return the original frame in case of error


def process_frame_async(frame_data, top_garment_image_store):
    """Run the process_frame function in a separate thread."""
    return executor.submit(process_frame, frame_data, top_garment_image_store)


def overlay_image(background, overlay, x, y):
    """Overlay the garment image onto the background frame."""
    h, w = overlay.shape[:2]

    # Clip overlay to fit inside the background
    if x < 0:
        overlay = overlay[:, abs(x):]
        w = overlay.shape[1]
        x = 0
    if y < 0:
        overlay = overlay[abs(y):, :]
        h = overlay.shape[0]
        y = 0
    if x + w > background.shape[1]:
        overlay = overlay[:, :background.shape[1] - x]
        w = overlay.shape[1]
    if y + h > background.shape[0]:
        overlay = overlay[:background.shape[0] - y, :]
        h = overlay.shape[0]

    alpha = overlay[:, :, 3] / 255.0 if overlay.shape[2] == 4 else np.ones((h, w), dtype=float)

    for c in range(0, 3):
        background[y:y+h, x:x+w, c] = (alpha * overlay[:h, :w, c] +
                                       (1 - alpha) * background[y:y+h, x:x+w, c])

    return background
