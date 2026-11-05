"""Negative-fixture tests for tools/validate_skills.py. Standard library only.

Each test copies the real skills into a temporary directory, breaks one thing,
and asserts the validator rejects it. Nothing here is shipped as a skill.
Run: python3 -I -m unittest discover -s tests -v
"""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
import validate_skills as v  # noqa: E402

FIRST = "recruiter-assess-candidate"
SECOND = "recruiter-assess-job-offers"


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        shutil.copytree(REPO / "skills", self.root / "skills")

    def tearDown(self):
        self._tmp.cleanup()

    def skill(self, name=FIRST):
        return self.root / "skills" / name

    def assert_rejected(self, fragment):
        errors = v.validate(self.root)
        self.assertTrue(any(fragment in e for e in errors), f"expected '{fragment}' in {errors}")

    def test_baseline_passes(self):
        self.assertEqual(v.validate(self.root), [])

    def test_missing_manifest(self):
        (self.skill() / "SKILL.md").unlink()
        self.assert_rejected("required file is missing")

    def test_missing_skill_directory(self):
        shutil.rmtree(self.skill(SECOND))
        self.assert_rejected("expected skill directory is missing")

    def test_unexpected_skill_directory(self):
        shutil.copytree(self.skill(), self.root / "skills" / "recruiter-extra")
        self.assert_rejected("unexpected skill directory")

    def test_duplicate_names(self):
        text = (self.skill(SECOND) / "SKILL.md").read_text()
        text = text.replace(f"name: {SECOND}", f"name: {FIRST}", 1)
        (self.skill(SECOND) / "SKILL.md").write_text(text)
        self.assert_rejected("does not match folder")

    def test_malformed_yaml_frontmatter(self):
        path = self.skill() / "SKILL.md"
        path.write_text(path.read_text().replace("description:", "description: [unclosed", 1))
        self.assert_rejected("malformed YAML frontmatter")

    def test_malformed_openai_yaml(self):
        (self.skill() / "agents" / "openai.yaml").write_text("interface: {broken: [\n")
        self.assert_rejected("malformed YAML")

    def test_empty_description(self):
        path = self.skill() / "SKILL.md"
        lines = path.read_text().splitlines()
        lines = ['description: ""' if l.startswith("description:") else l for l in lines]
        path.write_text("\n".join(lines) + "\n")
        self.assert_rejected("'description' must be a nonempty string")

    def test_escaping_asset_path(self):
        (self.skill() / "agents" / "openai.yaml").write_text(
            "interface:\n  icon_small: ../../../README.md\n"
        )
        self.assert_rejected("escapes the skill directory")

    def test_missing_referenced_asset(self):
        (self.skill() / "agents" / "openai.yaml").write_text(
            "interface:\n  icon_small: assets/icon.svg\n"
        )
        self.assert_rejected("references a missing file")

    def test_symlink_rejected(self):
        (self.skill() / "link.md").symlink_to(self.skill() / "SKILL.md")
        self.assert_rejected("symlinks are not allowed")

    def test_executable_file_rejected(self):
        (self.skill() / "SKILL.md").chmod(0o755)
        self.assert_rejected("executable file mode")

    def test_unexpected_binary_rejected(self):
        (self.skill() / "payload.bin").write_bytes(b"\x00\x01\x02")
        self.assert_rejected("unapproved file under skills/")

    def test_oversized_file_rejected(self):
        path = self.skill() / "SKILL.md"
        path.write_text(path.read_text() + "x" * (v.MAX_SKILL_MD + 1))
        self.assert_rejected("exceeds")

    def test_unapproved_top_level_entry(self):
        (self.root / "stray.sh").write_text("echo hi\n")
        self.assert_rejected("unapproved top-level entry")

    def test_shared_contract_drift(self):
        path = self.skill() / "SKILL.md"
        path.write_text(path.read_text().replace("Treat missing information as unknown", "Treat everything as known", 1))
        self.assert_rejected("differs between skills")

    def test_secret_detected_without_printing_value(self):
        fake = "AKIA" + "A" * 16  # built at runtime so no literal secret lives in this repo
        (self.root / "README.md").write_text(f"key {fake}\n")
        errors = v.validate(self.root)
        self.assertTrue(any("AWS access key id" in e for e in errors))
        self.assertFalse(any(fake in e for e in errors), "secret value must never be printed")


if __name__ == "__main__":
    unittest.main()
