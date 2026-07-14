def generate_analysis(repositories):
    features = []
    limitations = []

    for repo in repositories:
        text = (
            (repo.get("description") or "").lower()
        )

        if "cnn" in text:
            features.append("CNN based disease detection")

        if "deep learning" in text:
            features.append("Deep Learning models")

        if "image" in text:
            features.append("Leaf image analysis")

        if "recommendation" in text:
            features.append("Crop recommendation")

        if "weather" in text:
            features.append("Weather prediction")

        if "iot" in text:
            features.append("IoT sensors")

    features = list(set(features))

    if "CNN based disease detection" in features:
        limitations.append("Requires labeled datasets")

    if "Leaf image analysis" in features:
        limitations.append("Detects only after visible symptoms")

    if "Weather prediction" in features:
        limitations.append("Depends on internet APIs")

    if not limitations:
        limitations = [
            "Limited explainability",
            "Low scalability",
            "Requires large datasets"
        ]

    innovation = [
        "Predict disease before symptoms",
        "Explainable AI recommendations",
        "Offline mobile diagnosis",
        "Satellite + Drone integration",
        "IoT based continuous monitoring"
    ]

    return {
        "features": features,
        "limitations": limitations,
        "innovation": innovation
    }