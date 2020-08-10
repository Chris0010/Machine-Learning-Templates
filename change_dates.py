import pandas as pd
import numpy as np
import datetime, glob, os

# func to pull out each .csv in a given folder
def files(folder = os.getcwd()):
	for file in glob.glob(folder + "/*.csv"):
		yield file

# func to transform the unix epoch datetime objects into human readable datetime and return new .csv 
def correctedDate(folder = 'folder', cols = []):
	csv = files(folder)
	for file in csv:
		df = pd.read_csv(file, header = 0)
		for col in cols:
			# replace the NaN values with zero so the column can be changed to dates
			df[col] = df[col].replace(np.nan, 0)
			lst = []
			for x in df[col]:
				timestamp = datetime.datetime.fromtimestamp(int(x))
				lst.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
			df[col] = lst
			# the 0's that were NaN were changed to the below date, this changes that to the below statement instead
			df[col] = df[col].replace('1969-12-31 19:00:00', "No Date Given")
		df.to_csv(file)




if __name__ == "__main__":
	correctedDate()
