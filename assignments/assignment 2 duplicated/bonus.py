def get_top_and_bottom(hotels: list[Hotel], sorting_order: bool) -> list[tuple[str, float]]:
    """
    Computes the top and bottom 10 hotels based on the review scores mean of the hotels, and returns the top 10 or the bottom 10 based on sorting_order param.

    :param sorting_order: If True, returns bottom 10 hotels else top 10 hotels.
    :returns: Returns a list of tuple with the hotel name(string) as first entry and review scores(float) as second entry.
    """
    hotel_m_scores: list = []

    for hotel in hotels:
        review_scores = [review.score for review in hotel.reviews]
        mean_score = round(statistics.median(review_scores), 1)
        hotel_m_scores.append((hotel.name, mean_score))

    hotel_m_scores_sorted = sorted(hotel_m_scores, key=lambda hotel_m_score: hotel_m_score[1], reverse=True)
    top_10 = hotel_m_scores_sorted[:10]
    bottom_10 = hotel_m_scores_sorted[-10:]

    return bottom_10 if sorting_order else top_10