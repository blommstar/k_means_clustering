import math


def pearson(object1, object2):
	correlation = {}
	for word in object1:
		if word in object2:
				correlation[word]

		n = len(correlation)
		
		if(n == 0):
				return 0

		# Calc som of scores
		sum1 = sum([object1[item] for item in correlation])
		sum2 = sum([object2[item] for item in correlation])

		# Squared
		sumSq1 = sum([pow(object1[item], 2) for item in correlation])
		sumSq2 = sum([pow(object2[item], 2) for item in correlation])

		# Sum of squared
		sumPr = sum([object1[item] * object2[item]
									for item in correlation])

		# calculating pearson score
		num = sumPr - (sum1*sum2)/n
		den = math.sqrt(abs(sumSq1 - pow(sum1, 2)/n)
										* abs(sumSq2 - pow(sum1, 2)/n))
		if(den == 0):
				return 0

		return num/den
