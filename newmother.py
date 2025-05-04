import datetime
import logging
from typing import List, Dict, Optional, Union, Any

# Setup logging for better error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Event:
    """
    Base class for tracking events related to the newborn.  Uses the Template Method
    pattern to ensure all events have a timestamp and can be represented as a dictionary.
    """
    def __init__(self, timestamp: Optional[datetime.datetime] = None) -> None:
        """
        Initializes an Event object.

        Args:
            timestamp: The timestamp of the event. If None, the current time is used.
        """
        self._timestamp = timestamp if timestamp else datetime.datetime.now()

    @property
    def timestamp(self) -> datetime.datetime:
        """
        Gets the timestamp of the event.

        Returns:
            The timestamp as a datetime object.
        """
        return self._timestamp

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the event data to a dictionary.  This is an abstract method that
        must be implemented by subclasses.

        Returns:
            A dictionary representation of the event.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("Subclasses must implement the to_dict method.")

    def __repr__(self) -> str:
        """
        Provides a string representation of the Event.

        Returns:
            A string representation, including the timestamp.
        """
        return f"{self.__class__.__name__}(timestamp={self.timestamp})"


class NursingEvent(Event):
    """
    Represents a nursing session.
    """
    def __init__(self, start_time: datetime.datetime, end_time: datetime.datetime,
                 side: str, notes: str = "") -> None:
        """
        Initializes a NursingEvent object.

        Args:
            start_time: The start time of the nursing session.
            end_time: The end time of the nursing session.
            side: The side the baby nursed on ('left', 'right', or 'both').
            notes: Any additional notes about the session.
        """
        super().__init__(start_time)  # Use start_time as the event timestamp
        self.start_time = start_time
        self.end_time = end_time
        self.side = side
        self.notes = notes

    @property
    def duration(self) -> datetime.timedelta:
        """
        Calculates the duration of the nursing session.

        Returns:
            The duration as a timedelta object.
        """
        return self.end_time - self.start_time

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the nursing event data to a dictionary.

        Returns:
            A dictionary representation of the event.
        """
        return {
            "type": "nursing",
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "duration_seconds": self.duration.total_seconds(),
            "side": self.side,
            "notes": self.notes
        }

    def __repr__(self) -> str:
        """
        Provides a string representation of the NursingEvent.
        """
        return (f"NursingEvent(start_time={self.start_time}, end_time={self.end_time}, "
                f"side='{self.side}', notes='{self.notes}')")


class SleepEvent(Event):
    """
    Represents a sleep session.
    """
    def __init__(self, start_time: datetime.datetime, end_time: datetime.datetime,
                 notes: str = "") -> None:
        """
        Initializes a SleepEvent object.

        Args:
            start_time: The start time of the sleep session.
            end_time: The end time of the sleep session.
            notes: Any additional notes about the sleep session.
        """
        super().__init__(start_time) # Use start_time as the event timestamp
        self.start_time = start_time
        self.end_time = end_time
        self.notes = notes

    @property
    def duration(self) -> datetime.timedelta:
        """
        Calculates the duration of the sleep session.

        Returns:
            The duration as a timedelta object.
        """
        return self.end_time - self.start_time

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the sleep event data to a dictionary.

        Returns:
            A dictionary representation of the event.
        """
        return {
            "type": "sleep",
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "duration_seconds": self.duration.total_seconds(),
            "notes": self.notes
        }

    def __repr__(self) -> str:
        """
        Provides a string representation of the SleepEvent.
        """
        return f"SleepEvent(start_time={self.start_time}, end_time={self.end_time}, notes='{self.notes}')"


class NewbornTracker:
    """
    Manages and tracks nursing and sleep events for a newborn.
    """
    def __init__(self) -> None:
        """
        Initializes the NewbornTracker object.
        """
        self.events: List[Event] = []

    def add_event(self, event: Event) -> None:
        """
        Adds a new event to the tracker.

        Args:
            event: The Event object to add (NursingEvent or SleepEvent).

        Raises:
            TypeError: If the event is not a NursingEvent or SleepEvent.
        """
        if not isinstance(event, (NursingEvent, SleepEvent)):
            raise TypeError("event must be a NursingEvent or SleepEvent")
        self.events.append(event)
        logging.info(f"Added event: {event}")

    def get_events(self, event_type: Optional[str] = None,
                   start_date: Optional[datetime.datetime] = None,
                   end_date: Optional[datetime.datetime] = None) -> List[Event]:
        """
        Retrieves events, optionally filtered by type and/or date range.

        Args:
            event_type: The type of event to filter by ('nursing' or 'sleep').
            start_date: The start date for filtering events.
            end_date: The end date for filtering events.

        Returns:
            A list of Event objects matching the criteria.  Returns an empty list
            if no events match.
        """
        filtered_events: List[Event] = self.events

        if event_type:
            event_type = event_type.lower() #simplify
            if event_type not in ('nursing', 'sleep'):
                raise ValueError(f"Invalid event_type: {event_type}.  Must be 'nursing' or 'sleep'.")
            filtered_events = [event for event in filtered_events if isinstance(event, NursingEvent if event_type == 'nursing' else SleepEvent)]

        if start_date:
            filtered_events = [event for event in filtered_events if event.timestamp >= start_date]
        if end_date:
            filtered_events = [event for event in filtered_events if event.timestamp <= end_date]

        return filtered_events

    def get_summary(self, start_date: Optional[datetime.datetime] = None,
                    end_date: Optional[datetime.datetime] = None) -> Dict[str, Any]:
        """
        Provides a summary of nursing and sleep activity, optionally within a date range.

        Args:
            start_date: The start date for the summary.
            end_date: The end date for the summary.

        Returns:
            A dictionary containing the summary data, including total nursing duration,
            total sleep duration, and number of nursing and sleep sessions.
        """
        nursing_events = self.get_events(event_type='nursing', start_date=start_date, end_date=end_date)
        sleep_events = self.get_events(event_type='sleep', start_date=start_date, end_date=end_date)

        total_nursing_duration = datetime.timedelta()
        for event in nursing_events:
            if isinstance(event, NursingEvent): #redundant, but safe
                total_nursing_duration += event.duration

        total_sleep_duration = datetime.timedelta()
        for event in sleep_events:
             if isinstance(event, SleepEvent): #redundant, but safe
                total_sleep_duration += event.duration

        return {
            "summary_start_date": start_date.isoformat() if start_date else "All Time",
            "summary_end_date": end_date.isoformat() if end_date else "All Time",
            "total_nursing_sessions": len(nursing_events),
            "total_nursing_duration_seconds": total_nursing_duration.total_seconds(),
            "total_sleep_sessions": len(sleep_events),
            "total_sleep_duration_seconds": total_sleep_duration.total_seconds(),
        }

    def to_dict(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Converts all events in the tracker to a list of dictionaries.  Useful for
        serialization (e.g., JSON).

        Returns:
            A dictionary with a single key "events" and a list of event dictionaries
            as the value.
        """
        return {"events": [event.to_dict() for event in self.events]}

    @classmethod
    def from_dict(cls, data: Dict[str, List[Dict[str, Any]]]) -> 'NewbornTracker':
        """
        Creates a NewbornTracker object from a dictionary representation of events.
        Useful for deserialization.

        Args:
            data: A dictionary containing the events data, expected to have the format
                  produced by the `to_dict` method.

        Returns:
            A new NewbornTracker object populated with the events from the dictionary.

        Raises:
            KeyError: If the input dictionary does not contain the "events" key.
            ValueError: If an event dictionary has an invalid type.
        """
        if "events" not in data:
            raise KeyError("Input dictionary must contain 'events' key.")

        tracker = cls()
        for event_dict in data["events"]:
            event_type = event_dict.get("type")
            if not event_type:
                logging.warning(f"Skipping event with missing 'type': {event_dict}")
                continue  # Skip invalid event

            try:
                start_time = datetime.datetime.fromisoformat(event_dict["start_time"])
                end_time = datetime.datetime.fromisoformat(event_dict["end_time"])
            except (KeyError, ValueError) as e:
                logging.error(f"Skipping event with invalid date format: {event_dict} - {e}")
                continue

            if event_type == "nursing":
                try:
                    side = event_dict["side"]
                    notes = event_dict.get("notes", "")
                    event = NursingEvent(start_time, end_time, side, notes)
                    tracker.add_event(event)
                except KeyError as e:
                    logging.error(f"Skipping nursing event with missing key: {event_dict} - {e}")
            elif event_type == "sleep":
                notes = event_dict.get("notes", "")
                event = SleepEvent(start_time, end_time, notes)
                tracker.add_event(event)
            else:
                logging.warning(f"Skipping event with unknown type: {event_type}")

        return tracker
    def __repr__(self) -> str:
        """
        Provides a string representation of the NewbornTracker.
        """
        return f"NewbornTracker(events={self.events})"

def main() -> None:
    """
    Main function to demonstrate the usage of the NewbornTracker class.
    """
    tracker = NewbornTracker()

    # Add some sample events
    now = datetime.datetime.now()
    five_minutes_ago = now - datetime.timedelta(minutes=5)
    thirty_minutes_ago = now - datetime.timedelta(minutes=30)
    one_hour_ago = now - datetime.timedelta(hours=1)
    two_hours_ago = now - datetime.timedelta(hours=2)


    nursing1 = NursingEvent(start_time=thirty_minutes_ago, end_time=now, side="left", notes="Good latch")
    nursing2 = NursingEvent(start_time=two_hours_ago, end_time=one_hour_ago, side="right", notes="Fussy baby")
    sleep1 = SleepEvent(start_time=two_hours_ago, end_time=now, notes="Deep sleep")
    sleep2 = SleepEvent(start_time=now - datetime.timedelta(hours=4), end_time=now - datetime.timedelta(hours=3), notes="short nap")


    tracker.add_event(nursing1)
    tracker.add_event(nursing2)
    tracker.add_event(sleep1)
    tracker.add_event(sleep2)

    # Get events for the last hour
    last_hour_events = tracker.get_events(start_date=now - datetime.timedelta(hours=1))
    print("\nEvents in the last hour:")
    for event in last_hour_events:
        print(event)

    # Get a summary of all events
    summary = tracker.get_summary()
    print("\nSummary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Get a summary of the last 24 hours
    summary_24_hours = tracker.get_summary(start_date=now - datetime.timedelta(days=1), end_date=now)
    print("\nSummary for the last 24 hours:")
    for key, value in summary_24_hours.items():
        print(f"{key}: {value}")
    # Convert tracker to dictionary and back
    tracker_dict = tracker.to_dict()
    print("\nTracker as dictionary:")
    print(tracker_dict)

    tracker_from_dict = NewbornTracker.from_dict(tracker_dict)
    print("\nTracker from dictionary:")
    print(tracker_from_dict)

    #Demonstrate filtering by event type
    nursing_events = tracker.get_events(event_type='nursing')
    print("\nNursing Events Only")
    for event in nursing_events:
        print(event)

if __name__ == "__main__":
    main()
