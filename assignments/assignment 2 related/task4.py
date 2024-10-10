def perform_eda(self) -> dict[str,list]:
    """
    Performing exploratory data analysis on booking reviews and returning the results.

    :returns: The mean, median, and std computed of all the neg_words, pos_words, score, and days_rev attributes of review class.
    """
    neg_words = [review.neg_words for review in self.reviews]
    pos_words = [review.pos_words for review in self.reviews]
    score = [review.score for review in self.reviews]
    days_rev = [review.days_rev for review in self.reviews]

    output_dict: dict[str,list] = {
        "neg_words": [len(neg_words), {
            "mean": round(statistics.mean(neg_words), 2),
            "median": round(statistics.median(neg_words), 2),
            "std": round(statistics.stdev(neg_words), 2)
        }],
        "pos_words": [len(pos_words), {
            "mean": round(statistics.mean(pos_words), 2),
            "median": round(statistics.median(pos_words), 2),
            "std": round(statistics.stdev(pos_words), 2)
        }],
        "score": [len(score), {
            "mean": round(statistics.mean(score), 2),
            "median": round(statistics.median(score), 2),
            "std": round(statistics.stdev(score), 2)
        }],
        "days_rev": [len(days_rev), {
            "mean": round(statistics.mean(days_rev), 2),
            "median": round(statistics.median(days_rev), 2),
            "std": round(statistics.stdev(days_rev), 2)
        }],
    }

    return output_dict

Booking.perform_eda = perform_eda