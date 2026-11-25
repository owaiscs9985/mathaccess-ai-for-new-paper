import json
from pathlib import Path
p = Path("test_pairs.json")
d = json.loads(p.read_text(encoding="utf-8-sig"))
drop = {"x**2 <= 4", "x > 1 and x < 5"}
d["equivalent"] = [e for e in d["equivalent"] if e["a"] not in drop]
ad = [e for e in d["equivalent"] if e["cat"] in ("log", "radical")]
d["equivalent"] = [e for e in d["equivalent"] if e["cat"] not in ("log", "radical")]
d["assumption_dependent"] = ad
p.write_text(json.dumps(d, indent=2), encoding="utf-8")
print("equivalent:", len(d["equivalent"]))
print("non_equivalent:", len(d["non_equivalent"]))
print("malformed:", len(d["malformed"]))
print("assumption_dependent:", len(d["assumption_dependent"]))
