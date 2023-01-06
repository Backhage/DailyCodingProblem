def get_itinerary(flights, current_itenerary):
    if not flights:
        return current_itenerary

    last_stop = current_itenerary[-1]
    for i, (origin, destination) in enumerate(flights):
        flights_minus_current = flights[:i] + flights[i + 1 :]
        current_itenerary.append(destination)
        if origin == last_stop:
            return get_itinerary(flights_minus_current, current_itenerary)
        current_itenerary.pop()

    return None
