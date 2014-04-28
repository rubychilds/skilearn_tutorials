from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

# Esitimator - object that learns from data/ Can be classification, regression, clustering
# looks like the following:
class Estimator(object):

	def fit(self, X, Y=None):
		# sets state of self
		return self

	def predict(self, X):
		# sets predication values
		return pred # returns 2-dim array (n_samples, n_classes)

class Transformer(Estimator): # class to transform inpuut data eg. selects subset of features or extracts new features based on initial

	def transform(self, X):
		# transforms input data
		return X_prime

	def fit(self, X):

		return X_fit

	# doesn't tend to include a predict method, only in a few cases

def linearRegressionExample(X, Y):
	# fit-intercept defines if we should fit an intrecpt term or not
	est = LinearRegression(fit_intercept=False)
	#fit the data
	est.fit(X,Y)
	# get coefficients
	est.coef_

def transformExample(X):
	# scaler method
	scaler = StandardScaler(copy=True)
	X_centered = scaler.fit(X).transform(X)
	scaler.mean_ # mean subtracted from transform

def main():
	
	# create random data
	X = np.random.rand(10,2)
	Y = np.random.rand(2,size=10)
	
	linearRegressionExample(X,Y)
	transformExample(X)

	


if __name__ == '__main__':
	main()


