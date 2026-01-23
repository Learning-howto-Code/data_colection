import cv2
import os
import argparse

def extract_frames(video_path, output_folder, step=1):
    try:
        os.makedirs(output_folder, exist_ok=True)
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        saved_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % step == 0:
                filename = os.path.join(output_folder, f"frame_{saved_count:05d}.jpg")
                cv2.imwrite(filename, frame)
                saved_count += 1
            frame_count += 1

        cap.release()
        print(f"Saved {saved_count} frames to {output_folder}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--step", type=int, default=1)
    args = parser.parse_args()

    extract_frames(args.input, args.output, args.step)
