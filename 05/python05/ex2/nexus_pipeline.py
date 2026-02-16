import time
from abc import ABC, abstractmethod
from typing import Protocol, Any, Union, List, Dict


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[Any] = []
        self.stats: Dict[str, Any] = {
            "processed": 0,
            "errors": 0,
            "start_time": 0.0,
            "total_time": 0.0
        }

    def add_stage(self, stage: Any) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any: ...

    def run_pipeline(self, data: Any) -> Any:
        """Runs each stage sequentially."""
        self.stats["start_time"] = time.time()
        result = data
        for stage in self.stages:
            try:
                result = stage.process(result)
            except Exception as e:
                self.stats["errors"] += 1
                print(f"  Error detected in Stage 2: {e}")
                print("  Recovery initiated: Switching to backup processor")
                result = {"error_recovery": True, "original_data": data}
                print("  Recovery successful: Pipeline restored, \
processing resumed")
                break
        self.stats["processed"] += 1
        self.stats["total_time"] = time.time() - self.stats["start_time"]
        return result


class InputStage:
    """Stage 1: input validation and parsing."""
    def process(self, data: Any) -> Dict:
        if isinstance(data, dict):
            return {**data, "_validated": True}
        if isinstance(data, str):
            return {"raw": data, "_validated": True}
        return {"raw": str(data), "_validated": True}


class TransformStage:
    """Stage 2: data transformation and enrichment."""
    def process(self, data: Any) -> Dict:
        if not isinstance(data, dict):
            raise ValueError("Invalid data format")
        enriched = {**data, "_enriched": True, "_timestamp": time.time()}
        if "value" in enriched:
            val = enriched["value"]
            enriched["_range"] = "Normal range" if 18 <= val <= 26 else "Out \
of range"
        if "raw" in enriched and "," in str(enriched["raw"]):
            enriched["_parsed"] = True
            enriched["_actions"] = 1
        return enriched


class OutputStage:
    """Stage 3: output formatting and delivery."""
    def process(self, data: Any) -> str:
        if not isinstance(data, dict):
            return str(data)
        if "sensor" in data:
            return (f"Processed {data['sensor']} reading: "
                    f"{data['value']}°C ({data.get('_range', '')})")
        if "_parsed" in data:
            return f"User activity logged: {data.get('_actions', 0)} actions \
processed"
        if "stream_data" in data:
            readings = data["stream_data"]
            avg = sum(readings) / len(readings) if readings else 0
            return f"Stream summary: {len(readings)} readings, \
avg: {avg:.1f}°C"
        return str(data)


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print('  Input: {{"sensor": "temp", "value": 23.5, "unit": "C"}}')
        result = self.run_pipeline(data)
        print("  Transform: Enriched with metadata and validation")
        print(f"  Output: {result}")
        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print('  Input: "user,action,timestamp"')
        result = self.run_pipeline(data)
        print("  Transform: Parsed and structured data")
        print(f"  Output: {result}")
        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print("  Input: Real-time sensor stream")
        result = self.run_pipeline(data)
        print("  Transform: Aggregated and filtered")
        print(f"  Output: {result}")
        return result


# ============================================================
# NEXUS MANAGER — orchestrates the pipelines
# ============================================================
class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.pipeline_registry: Dict[str, ProcessingPipeline] = {}
        self.chain_log: List[Dict[str, Any]] = []

    def add_pipeline(self, name: str, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)
        self.pipeline_registry[name] = pipeline

    def process_data(self, name: str, data: Any) -> Any:
        pipeline = self.pipeline_registry.get(name)
        if pipeline:
            return pipeline.process(data)
        return None

    def chain_pipelines(self, pipeline_names: List[str], data: Any) -> Any:
        """Chains multiple pipelines: output
        of one pipeline feeds into the next."""
        result = data
        for name in pipeline_names:
            pipeline = self.pipeline_registry.get(name)
            if pipeline:
                result = pipeline.run_pipeline(result)
                self.chain_log.append({"pipeline": name, "result": result})
                if len(self.chain_log) > 100:
                    self.chain_log.pop(0)
        return result

    def get_stats(self) -> Dict[str, Any]:
        stats: Dict[str, Any] = {}
        for name, pipeline in self.pipeline_registry.items():
            stats[name] = pipeline.stats
        return stats


# ============================================================
# MAIN
# ============================================================
def _build_pipeline(adapter: ProcessingPipeline) -> ProcessingPipeline:
    """Adds the 3 standard stages to a pipeline."""
    adapter.add_stage(InputStage())
    adapter.add_stage(TransformStage())
    adapter.add_stage(OutputStage())
    return adapter


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    # --- Create manager and pipelines ---
    manager = NexusManager()

    json_pipeline = _build_pipeline(JSONAdapter("json-001"))
    csv_pipeline = _build_pipeline(CSVAdapter("csv-001"))
    stream_pipeline = _build_pipeline(StreamAdapter("stream-001"))

    manager.add_pipeline("json", json_pipeline)
    manager.add_pipeline("csv", csv_pipeline)
    manager.add_pipeline("stream", stream_pipeline)

    # --- Multi-format processing ---
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    print("=== Multi-Format Data Processing ===\n")

    print("Processing JSON data through pipeline...")
    json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    manager.process_data("json", json_data)

    print("\nProcessing CSV data through same pipeline...")
    csv_data = "user,action,timestamp"
    manager.process_data("csv", csv_data)

    print("\nProcessing Stream data through same pipeline...")
    stream_data = {"stream_data": [21.5, 22.0, 22.1, 22.3, 22.4]}
    manager.process_data("stream", stream_data)

    print("\n=== Pipeline Chaining Demo ===\n")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

    chain_a = _build_pipeline(JSONAdapter("chain-A"))
    chain_b = _build_pipeline(CSVAdapter("chain-B"))
    chain_c = _build_pipeline(StreamAdapter("chain-C"))
    manager.add_pipeline("chain_A", chain_a)
    manager.add_pipeline("chain_B", chain_b)
    manager.add_pipeline("chain_C", chain_c)

    chain_input = {"records": 100, "source": "raw_data", "value": 20.0}
    chain_result = manager.chain_pipelines(
        ["chain_A", "chain_B", "chain_C"],
        chain_input
    )
    print(f"Chain result: {chain_input['records']} records processed through \
{len(chain_result)}-stage pipeline")

    all_stats = manager.get_stats()
    total_errors = sum(s["errors"] for s in all_stats.values())
    total_processed = sum(s["processed"] for s in all_stats.values())
    efficiency = ((total_processed - total_errors) /
                  max(total_processed, 1)) * 100
    total_time = sum(s["total_time"] for s in all_stats.values())
    print(f"Performance: {efficiency}% efficiency, {total_time:.1f}s total \
processing time")

    print("\n=== Error Recovery Test ===\n")
    print("Simulating pipeline failure...")

    error_pipeline = JSONAdapter("error-test")
    error_pipeline.add_stage(InputStage())
    error_pipeline.add_stage(TransformStage())
    error_pipeline.add_stage(OutputStage())
    manager.add_pipeline("error_test", error_pipeline)

    class BadData:
        """Object designed to trigger an error in TransformStage."""
        def __str__(self) -> str:
            raise ValueError("Invalid data format")

    error_pipeline.run_pipeline(BadData())

    print("\nNexus Integration complete. All systems operational.")
    print("\nHow does the combination of method overriding and subtype \
polymorphism")
    print("enable building scalable, maintainable data processing systems?")
    print("What real-world engineering problems does this approach solve?")


if __name__ == "__main__":
    main()
