def check_improvement(hotels: list[Hotel]) -> dict[str, tuple]:
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