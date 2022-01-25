from tqdm import tqdm
import cv2
import os


def split_video(source_path, output_path=os.path.join(os.getcwd(), 'frames')):
    capture = cv2.VideoCapture(source_path)

    num_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in tqdm(range(num_frames), desc="Writing frames ", unit=' frames'):
        success, frame = capture.read()
        if success:
            framename = "frame_%s.jpg" % i
            path = os.path.join(output_path, framename)
            cv2.imwrite(path, frame)

    capture.release()


if __name__ == "__main__":
    print("starting with video splitting")
    split_video(os.path.join(os.getcwd(), 'IMG_5217.MOV'))
    print("finished splitting, find the frames here: %s" % os.path.join(os.getcwd(), 'frames'))
