import numpy as np


class MNIST_RNN:
    def __init__(self, input_dim=28, hidden_dim=64, output_dim=10):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim

        self.W_xh = np.random.randn(hidden_dim, input_dim) * 0.05
        self.W_hh = np.random.randn(hidden_dim, hidden_dim) * 0.05
        self.b_h = np.zeros((hidden_dim, 1))

        self.W_hy = np.random.randn(output_dim, hidden_dim) * 0.05
        self.b_y = np.zeros((output_dim, 1))

    def forward(self, x_seq):
        T = x_seq.shape[0]
        h = {}
        h[-1] = np.zeros((self.hidden_dim, 1))

        for t in range(T):
            xt = x_seq[t].reshape(-1, 1)  # (28, 1)
            # h_t = tanh(W_xh * x_t + W_hh * h_{t-1} + b_h)
            h[t] = np.tanh(
                np.dot(self.W_xh, xt) + np.dot(self.W_hh, h[t - 1]) + self.b_h
            )

        logits = np.dot(self.W_hy, h[T - 1]) + self.b_y

        exp_logits = np.exp(logits - np.max(logits))
        probs = exp_logits / np.sum(exp_logits)

        return probs, h

    def backward(self, x_seq, h, probs, label):
        T = x_seq.shape[0]
        dW_xh = np.zeros_like(self.W_xh)
        dW_hh = np.zeros_like(self.W_hh)
        db_h = np.zeros_like(self.b_h)

        dz = probs.copy()
        dz[label] -= 1.0  # (10, 1)

        dW_hy = np.dot(dz, h[T - 1].T)
        db_y = dz.copy()

        dh_next = np.dot(self.W_hy.T, dz)

        for t in reversed(range(T)):
            xt = x_seq[t].reshape(-1, 1)
            dtanh = (1.0 - h[t] ** 2) * dh_next

            dW_xh += np.dot(dtanh, xt.T)
            dW_hh += np.dot(dtanh, h[t - 1].T)
            db_h += dtanh

            dh_next = np.dot(self.W_hh.T, dtanh)

        for grad in [dW_xh, dW_hh, db_h, dW_hy, db_y]:
            np.clip(grad, -1.0, 1.0, out=grad)

        return dW_xh, dW_hh, db_h, dW_hy, db_y

    def train_step(self, x_seq, label, lr=0.01):
        probs, h = self.forward(x_seq)
        loss = -np.log(probs[label, 0] + 1e-12)
        grads = self.backward(x_seq, h, probs, label)

        dW_xh, dW_hh, db_h, dW_hy, db_y = grads
        self.W_xh -= lr * dW_xh
        self.W_hh -= lr * dW_hh
        self.b_h -= lr * db_h
        self.W_hy -= lr * dW_hy
        self.b_y -= lr * db_y

        pred = np.argmax(probs)
        return loss, (pred == label)
