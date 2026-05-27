import trafilatura
import requests
import os
import sys
import traceback
from pathlib import Path

sources = [
    # === M10: Evangelism in Everyday Life ===
    {
        "url": "https://livingwaters.com/witnessing-to-family-members/",
        "path": "level-2-evangelism/10-evangelism-in-everyday-life/RayComfort_WitnessingToFamilyMembers_LivingWaters.txt",
    },
    {
        "url": "https://livingwaters.com/episode/how-to-witness-to-family-and-friends/",
        "path": "level-2-evangelism/10-evangelism-in-everyday-life/RayComfort_HowToWitnessToFamilyAndFriends_Podcast_Ep123.txt",
    },
    {
        "url": "https://disntr.com/2019/03/14/voddie-bauchams-tips-for-evangelism/",
        "path": "level-2-evangelism/10-evangelism-in-everyday-life/VoddieBaucham_EvangelismTipsIntentional_Everyday.txt",
    },
    {
        "url": "https://livingwaters.com/how-to-witness-to-intellectuals/",
        "path": "level-2-evangelism/10-evangelism-in-everyday-life/RayComfort_HowToWitnessToIntellectuals_LivingWaters.txt",
    },
    # === M11: Using Scripture in Conversation ===
    {
        "url": "https://livingwaters.com/nutshell-answers-to-the-top-ten-objections-to-christianity/",
        "path": "level-2-evangelism/11-using-scripture-in-conversation/RayComfort_NutshellAnswersTop10Objections_LivingWaters.txt",
    },
    {
        "url": "https://www.bravethebattle.com/post/street-preacher-s-gospel-sharing-outline",
        "path": "level-2-evangelism/11-using-scripture-in-conversation/RayComfort_StreetPreacherGospelOutline_HowToUseScripture.txt",
    },
    # === M5: Buddhism ===
    {
        "url": "https://carm.org/world-religions/buddhism/",
        "path": "level-3-apologetics/5-buddhism/CARM_Buddhism_MainHub_Overview.txt",
    },
    {
        "url": "https://carm.org/buddhism/is-buddhism-compatible-with-christianity/",
        "path": "level-3-apologetics/5-buddhism/CARM_IsBuddhismCompatibleWithChristianity.txt",
    },
    {
        "url": "https://carm.org/buddhism/do-buddhism-and-christianity-have-common-ground-in-ethics/",
        "path": "level-3-apologetics/5-buddhism/CARM_Buddhism_ChristianityEthicsComparison.txt",
    },
    {
        "url": "https://livingwaters.com/how-to-witness-to-a-buddhist/",
        "path": "level-3-apologetics/5-buddhism/LivingWaters_HowToWitnessToABuddhist.txt",
    },
    {
        "url": "https://livingwaters.com/how-to-witness-to-those-in-cults-and-other-religions/",
        "path": "level-3-apologetics/5-buddhism/LivingWaters_HowToWitnessToOtherReligions_AllCults.txt",
    },
    {
        "url": "https://www.namb.net/apologetics/resource/buddhism/",
        "path": "level-3-apologetics/5-buddhism/NAMB_Buddhism_Apologetics_WitnessingGuide.txt",
    },
    {
        "url": "https://cbn.com/article/not-selected/what-makes-christian-message-unique-0",
        "path": "level-3-apologetics/5-buddhism/RaviZacharias_BuddhismHinduismResponse_CBN.txt",
    },
    {
        "url": "https://www.apologeticsindex.org/2647-buddhism",
        "path": "level-3-apologetics/5-buddhism/ApologeticsIndex_Buddhism_ResourceHub.txt",
    },
    {
        "url": "https://www.biblicaltraining.org/learn/institute/wm646-buddhism/wm646-12-explorations-in-buddhist-apologetics-1",
        "path": "level-3-apologetics/5-buddhism/BiblicalTraining_TennentBuddhismApologetics_Part1.txt",
    },
]

BASE = Path("C:/Users/Trade/Desktop/Projects/Preach/IDE/Resources")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

for s in sources:
    url = s["url"]
    rel_path = s["path"]
    out_path = BASE / rel_path

    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\n=== {rel_path} ===")
    print(f"  URL: {url}")

    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded is None:
            # Try with requests directly
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            downloaded = resp.text

        result = trafilatura.extract(
            downloaded,
            output_format="txt",
            include_links=True,
            include_tables=True,
            include_images=False,
            include_formatting=True,
            favor_precision=True,
        )

        if result and len(result.strip()) > 200:
            content = f"{url}\n\n{result.strip()}"
            with open(str(out_path), "w", encoding="utf-8", errors="replace") as f:
                f.write(content)
            print(f"  OK: {len(content)} chars → {out_path.name}")
        else:
            print(f"  FAIL: extracted too little ({len(result) if result else 0} chars)")
    except Exception as e:
        print(f"  ERROR: {e}")
