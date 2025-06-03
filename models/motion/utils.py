import numpy as np

def calc_angle(a, b, c):
    angle = np.arctan2(c[1]-b[1], c[0]-b[0]) -np.arctan2(a[1]-b[1], a[0]-b[0])
    return np.abs(np.degrees(angle))

def calc_distance(*landmark_list):
    if len(landmark_list) < 2:
        return
    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]
    disatance = np.hypot(x2-x1, y2-y1)
    return np.interp(disatance, [0, 1], [0, 1000])

def is_right_click(landmarks_list, thumb_ring_dist):
    return(
            calc_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 90 < calc_angle(landmarks_list[5],
                                                                                                    landmarks_list[6],
                                                                                                    landmarks_list[8]) and
            thumb_ring_dist > 50
    )


def is_left_click(landmarks_list, thumb_ring_dist):
    return (
            calc_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 90 < calc_angle(landmarks_list[9],
                                                                                                  landmarks_list[10],
                                                                                                  landmarks_list[
                                                                                                      12]) and
            thumb_ring_dist > 50
    )