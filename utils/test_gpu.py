import tensorflow as tf
import torch
import os

# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
print('Tensorflow GPU:', tf.test.is_gpu_available())
print('Pytorch GPU:', torch.cuda.is_available())
