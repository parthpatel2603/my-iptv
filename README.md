# My Indian TV playlist for Stremio

Auto-builds `playlist.m3u` daily from iptv-org's free, publicly available channels (India + Gujarati).

## Setup (one time, ~5 minutes)
1. On github.com, click **New repository**, name it `my-iptv`, set it **Public**, create it.
2. Click **Add file → Upload files** and upload everything in this folder
   (including the `.github` folder — on PC, drag the whole folder in).
3. Go to **Actions** tab → **Update playlist** → **Run workflow**. Wait ~1 minute.
4. Your playlist link is:
   `https://raw.githubusercontent.com/<your-username>/my-iptv/main/playlist.m3u`

## Add to Stremio
Stremio → Addons → Community → search "IPTV" / "M3U" → Configure → paste the link above → Install.
Channels appear under Discover → TV on both PC and Android.

## Customize
Edit `keep.txt` on GitHub (pencil icon) to add/remove channel names, then Run workflow again.
