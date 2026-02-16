#!/usr/bin/env python3

from typing import Any
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

    def format_output(self, result: Any) -> str:
        return result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        try:
            medium = 0
            total = sum(data)
            medium = total/len(data)
            return f"Processed {len(data)} numeric values, sum={total}, \
avg={medium}"
        except TypeError:
            return "Fail"

    def validate(self, data: Any) -> bool:
        for element in data:
            if not (isinstance(element, int)):
                return False
        return True


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        try:
            str_split = data.split()
            return f"Processed text: {len(data)} \
characters, {len(str_split)} words"
        except TypeError:
            return "Fail"

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
        except TypeError:
            return "Fail"

    def validate(self, data: Any) -> bool:
        if isinstance(data, tuple):
            return True
        return False


def multi_data(util: list) -> None:
    nb = 0
    for element in util:
        nb += 1
        text, data = element
        result_text = text.process(data)
        if (text.validate(data)):
            print(f"Result {nb}: {text.format_output(result_text)}")


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data}")
    result_num = numeric.process(data)
    if (numeric.validate(data)):
        print("Validation: Numeric data verified")
    else:
        print("Validation: Numeric data not verified")
    print(f"Output: {numeric.format_output(result_num)}")

    text = TextProcessor()
    data = "Hello Nexus World"
    print("\nInitializing Text Processor...")
    print(f"Processing data: {data}")
    result_text = text.process(data)
    if (text.validate(data)):
        print("Validation: Text data verified")
    else:
        print("Validation: Text data not verified")
    print(f"Output: {text.format_output(result_text)}")

    log = LogProcessor()
    data = ("ERROR", "Connection timeout")
    print("\nInitializing Log Processor...")
    print(f"Processing data: {data[0]}: {data[1]}")
    result_log = log.process(data)
    if (log.validate(data)):
        print("Validation: Log data verified")
    else:
        print("Validation: Log data not verified")
    print(f"Output: {log.format_output(result_log)}")

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
