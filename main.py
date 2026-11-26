"""Gate runner: reads the one-line entry and writes it to the output dir."""
import json
import pathlib
import sys

here = pathlib.Path(__file__).resolve().parent
ENTRY = here / "entry.txt"
FLOOR, CEIL = 1, 199


def emit(text):
    import os

    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out.mkdir(parents=True, exist_ok=True)
    dest = out / "entry.txt"
    dest.write_text(text + "\n", encoding="utf-8")
    return dest


payload = {}
line = ENTRY.read_text(encoding="utf-8").strip()
payload["chars"] = len(line)
payload["valid"] = FLOOR <= len(line) <= CEIL and line.isprintable()
if payload["valid"]:
    payload["dest"] = str(emit(line))
print(json.dumps(payload))
sys.exit(0 if payload["valid"] else 1)
