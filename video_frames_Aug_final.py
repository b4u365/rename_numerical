import cv2
import os


def split_video_into_frames(video_path, output_dir):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not video.isOpened():
        print(f"Error opening video file: {video_path}")
        return

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    frame_count = 0

    # Read the video frame by frame
    while True:
        # Read the current frame
        ret, frame = video.read()

        # If there are no more frames, break out of the loop
        if not ret:
            break

        # Save the frame as an image file
        frame_path = os.path.join(output_dir, f"{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        frame_count += 1

    # Release the video object
    video.release()

    print(f"Video frames saved in: {output_dir}")


# Example usage
video_path = r'C:\Users\soma3420\Desktop\data_collection\logitech\rgb\6.avi'
output_dir = r'C:\Users\soma3420\Desktop\data_collection\logitech\rgb\rgb_6'
split_video_into_frames(video_path, output_dir)