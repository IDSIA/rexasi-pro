import csv
from scipy.stats import norm

def winkler(gt,mean,sd,n):
	"""
    Calculates the Winkler score for a prediction interval.

    The Winkler score is a metric used to evaluate the quality of a prediction interval
    by penalizing both the width of the interval and whether the true value lies outside it.
	"""
	n = float(n)
	alpha = 1.0 - (norm.cdf(n) - norm.cdf(-n))
	score = 2*n*sd
	if gt > mean + sd:
		score += 2/alpha*(gt-mean-sd)
	elif gt < mean - sd:
		score += 2/alpha*(mean-sd-gt)
	return score

def compute_score(filename,n_of_devs,mean_idx,sd_idx,gt_idx):
	"""
    Computes the total Winkler score over a CSV file containing prediction data.

    This function reads a CSV file row by row and calculates the Winkler score
    for each row (skipping headers or metadata).
    It sums the individual scores to return a total performance metric.
	"""
	with open(filename, newline='') as csvfile:
		file1 = csv.reader(csvfile, delimiter=",")
		k = 0
		totalscore = 0.0
		for row in file1:
			if k>1:
				mean, sd = float(row[mean_idx]),float(row[sd_idx])
				gt = float(row[gt_idx])
				totalscore += winkler(gt,mean,sd,n_of_devs)
			k += 1
	return totalscore

output_filename = "winkler_scores.csv"

# To CSV
with open(output_filename, "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["filename", "sd", "BN_score", "KF_score"])

    for n in [1.0, 2.0, 3.0]:
        for effect in ['original', 'rain_1', 'rain_2', 'fog_1']:
            for i in range(14):
                filebase = f"winkler/data_for_plot_{effect}_exp{i}"
                filename = filebase + ".csv"
                try:
                    bn = compute_score(filename, n, 3, 4, 5)
                    kf = compute_score(filename, n, 11, 12, 5)  
                    filename = filename.replace('winkler/', '')
                    writer.writerow([filename, n, bn, kf])
                except Exception as e:
                    print(f"Errore con file {filename}: {e}")
