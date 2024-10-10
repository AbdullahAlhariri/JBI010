# For the reason description of the chosen analyses, we refer you to the report
# We made two analyses instead of one :)

def average_score_per_country(booking: Booking) -> dict[str, float]:
    """
    Find the average score per country where the hotel is based and returns them.

    :param booking: Booking instance where the dataset has been loaded.
    :returns: Average score per country where the hotel is based as a dictionary.

    >>> booking = Booking([], [])
    >>> booking.read_csv("data/Hotel_Reviews_EU.csv")
    >>> average_score_per_country(booking)
    {'Netherlands': 8.41, 'France': 8.49, 'Spain': 8.5, 'Italy': 8.32, 'Austria': 8.55, 'United Kingdom': 8.46}

    >>> booking = Booking([], [])
    >>> booking.read_csv("data/Hotel_Reviews_EU_minimal.csv")
    >>> average_score_per_country(booking)
    {'Netherlands': 7.7, 'United Kingdom': 8.47}
    """
    reviews_per_country: dict = {}
    for hotel in booking.hotels:
        country: str = hotel.address.split(' ')[-1]
        if country not in reviews_per_country:
            reviews_per_country[country] = []

        (reviews_per_country[country].append(hotel.av_score))

    for country, reviews in reviews_per_country.items():
        reviews_per_country[country] = round(statistics.mean(reviews), 2)

    # Fixing for United Kingdom
    if 'Kingdom' in reviews_per_country:
        reviews_per_country['United Kingdom'] = reviews_per_country['Kingdom']
        del reviews_per_country['Kingdom']

    return reviews_per_country

# Extra analyse
def highest_nationalities_average_score(booking: Booking):
    """
    Determines the nationalities that gives the highest scores and returning them as string.

    :param booking: Booking instance where the dataset has been loaded.
    :returns: Highest nationalities average score as string.

    >>> booking = Booking([], [])
    >>> booking.read_csv("data/Hotel_Reviews_EU.csv")
    >>> highest_nationalities_average_score(booking)
    All the following nationalities had average of 10.0:
    Crimea
    Equatorial Guinea
    Comoros
    Svalbard Jan Mayen

    >>> booking = Booking([], [])
    >>> booking.read_csv("data/Hotel_Reviews_EU_minimal.csv")
    >>> highest_nationalities_average_score(booking)
    All the following nationalities had average of 10.0:
    Panama
    Liechtenstein
    United States Minor Outlying Islands
    Morocco
    Uruguay
    """

    av_score_per_nationality: dict = {}
    for review in booking.reviews:
        nationality: str = review.nationality.strip()
        if nationality == '':
            continue

        if nationality not in av_score_per_nationality:
            av_score_per_nationality[nationality] = []

        av_score_per_nationality[nationality].append(review.score)

    for nationality, av_scores in av_score_per_nationality.items():
        av_score_per_nationality[nationality] = round(statistics.mean(av_scores),2)

    highest_av_score = av_score_per_nationality[max(av_score_per_nationality, key=av_score_per_nationality.get)]
    highest_av_nationalities: dict = {nationality:av_score for nationality, av_score in av_score_per_nationality.items() if av_score == highest_av_score}
    return f"All the following nationalities had average of {highest_av_score}: \n" + "\n".join(highest_av_nationalities.keys())