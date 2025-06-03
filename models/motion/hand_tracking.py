from threading import Thread

import pyautogui
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB, destroyAllWindows, flip, resize
import mediapipe as mp
from .utils import calc_angle, calc_distance, is_right_click, is_left_click
from pyautogui import moveTo
from pynput.mouse import Controller, Button

class HandTracking:
    mouse = Controller()
    mp_hands = mp.solutions.hands
    hand = mp_hands.Hands(
        static_image_mode=False,
        model_complexity= 1,
        min_detection_confidence= 0.7,
        min_tracking_confidence= 0.7,
        max_num_hands= 1
    )

    width, height = pyautogui.size()

    def __init__(self):

        self.running = True
        self.thread = Thread(target=self.main)
        self.thread.start()

    def finger_tip(self, find_hand):
        if find_hand:
            hand_landmark = find_hand[0]
            return hand_landmark.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        return None

    def stop(self):
        self.running = False
        self.thread.join()

    def move_mouse(self, index_finger_tip):
        if index_finger_tip is not None:
            x = int(index_finger_tip.x * self.width)
            y = int(index_finger_tip.y * self.height)
            moveTo(x, y)


    def detect_gesture(self, landmarks_list, find_hand):
        if len(landmarks_list) >=2:

            index_finger_tip = self.finger_tip(find_hand)
            thumb_index_dist = calc_distance(landmarks_list[4], landmarks_list[5])
            angle = calc_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8])
            if thumb_index_dist < 50 and angle > 90:
                self.move_mouse(index_finger_tip)
            elif is_left_click(landmarks_list, thumb_index_dist):
                self.mouse.press(Button.left)
                self.mouse.release(Button.left)
            elif is_right_click(landmarks_list, thumb_index_dist):
                self.mouse.press(Button.right)
                self.mouse.release(Button.right)

    def main(self):
        cap = VideoCapture(0)
        draw = mp.solutions.drawing_utils
        try:
            while cap.isOpened():
                ret, frame = cap.read()

                if not ret:
                    break

                frame = flip(frame, 1)
                frame = resize(frame, (500, 500))
                rgb = cvtColor(frame, COLOR_BGR2RGB)
                landmarks_list = []
                find_hand = self.hand.process(rgb).multi_hand_landmarks

                if find_hand:
                    landmarks = find_hand[0]
                    draw.draw_landmarks(frame, landmarks, self.mp_hands.HAND_CONNECTIONS)

                    for ld in landmarks.landmark:
                        landmarks_list.append((ld.x, ld.y))

                self.detect_gesture(landmarks_list, find_hand)

        finally:
            cap.release()
            destroyAllWindows()