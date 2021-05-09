#!/usr/bin/env python3

import imageio
import os, glob

if __name__ == "__main__":
    path = "/home/jetson/SLAM/runbot_custom_localization/frontend/SuperGlue_ROS/results/left"
    imgs = []
    for file in sorted(glob.glob(os.path.join(path, '*.jpg'))):
        print(file)
        im = imageio.imread(file)
        imgs += [im]

    imageio.mimsave("video.mp4", imgs, fps=5)