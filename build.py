"""Builds playlist.m3u from iptv-org's free, public India + Gujarati lists.
Edit keep.txt to choose channels (one name fragment per line). Empty = keep all."""
import urllib.request, re, pathlib

SOURCES = [
    "https://iptv-org.github.io/iptv/countries/in.m3u",   # all channels from India
    "https://iptv-org.github.io/iptv/languages/guj.m3u",  # Gujarati
    "https://iptv-org.github.io/iptv/languages/hin.m3u",  # Hindi (incl. channels outside India)
    "https://iptv-org.github.io/iptv/languages/mar.m3u",  # Marathi
    "https://iptv-org.github.io/iptv/languages/pan.m3u",  # Punjabi
    "https://iptv-org.github.io/iptv/languages/tam.m3u",  # Tamil
    "https://iptv-org.github.io/iptv/languages/tel.m3u",  # Telugu
    "https://iptv-org.github.io/iptv/languages/ben.m3u",  # Bengali
    "https://iptv-org.github.io/iptv/languages/mal.m3u",  # Malayalam
    "https://iptv-org.github.io/iptv/languages/kan.m3u",  # Kannada
    "https://raw.githubusercontent.com/Free-TV/IPTV/master/playlists/playlist_india.m3u8",  # Free-TV project (only free-to-air)
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
