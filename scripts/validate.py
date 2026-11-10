"""Validate portable preparation state using only the Python standard library."""

import csv
import json
import re
import sys
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    errors = []
    bank = (root / "questions/BANK.md").read_text(encoding="utf-8")
    questions = re.findall(r"^\| ([A-Z]+-\d{2}) \| (P[012]) \|", bank, re.M)
    ids = [qid for qid, _ in questions]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate question IDs in BANK.md")
    if len(ids) != 155:
        errors.append(f"Expected 155 questions, found {len(ids)}")
    with (root / "progress/questions.csv").open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    tracked = [row["id"] for row in rows]
    if len(tracked) != len(set(tracked)) or set(tracked) != set(ids):
        errors.append("Question tracker must contain every bank ID exactly once")
    valid_states = {"unattempted", "in_progress", "learning", "review_due", "mastered"}
    for row in rows:
        if row["status"] not in valid_states:
            errors.append(f"Invalid status: {row['id']}")
        if row["score"] not in {"", "0", "1", "2", "3", "4"}:
            errors.append(f"Invalid score: {row['id']}")
        if row["status"] == "unattempted" and (row["score"] or row["attempts"] != "0"):
            errors.append(f"Unattempted question has invented assessment: {row['id']}")
    state = json.loads((root / "progress/state.json").read_text(encoding="utf-8"))
    if state["active_question_id"] not in ids:
        errors.append("Active question does not exist")
    if not (root / state["last_session"]).is_file():
        errors.append("Last session does not exist")
    for key in ("completed_diagnostic_questions", "due_review_ids"):
        if not set(state[key]).issubset(ids):
            errors.append(f"Unknown question in {key}")
    for md in root.rglob("*.md"):
        if any(part in {".git", "private", "target", "node_modules"} for part in md.parts):
            continue
        content = md.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            if local and not (md.parent / local).exists():
                errors.append(f"Broken local link in {md.relative_to(root)}: {target}")
    hotlist = (root / "questions/HOTLIST.md").read_text(encoding="utf-8")
    hot_ids = re.findall(r"^\| \d+ \| ([A-Z]+-\d{2}) \|", hotlist, re.M)
    if len(hot_ids) != 25 or len(set(hot_ids)) != 25 or not set(hot_ids).issubset(ids):
        errors.append("Hotlist must contain 25 unique known questions")
    diagnostic = (root / "sessions/DIAGNOSTIC.md").read_text(encoding="utf-8")
    diagnostic_ids = re.findall(r"^\| \d+ \| ([A-Z]+-\d{2}) \|", diagnostic, re.M)
    if not set(diagnostic_ids).issubset(ids):
        errors.append("Diagnostic references unknown questions")
    if errors:
        print("Validation failed:\n" + "\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Validated {len(ids)} questions, {len(hot_ids)} hotlist entries, "
          f"{len(diagnostic_ids)} diagnostic prompts, state, tracker, and local links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
