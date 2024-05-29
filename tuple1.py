def format_itineraries(itineraries):
    formatted_str = ""
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        formatted_str += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return formatted_str.strip()

# Example usage:
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(format_itineraries(itineraries))
