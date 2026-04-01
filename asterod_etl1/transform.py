def transform_data(raw_data):
    result = []

    if not raw_data or "near_earth_objects" not in raw_data:
        return result

    neo_data = raw_data["near_earth_objects"]

    for date in neo_data:
        for obj in neo_data[date]:
            try:
                result.append({
                    "id": obj["id"],
                    "name": obj["name"],
                    "magnitude": obj["absolute_magnitude_h"],
                    "hazardous": obj["is_potentially_hazardous_asteroid"],
                    "approach_date": date,
                    "velocity": float(
                        obj["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]
                    ),
                    "miss_distance": float(
                        obj["close_approach_data"][0]["miss_distance"]["kilometers"]
                    ),
                    "orbiting_body": obj["close_approach_data"][0]["orbiting_body"]
                })
            except Exception as e:
                print("TRANSFORM ERROR:", e)

    return result