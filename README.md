# Azhi Campaign

A D&D 5e setting on a ring-shaped world, the corpse of Azhi, the philosopher dragon who ate itself.

- **Claude, start here:** `CLAUDE.md`
- **Plan and checklist:** `PLAN.md`
- **Setting facts:** `canon/setting-bible.md` · **Decisions:** `canon/decisions.md` · **Myth:** `canon/azhi-myth.md`
- **Maps:** `worldgen/` · **Art:** `art/` · **Rules (from Phase 1):** `srd/`

![The world of Azhi](worldgen/output/azhi_flat_map.png)

## Push to a git host (one time)

Preferred: Codeberg (Troy would rather not use GitHub).

Create an **empty private** repo named `azhi-campaign`, with no README. Then, from inside this folder:

```
git remote add origin https://codeberg.org/<your-username>/azhi-campaign.git
git branch -M main
git push -u origin main
```

To let Claude push directly, add `codeberg.org` to the allowed domains in Claude's settings (Settings → Capabilities), and give the session a token limited to this repo.

## Claude Project

See `project-instructions.md` for the custom-instructions text and the list of knowledge files.
