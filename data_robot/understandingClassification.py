import pandas as pd

def main():
	df = pd.read_csv()

	indices = np.where(df.default == "NO")[0]
	# downsize negative cases
	rng = np.random.RandomState(13)
	rng.shuffle(indices)
	n_pos = (df.default == 'YES').sum()
	df = df.drop(df.index[indices[n_pos:]])
	df.head()


if __name__ == '__main__':
	main()