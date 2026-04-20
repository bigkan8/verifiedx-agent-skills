from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]


def _load_json(relative_path: str) -> dict:
    path = ROOT / relative_path
    if not path.exists():
        raise SystemExit(f"Missing required file: {relative_path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in {relative_path}: {error}") from error


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def _validate_skill(relative_path: str) -> None:
    path = ROOT / relative_path
    _require(path.exists(), f"Missing skill file: {relative_path}")
    text = path.read_text(encoding="utf-8")
    _require(text.startswith("---\n"), f"Skill frontmatter missing in {relative_path}")
    _require("\nname:" in text, f"Skill name missing in {relative_path}")
    _require("\ndescription:" in text, f"Skill description missing in {relative_path}")
    _require("../../../../skills/" not in text, f"Skill must be self-contained inside plugin cache: {relative_path}")
    _require(
        "Read and follow the canonical skill at" not in text,
        f"Skill must contain full instructions, not an external redirect: {relative_path}",
    )


def _require_file(relative_path: str) -> None:
    _require((ROOT / relative_path).exists(), f"Missing required file: {relative_path}")


def _validate_marketplace(relative_path: str, sources: list[str]) -> None:
    marketplace = _load_json(relative_path)
    plugins = marketplace.get("plugins")
    _require(isinstance(plugins, list) and plugins, f"No plugins listed in {relative_path}")
    for source in sources:
        _require((ROOT / source).exists(), f"Marketplace path missing for {relative_path}: {source}")


def _validate_plugin_skill_bundle(plugin_root: str) -> None:
    _validate_skill(f"{plugin_root}/skills/install-verifiedx/SKILL.md")
    _validate_skill(f"{plugin_root}/skills/verify-verifiedx/SKILL.md")
    _require_file(f"{plugin_root}/skills/install-verifiedx/references/supported-stacks.md")
    _require_file(f"{plugin_root}/skills/install-verifiedx/references/lower-seam-ts.md")
    _require_file(f"{plugin_root}/skills/install-verifiedx/references/lower-seam-py.md")
    _require_file(f"{plugin_root}/skills/install-verifiedx/references/mcp-ts.md")
    _require_file(f"{plugin_root}/skills/install-verifiedx/references/mcp-py.md")
    _require_file(f"{plugin_root}/skills/install-verifiedx/references/manual-explicit.md")
    _require_file(f"{plugin_root}/skills/install-verifiedx/references/langgraph-openai.md")
    _require_file(f"{plugin_root}/skills/install-verifiedx/references/langgraph-anthropic.md")
    _require_file(f"{plugin_root}/skills/verify-verifiedx/references/audit-checklist.md")


def main() -> int:
    _validate_skill("skills/install-verifiedx/SKILL.md")
    _validate_skill("skills/verify-verifiedx/SKILL.md")
    _require_file("skills/install-verifiedx/references/supported-stacks.md")
    _require_file("skills/install-verifiedx/references/lower-seam-ts.md")
    _require_file("skills/install-verifiedx/references/lower-seam-py.md")
    _require_file("skills/install-verifiedx/references/mcp-ts.md")
    _require_file("skills/install-verifiedx/references/mcp-py.md")
    _require_file("skills/install-verifiedx/references/manual-explicit.md")
    _require_file("skills/verify-verifiedx/references/audit-checklist.md")

    _validate_marketplace(".agents/plugins/marketplace.json", ["plugins/verifiedx"])
    codex_manifest = _load_json("plugins/verifiedx/.codex-plugin/plugin.json")
    _require(codex_manifest.get("name") == "verifiedx", "Codex plugin name must be `verifiedx`.")
    _require(codex_manifest.get("skills") == "./skills/", "Codex plugin skills path must be ./skills/.")

    _validate_marketplace(".claude-plugin/marketplace.json", ["claude/verifiedx"])
    claude_manifest = _load_json("claude/verifiedx/.claude-plugin/plugin.json")
    _require(claude_manifest.get("name") == "verifiedx", "Claude plugin name must be `verifiedx`.")

    _validate_marketplace(".cursor-plugin/marketplace.json", ["cursor/verifiedx"])
    cursor_manifest = _load_json("cursor/verifiedx/.cursor-plugin/plugin.json")
    _require(cursor_manifest.get("name") == "verifiedx", "Cursor plugin name must be `verifiedx`.")
    _require(cursor_manifest.get("skills") == "./skills/", "Cursor plugin skills path must be ./skills/.")
    _require(cursor_manifest.get("rules") == "./rules/", "Cursor plugin rules path must be ./rules/.")
    _require(cursor_manifest.get("logo") == "assets/logo.svg", "Cursor plugin logo must be assets/logo.svg.")
    _require((ROOT / "cursor/verifiedx/assets/logo.svg").exists(), "Missing Cursor plugin logo asset.")

    _validate_plugin_skill_bundle("plugins/verifiedx")
    _validate_plugin_skill_bundle("claude/verifiedx")
    _validate_plugin_skill_bundle("cursor/verifiedx")
    _require((ROOT / "cursor/verifiedx/rules/minimal-integration.mdc").exists(), "Missing Cursor rule file.")

    print("validated verifiedx-agent-skills packaging")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
