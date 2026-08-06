import json
import time
from pathlib import Path

from app.rag import ask

BENCHMARK_FILE = Path("evaluation") / "benchmark.json"


def load_benchmarks():

    with open(
        BENCHMARK_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

def evaluate():

    benchmarks = load_benchmarks()

    total = len(benchmarks)

    passed = 0

    total_latency = 0

    print("=" * 70)
    print("BYTEVOX RAG EVALUATION")
    print("=" * 70)

    for index, item in enumerate(
        benchmarks,
        start=1
    ):

        question = item["question"]

        expected = item["expected_source"]

        start = time.perf_counter()

        result = ask(question)

        latency = (
            time.perf_counter() - start
        ) * 1000

        total_latency += latency

        sources = result["sources"]

        success = expected in sources

        if success:
            passed += 1

        print()

        print("-" * 70)

        print(f"Question {index}")

        print()

        print("Question:")

        print(question)

        print()

        print("Expected Source:")

        print(expected)

        print()

        print("Retrieved Sources:")

        for src in sources:

            print(" -", src)

        print()

        print("Latency:")

        print(f"{latency:.2f} ms")

        print()

        print("Status:")

        print(
            "PASS"
            if success
            else "FAIL"
        )

        print("-" * 70)

    print()

    print("=" * 70)

    print("SUMMARY")

    print("=" * 70)

    print(f"Passed : {passed}/{total}")

    print(
        f"Accuracy : {(passed/total)*100:.2f}%"
    )

    print(
        f"Average Latency : {total_latency/total:.2f} ms"
    )

    print("=" * 70)

    
if __name__ == "__main__":

    evaluate()