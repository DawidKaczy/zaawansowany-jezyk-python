import copy


class EventLog:
    def __init__(self, source, events: list[dict] = None):
        self.source = source

        if events is None:
            self.events = []
            return

        for event in events:
            # Sprawdzamy obecność kluczy bez iterowania po nich!
            if "timestamp" not in event or "message" not in event:
                raise ValueError("Brak wymaganego klucza 'timestamp' lub 'message' w zdarzeniu.")

            # 3. Jeśli pętla doszła do tego miejsca, znaczy, że nie było błędów.
            # Dopiero teraz, JEDEN RAZ, wykonujemy głęboką kopię.
        self.events = copy.deepcopy(events)


try:
    invalid_logs = [
        {"timestamp": "2023-10-24 10:00:00", "message": "Wszystko ok"},
        {"timestamp": "2023-10-24 10:05:12", "message": 404}  # Brakuje 'message'
    ]
    bad_log = EventLog(source="AppServer", events=invalid_logs)
except ValueError as e:
    print(f"Zatrzymano (ValueError): {e}")
