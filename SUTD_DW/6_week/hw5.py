def process_scores(f):
    scores = f.readlines()
    scores,sum = scores[0].split(),0.0
    for i in scores:
        sum += float(i)
    return sum,sum / len(scores)