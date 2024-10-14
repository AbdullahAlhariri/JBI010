def check_improvement(hotels: list[Hotel]) -> dict[str, tuple]:
    """
    Checks every hotel given as param if it's reviews score in the second half has been improved compared to the first one by taking the mean. And returning the results.

    :param hotels: Hotels where checks for improvements will be done as list[Hotel].
    :returns: Returns a dict with hotel name(str) as key and first and second half mean and whether the second half has been an improvements over the fist one all as a value (tuple).
    """
    output_dict: dict = {}
    for hotel in hotels:
        reviews: list = sorted(hotel.reviews, key=lambda review: review.days_rev, reverse=True)
        half_point = round(len(reviews) / 2)

        reviews_first_half_scores = [review.score for review in reviews[:half_point]]
        reviews_second_half_scores = [review.score for review in reviews[half_point:]]
        reviews_first_half_mean = statistics.mean(reviews_first_half_scores)
        reviews_second_half_mean = statistics.mean(reviews_second_half_scores)

        if reviews_first_half_mean < reviews_second_half_mean:
            hotel.improved = True

        output_dict[hotel.name] = (reviews_first_half_mean, reviews_second_half_mean, hotel.improved)

    return output_dict