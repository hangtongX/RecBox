from enum import Enum


class CDAE(Enum):
    loss_type = 'BCE'  # (str) The loss function of model. Range in [BCE, MSE].
    hid_activation = 'relu'  # (str) The hidden layer activation function. Range in [sigmoid, relu, tanh].
    out_activation = 'sigmoid'  # (str) The output layer activation function. Range in [sigmoid, relu].
    corruption_ratio = 0.5  # (float) The corruption ratio of the input.
    embedding_size = 64  # (int) The embedding size of user.
    reg_weight_1 = 0.  # (float) L1-regularization weight.
    reg_weight_2 = 0.01  # (float) L2-regularization weight.