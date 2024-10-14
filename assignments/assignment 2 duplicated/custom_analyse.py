def analyse_template(booking: Booking) -> dict:
    nationalities: dict = {}
    austria_hotels_reviews: list = []

    for hotels in booking.hotels:
        country: str = hotels.address.split(' ')[-1]
        if country != "Austria":
            continue
        austria_hotels_reviews.extend(hotels.reviews)

    for review in austria_hotels_reviews:
        nationality: str = review.nationality
        if nationality not in nationalities:
            nationalities[nationality] = 0
        nationalities[nationality] += 1

    return dict(sorted(nationalities.items(), key=lambda item: item[1], reverse=True))

def analyse_template_two(booking: Booking) -> dict:

    reviews_per_nationality: dict = {}
    for review in booking.reviews:
        nationality: str = review.nationality
        if nationality not in reviews_per_nationality:
            reviews_per_nationality[nationality] = []
        reviews_per_nationality[nationality].append(review.score)

    for nationality, reviews  in reviews_per_nationality.items():
        reviews_per_nationality[nationality] = statistics.median(reviews)

    return dict(sorted(reviews_per_nationality.items(), key=lambda item: item[1], reverse=True))
