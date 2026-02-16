#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    """Abstract base class to represent a generic data stream interface."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the data stream with a unique identifier."""
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter the input batch based on a specific string criterion."""
        return [item for item in data_batch
                if isinstance(item, str) and criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic metadata and statistics about the stream."""
        return {"stream_id": self.stream_id, "type": "base"}


class SensorStream(DataStream):
    """A stream specialized in processing environmental sensor data."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Calculate the average temperature
        from a batch of sensor readings."""
        temps = self.filter_data(data_batch, "temp:")
        parsed = []
        for item in temps:
            try:
                parsed.append(float(item.split(":")[1]))
            except (ValueError, IndexError):
                pass
        avg_temp = sum(parsed) / len(parsed) if parsed else 0
        return (f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg_temp}°C")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor data specifically for
        strings containing the criteria."""
        return [item for item in data_batch
                if isinstance(item, str) and criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Log and return statistics specific to environmental data."""
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
        return {"stream_id": self.stream_id, "type": "Environmental Data"}


class TransactionStream(DataStream):
    """A stream designed to track and calculate financial transaction flows."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Analyze buy/sell operations to determine the net financial flow."""
        buy_total = 0
        sell_total = 0
        data_batch = self.filter_data(data_batch, "buy")
        for element in data_batch:
            if isinstance(element, str):
                try:
                    if "buy:" in element:
                        buy_total += int(element.split(":")[1])
                    elif "sell:" in element:
                        sell_total += int(element.split(":")[1])
                except (ValueError, IndexError):
                    pass
        net_flow = buy_total - sell_total
        sign = "+" if net_flow >= 0 else ""
        return (f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {sign}{net_flow} units")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data to include only relevant financial transaction tags."""
        return [item for item in data_batch
                if isinstance(item, str)
                and (criteria in item or "sell" in item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Log and return statistics specific to financial data."""
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")
        return {"stream_id": self.stream_id, "type": "Financial Data"}


class EventStream(DataStream):
    """A stream dedicated to monitoring and counting
    system events and errors."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Count the number of errors detected within a batch of events."""
        errors = self.filter_data(data_batch, "error")
        return (f"Event analysis: {len(data_batch)} events, "
                f"{len(errors)} error detected")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter event logs based on severity or type keywords."""
        return [item for item in data_batch
                if isinstance(item, str) and criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Log and return statistics specific to system event logs."""
        print(f"Stream ID: {self.stream_id}, Type: System Events")
        return {"stream_id": self.stream_id, "type": "System Events"}


class StreamProcessor:
    """Manager class to aggregate and process multiple polymorphic streams."""

    def __init__(self) -> None:
        """Initialize the processor with an empty list of streams."""
        self.streams: List[tuple] = []

    def add_stream(self, stream: DataStream, data: List[Any]) -> None:
        """Register a new stream and its associated data for processing."""
        self.streams.append((stream, data))

    def process_all(self) -> None:
        """Iterate through all registered streams and
        print their analysis results."""
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        for stream, data in self.streams:
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {len(data)} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {len(data)} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {len(data)} events processed")

    def filter_streams(self, data: List[str]) -> None:
        """Extract and count high-priority alerts and
        transactions from raw data."""
        print("\nStream filtering active: High-priority data only")
        alert = 0
        transaction = 0
        for element in data:
            if "error" in element:
                alert += 1
            if "buy" in element or "sell" in element:
                transaction += 1
        print(f"Filtered results: {alert} critical sensor alerts, "
              f"{transaction} large transaction")


def main():
    """Main execution entry point for the Code Nexus system."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    data = SensorStream("SENSOR_001")
    value = ["temp:22.5", "humidity:65", "pressure:1013"]
    data.get_stats()
    print(f"Processing sensor batch: {value}")
    print(data.process_batch(value))
    print()

    print("Initializing Transaction Stream...")
    data = TransactionStream("TRANS_001")
    value = ["buy:100", "sell:150", "buy:75"]
    data.get_stats()
    print(f"Processing transaction batch: {value}")
    print(data.process_batch(value))
    print()

    print("Initializing Event Stream...")
    data = EventStream("EVENT_001")
    value = ["login", "error", "logout"]
    data.get_stats()
    print(f"Processing event batch: {value}")
    print(data.process_batch(value))
    print()

    print("=== Polymorphic Stream Processing ===\n")
    processor = StreamProcessor()
    processor.add_stream(
        SensorStream("SENSOR_002"),
        ["temp:22.5", "temp:30.1"])
    processor.add_stream(
        TransactionStream("TRANS_002"),
        ["buy:100", "sell:150", "buy:75", "sell:10000000000"])
    processor.add_stream(
        EventStream("EVENT_002"),
        ["login", "error", "logout"])
    processor.process_all()
    processor.filter_streams(["error", "info", "buy", "error"])
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if (__name__ == "__main__"):
    main()
