import trafilatura, requests

sources = [
    ("M10 S6", "https://livingwaters.com/how-to-witness-to-intellectuals/",
     "level-2-evangelism/10-evangelism-in-everyday-life/RayComfort_HowToWitnessToIntellectuals_LivingWaters.txt"),
    ("M5 S1", "https://carm.org/world-religions/buddhism/",
     "level-3-apologetics/5-buddhism/CARM_Buddhism_MainHub_Overview.txt"),
    ("M5 S4", "https://livingwaters.com/how-to-witness-to-a-buddhist/",
     "level-3-apologetics/5-buddhism/LivingWaters_HowToWitnessToABuddhist.txt"),
]

BASE = "C:/Users/Trade/Desktop/Projects/Preach/IDE/Resources"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

for name, url, rel_path in sources:
    path = f"{BASE}/{rel_path}"
    print(f"\n=== {name} ===")
    print(f"  URL: {url}")

    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        downloaded = resp.text

        # Try with different extraction settings
        result = trafilatura.extract(
            downloaded,
            output_format="txt",
            include_links=True,
            favor_recall=True,
            no_fallback=False,
        )

        if result and len(result.strip()) > 200:
            content = f"{url}\n\n{result.strip()}"
            with open(path, "w", encoding="utf-8", errors="replace") as f:
                f.write(content)
            print(f"  OK: {len(content)} chars")
        else:
            print(f"  STILL LOW: {len(result) if result else 0} chars")
            print(f"  Raw preview: {downloaded[:500]}")

    except Exception as e:
        print(f"  ERROR: {e}")
