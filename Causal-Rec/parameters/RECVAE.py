from enum import Enum


class RECVAE(Enum):
    hidden_dimension = 600  # (int) The hidden dimension of auto-encoder.
    latent_dimension = 128  # (int) The latent dimension of auto-encoder.
    dropout_prob = 0.5  # (float) The drop out probability of input.
    beta = 0.2  # (float) The default hyperparameter of the weight of KL loss.
    gamma = 0.005  # (float) The hyper-parameter shared across all users.
    mixture_weights = [0.15, 0.75, 0.1]  # (list of float) The mixture weights of three composite priors.
    n_enc_epochs = 3  # (int) The training times of encoder per epoch.
    n_dec_epochs = 1  # (int) The training times of decoder per epoch.
    encoder_flag = True