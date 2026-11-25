import json
from pathlib import Path
p = Path("test_pairs.json")
d = json.loads(p.read_text(encoding="utf-8-sig"))
back = [e for e in d["assumption_dependent"] if e["a"] in ("sqrt(8)", "x**(1/2)")]
d["assumption_dependent"] = [e for e in d["assumption_dependent"] if e["a"] not in ("sqrt(8)", "x**(1/2)")]
d["equivalent"].extend(back)
p.write_text(json.dumps(d, indent=2), encoding="utf-8")
print("equivalent:", len(d["equivalent"]))
print("non_equivalent:", len(d["non_equivalent"]))
print("malformed:", len(d["malformed"]))
print("assumption_dependent:", len(d["assumption_dependent"]))
