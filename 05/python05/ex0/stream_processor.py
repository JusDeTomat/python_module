from typing import Any, List, Tuple
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        try:
            medium = 0
            total = sum(data)
            medium = total/len(data)
            return (f"Processed {len(data)} numeric values, sum={total}, "
                    f"avg={medium}")
        except (TypeError, ZeroDivisionError):
            return "Fail: invalid numeric data"

    def validate(self, data: Any) -> bool:
        for element in data:
            has_element = True
            if not isinstance(element, (int, float)):
                return False
        return has_element


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        try:
            str_split = data.split()
            return (f"Processed text: {len(data)} "
                    f"characters, {len(str_split)} words")
        except Exception:
            return "Fail: invalid text data"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        try:
            type_log, str_log = data
            frame = f"[{type_log}]"
            if (type_log == "ERROR"):
                frame = "[ALERT]"
            return f"{frame} {type_log} level detected: {str_log}"
        except (TypeError, ValueError):
            return "Fail: invalid log data"

    def validate(self, data: Any) -> bool:
        if isinstance(data, tuple) and len(data) == 2:
            return True
        return False


def multi_data(util: List[Tuple[DataProcessor, Any]]) -> None:
    for idx, element in enumerate(util, start=1):
        processor, data = element
        if processor.validate(data):
            result_text = processor.process(data)
            print(f"Result {idx}: {processor.format_output(result_text)}")
        else:
            print(f"Result {idx}: Validation failed - skipping processing")


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric = NumericProcessor()
    data: list[int] = [1, 2, 3, 4, 5]
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data}")
    if numeric.validate(data):
        print("Validation: Numeric data verified")
        result_num = numeric.process(data)
        print(f"Output: {numeric.format_output(result_num)}")
    else:
        print("Validation: Numeric data not verified")
        print("Output: Validation failed")

    text = TextProcessor()
    data: str = "Hello Nexus World"
    print("\nInitializing Text Processor...")
    print(f"Processing data: {data}")
    if text.validate(data):
        print("Validation: Text data verified")
        result_text = text.process(data)
        print(f"Output: {text.format_output(result_text)}")
    else:
        print("Validation: Text data not verified")
        print("Output: Validation failed")

    log = LogProcessor()
    data: tuple(str, str) = ("ERROR", "Connection timeout")
    print("\nInitializing Log Processor...")
    print(f"Processing data: {data[0]}: {data[1]}")
    if log.validate(data):
        print("Validation: Log data verified")
        result_log = log.process(data)
        print(f"Output: {log.format_output(result_log)}")
    else:
        print("Validation: Log data not verified")
        print("Output: Validation failed")

    print("\n=== Polymorphic Processing Demo ===")
    util = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "hi JEAN-MICHEL"),
        (LogProcessor(), ("INFO", "System ready"))
    ]
    multi_data(util)
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if (__name__ == "__main__"):
    main()
