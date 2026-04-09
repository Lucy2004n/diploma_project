import csv


def calculate_score(search_volume, engagement, sentiment):
    """Simple weighted score for trend ranking."""
    return (0.5 * search_volume) + (0.3 * engagement) + (0.2 * sentiment)


def load_market_data(file_path):
    trends = []

    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            keyword = row["keyword"]
            search_volume = float(row["search_volume"])
            engagement = float(row["engagement"])
            sentiment = float(row["sentiment"])

            score = calculate_score(search_volume, engagement, sentiment)

            trends.append(
                {
                    "keyword": keyword,
                    "search_volume": search_volume,
                    "engagement": engagement,
                    "sentiment": sentiment,
                    "score": score,
                }
            )

    return trends


def find_top_trend(trends):
    return max(trends, key=lambda item: item["score"])


def generate_ad_script(trend):
    keyword = trend["keyword"]

    scenes = [
        f"Scene 1: A customer notices a common beauty problem and searches for '{keyword}'.",
        f"Scene 2: Quick clips show social buzz and strong engagement around '{keyword}'.",
        f"Scene 3: The product is introduced as the easy solution inspired by '{keyword}'.",
        "Scene 4: Happy before/after moment with a call-to-action: 'Try it today!'.",
    ]

    return scenes


def main():
    file_path = "market_data.csv"
    trends = load_market_data(file_path)
    top_trend = find_top_trend(trends)

    print("Top trend:")
    print(f"- Keyword: {top_trend['keyword']}")
    print(f"- Score: {top_trend['score']:.2f}\n")

    print("4-scene advertising script:")
    for scene in generate_ad_script(top_trend):
        print(scene)


if __name__ == "__main__":
    main()
