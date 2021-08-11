# VINS-Fusion based SLAM with tightly-coupled wheel odometry and DNN based front-end
Localization package for outdoor delivery robot [[Skoltech](https://www.skoltech.ru/) ISR Lab project]

## DNN based front-end

Deep neural network-based front-end and offline optimization thread were implemented in the package. The architecture of the proposed system is shown below:

![](/media/DNN_opt_thred.png)

SLAM front-end is based on two state-of-the-art feature extraction and matching DNN architectures: SuperPoint and SuperGlue. SuperPoint and SuperGlue neural networks on NVIDIA Jetson AGX Xavier had 1.13 seconds mean forward pass time. Therefore DNN based front-end was utilized in an offline manner. The agent's position was estimated in the parallel thread.

## Graph based back-end

Tightly-coupled wheel odometry preintegration approach is proposed, which adds additional factors into the optimization pose estimation problem and improves pose estimation accuracy. System architecture:

![](/media/Architecture_VINS.png)
