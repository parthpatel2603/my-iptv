"""Builds playlist.m3u from iptv-org's free, public India + Gujarati lists.
Edit keep.txt to choose channels (one name fragment per line). Empty = keep all."""
import urllib.request, re, pathlib

SOURCES = [
    "https://iptv-org.github.io/iptv/countries/in.m3u",
    "https://iptv-org.github.io/iptv/languages/guj.m3u",
]
root = pathlib.Path(__file__).parent
keep = [l.strip().lower() for l in (root / "keep.txt").read_text(encoding="utf-8").splitlines()
        if l.strip() and not l.startswith("#")]

seen, out = set(), ["#EXTM3U"]
for src in SOURCES:
    lines = urllib.request.urlopen(src, timeout=60).read().decode("utf-8", "ignore").splitlines()
    for info, url in zip(lines, lines[1:]):
        if not info.startswith("#EXTINF") or not url.startswith("http"):
            continue
        name = info.rsplit(",", 1)[-1].strip()
        if url in seen or (keep and not any(k in name.lower() for k in keep)):
            continue
        seen.add(url)
        out += [info, url]

(root / "playlist.m3u").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"Wrote {len(seen)} channels")
