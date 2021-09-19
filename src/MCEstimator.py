import numpy as np


class MCEstimator:

    def __init__(self, samples=None, dist='uniform'):
        np.random.seed(314)
        # if samples are not provided, generate 25000 uniformly distributed samples
        if samples is None:
            self.n_samples = 25000
            samples = self.generate_samples(dist)
        # ... else use the samples provided
        else:
            self.n_samples = np.size(samples, 0)

        self.x_samples = samples[:, 0]
        self.y_samples = samples[:, 1]

    def generate_samples(self, dist='uniform'):
        """This method generates uniformly distributed samples between 0 and 1"""
        if dist == 'uniform':
            return np.random.random_sample((self.n_samples, 2))
        elif dist == 'normal':
            return self.__generate_normal_samples()
        else:
            raise NotImplementedError

    def __generate_normal_samples(self, lb=0, ub=1):
        """Generate normal-distributed samples in the interval [lb, ub]"""
        samples = np.empty([self.n_samples, 2])
        count = 0
        while count < self.n_samples:
            candidate = np.random.default_rng().normal(loc=0.5, scale=.2, size=(2,))
            is_valid = (candidate[0] >= lb) & (candidate[0] <= ub) & (candidate[1] >= lb) & (candidate[1] <= ub)
            if is_valid:
                samples[count, :] = candidate
                count += 1
        return samples

    def samples_inside_circle(self):
        """Calculate how many coords lie within a circle of radius 1 in a square with side length 1."""
        return self.x_samples ** 2 + self.y_samples ** 2 <= 1.0

    def samples_densities(self, n_bins=10):
        """Calculate the sample density/importance. Only supports uniform distribution."""
        return 1

    def pi(self) -> float:
        inside_circle = self.samples_inside_circle()
        sample_densities = self.samples_densities()
        return 4.0 * (inside_circle / sample_densities).mean()
