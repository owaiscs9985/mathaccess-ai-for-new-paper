import json, sys
from pathlib import Path
from sympy import sympify, simplify, solveset, Symbol, S, Eq
from sympy.parsing.sympy_parser import parse_expr, standard_transformations

def is_equation(s: str) -> bool:
    return "=" in s and not any(op in s for op in ["<", ">", "<=", ">="])

def is_inequality(s: str) -> bool:
    return any(op in s for op in ["<", ">"])

def verify_pair(a: str, b: str) -> bool:
    x = Symbol("x")
    if is_equation(a) and is_equation(b):
        la, ra = a.split("=", 1)
        lb, rb = b.split("=", 1)
        ea = Eq(parse_expr(la, transformations=standard_transformations),
                parse_expr(ra, transformations=standard_transformations))
        eb = Eq(parse_expr(lb, transformations=standard_transformations),
                parse_expr(rb, transformations=standard_transformations))
        return solveset(ea, x, domain=S.Reals) == solveset(eb, x, domain=S.Reals)
    if is_inequality(a) and is_inequality(b):
        return solveset(sympify(a), x, domain=S.Reals) == solveset(sympify(b), x, domain=S.Reals)
    A = parse_expr(a, transformations=standard_transformations)
    B = parse_expr(b, transformations=standard_transformations)
    return simplify(A - B) == 0

def run_category(name, pairs, expect):
    total = correct = 0
    for p in pairs:
        total += 1
        try:
            ok = verify_pair(p["a"], p["b"] if "b" in p else "")
        except Exception:
            ok = False
        if (expect == "accept" and ok) or (expect == "reject" and not ok):
            correct += 1
        else:
            print(f"[MISMATCH-{name}] {p.get('a')!r} vs {p.get('b')!r} ({p.get('cat')})")
    return total, correct

def main(path="test_pairs.json"):
    d = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    eq_t, eq_c = run_category("EQUIV", d["equivalent"], "accept")
    ne_t, ne_c = run_category("NONEQ", d["non_equivalent"], "reject")
    m_t = m_correct = m_accepted = 0
    for p in d["malformed"]:
        m_t += 1
        try:
            ok = verify_pair(p["a"], "")
            if ok:
                m_accepted += 1
                print(f"[MALFORMED ACCEPTED] {p['a']!r} ({p['cat']})")
            else:
                m_correct += 1
        except Exception:
            m_correct += 1
    ad_t = ad_accepted = 0
    for p in d.get("assumption_dependent", []):
        ad_t += 1
        try:
            if verify_pair(p["a"], p["b"]):
                ad_accepted += 1
                print(f"[ASSUMPTION ACCEPTED] {p['a']} vs {p['b']}")
        except Exception:
            pass
    print("\n=== RESULTS ===")
    print(f"Equivalent pairs:        {eq_t}, accepted: {eq_c}, FALSE REJECTS: {eq_t-eq_c} ({(eq_t-eq_c)/eq_t*100:.1f}%)")
    print(f"Non-equivalent pairs:    {ne_t}, rejected: {ne_c}, FALSE ACCEPTS: {ne_t-ne_c} ({(ne_t-ne_c)/ne_t*100:.1f}%)")
    print(f"Malformed inputs:        {m_t}, cleanly rejected: {m_correct}, erroneously accepted: {m_accepted}")
    print(f"Assumption-dependent:    {ad_t}, accepted (lenient): {ad_accepted}, rejected (strict): {ad_t-ad_accepted}")

if __name__ == "__main__":
    main()
