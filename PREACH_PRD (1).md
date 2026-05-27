# PREACH — Product Requirements Document (PRD)
**Version:** 1.4  
**Status:** Draft  
**Prepared for:** Development Handoff  

---

## 1. Overview

### 1.1 Product Name
**PREACH**

### 1.2 Tagline
*Know it. Share it. Defend it.*

### 1.3 Mission Statement
PREACH is a mobile application that equips Christians to know what they believe, share the gospel confidently, and defend their faith against common objections from opposing worldviews. It combines structured learning, memory verse drilling, prayer habit building, and a testimony-driven community to build a generation of equipped, grounded, and bold believers.

---

## 2. Problem Statement

Many Christians want to share their faith but don't fully understand core biblical doctrine, don't know how to start a gospel conversation, and can't respond when challenged by Muslims, Jehovah's Witnesses, Mormons, Atheists, or Buddhists. Existing resources are scattered across books, YouTube videos, and Bible apps. There is no single, focused, mobile-first tool that takes a believer from foundational doctrine all the way through evangelism training and apologetics defense.

---

## 3. Target Users

### Primary Users
- **Any Christian** wanting to grow in their ability to know, share, and defend the gospel
- **New & young Christians** who need to be grounded in foundational doctrine before going out

### Secondary Users
- **Church leaders and pastors** training their congregations — assigning levels based on maturity

---

## 4. Platform

- **Mobile First:** iOS and Android
- **Framework:** React Native (recommended for cross-platform parity)
- **Web app:** Not in scope for v1

---

## 5. The Three Levels

PREACH is structured as a **progressive journey** through three levels. Each level builds on the last. Users are routed to the right level during onboarding but can access any level.

```
LEVEL 1 — FOUNDATIONS
"Know What You Believe"
The bedrock. Foundational Christian doctrine.
Every new believer starts here.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEVEL 2 — EVANGELISM
"Share What You Believe"
Practical training to go out and win souls.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEVEL 3 — APOLOGETICS
"Defend What You Believe"
Respond to every argument from every worldview.
```

---

## 6. Content Structure

### 6.1 Lesson Structure Per Module

Every module across all three levels follows this exact structure:

```
Module: [Title]
├── Lesson 1 — [Title]
├── Lesson 2 — [Title]
├── Lesson 3 — [Title]
├── Lesson 4 — [Title]
├── Lesson 5 — [Title]
├── Lesson 6 — [Title]
├── Lesson 7 — [Title]
└── Review
    ├── Flashcard Deck
    └── Memory Verse Drill
```

### 6.2 Individual Lesson Content Structure

Each lesson contains:
- **Hook** — Opening question or real-world scenario to grab attention
- **Core Teaching** — Main content with scripture references
- **Key Scriptures** — 2–4 relevant verses with translation label
- **Practical Application** — "Here's how you use this in a real conversation"
- **Summary** — 3-bullet recap
- **Next Lesson Preview** — One line teasing what comes next

### 6.3 Apologetics Lesson Structure

Each worldview module follows this specific lesson order:
1. What they believe (overview)
2. Key differences from Biblical Christianity
3. Their most common arguments (top 5–10)
4. How to respond — argument by argument, with scripture
5. Dos and don'ts when engaging
6. A real conversation walkthrough
7. Flashcard + Memory Verse review

---

## 7. Full Content Map

---

### LEVEL 1 — FOUNDATIONS (10 Modules)
*Know What You Believe*

1. **Who Is God?** — The nature, character and attributes of God
2. **The Trinity** — Father, Son and Holy Spirit — one God, three persons
3. **Creation** — Genesis 1, John 1 — God as the author of all things
4. **Who Is Man?** — Created in God's image, the fall, the nature of sin
5. **Who Is Jesus?** — Fully God, fully man — the incarnation and why it matters
6. **The Cross & Resurrection** — What happened, why it happened, what it means
7. **The Authority of Scripture** — Why the Bible is God's Word and can be trusted
8. **Salvation & Grace** — What it truly means to be saved — not works, not religion
9. **The Holy Spirit** — Who He is and His role in the believer's life
10. **Heaven, Hell & Eternity** — What the Bible actually says about what comes after

---

### LEVEL 2 — EVANGELISM (12 Modules)
*Share What You Believe*

1. **What Is the Gospel?** — The core message in its fullness *(entirely free — the gospel is free)*
2. **Why Souls Matter** — Eternity, urgency, God's heart for the lost
3. **The Role of the Holy Spirit in Evangelism** — You cannot do this alone
4. **Starting the Conversation** — Opening doors naturally in everyday life
5. **Sharing Your Testimony** — Structuring your story for maximum impact
6. **Understanding Who You're Talking To** — Reading your audience
7. **Leading Someone to Christ** — Walking someone through salvation step by step
8. **What You're Asking Someone to Do** — The cost, the surrender, the reward
9. **Overcoming Fear & Rejection** — Pushing past hesitation and doubt
10. **Evangelism in Everyday Life** — Workplace, family, social settings
11. **Using Scripture in Conversation** — Naturally, confidently, not forcefully
12. **Praying for the Lost + Follow-Up & Discipleship** — Intercession and what comes after

---

### LEVEL 3 — APOLOGETICS (5 Worldviews → Expanding)
*Defend What You Believe*

1. **Islam** — What they believe, key differences, how to respond
2. **Jehovah's Witnesses** — Doctrinal disputes, door-to-door scenarios
3. **Mormonism (LDS)** — Key differences, talking points
4. **Atheism** — Evolution, problem of evil, science vs. faith
5. **Buddhism** — Core beliefs, contrast with Christianity, how to engage

*Post v1 worldviews: Catholicism, Hinduism, New Age, Secular Humanism*

---

## 8. Content Research & Creation Pipeline

### 8.1 Research Phase (Before Writing)

Content must be researched thoroughly before drafting begins. Use one NotebookLM notebook per module or worldview.

#### Recommended Sources

**For Foundations & Evangelism:**
- **Kenneth Hagin** — KHM.org, YouTube — Holy Spirit, faith, authority of the believer
- **Paul Washer** — HeartCry Missionary Society YouTube, heartcrymissionary.com — true gospel, grace
- **Voddie Baucham** — YouTube, *"Expository Apologetics"* — scripture authority, doctrine
- **Reverend Peter Alabi** — Prayer, Holy Spirit, West African church context
- **Ray Comfort / Living Waters** — livingwaters.com, YouTube — practical street evangelism
- **Reinhard Bonnke** — *"Evangelism by Fire"* — soul-winning, passion for the lost
- **Charles Spurgeon** — spurgeon.org — public domain sermons on soul-winning
- **Billy Graham** — billygraham.org — free structured evangelism training materials
- **Andrew Murray** — *"With Christ in the School of Prayer"* — public domain, prayer

**For Apologetics:**
- **David Wood** — Acts17Apologetics YouTube + website — Islam, atheism
- **Sam Shamoun** — answeringislam.org — deep Islam apologetics
- **GodLogic** — YouTube — general apologetics, atheism
- **Stand to Reason** — str.org — general apologetics
- **CARM** — carm.org — JW, Mormonism, cults
- **Voddie Baucham** — *"Expository Apologetics"* — scripture-based defense

### 8.2 NotebookLM Research Workflow
1. Pull YouTube transcripts from relevant teachers per topic
2. Download/copy written content from recommended websites
3. Upload all sources into a dedicated NotebookLM notebook per topic
4. Use NotebookLM to synthesize into a structured study guide
5. Feed study guide into Claude to draft lesson content in PREACH format
6. Human theologian/pastor reviews draft for accuracy
7. Approved content uploaded to CMS

### 8.3 Content Review & Approval
- All content reviewed by at least one qualified pastor or theologian before publishing
- Scripture references verified against primary translations
- **Critical:** Reviewer must be identified and committed before launch
- Reviewer uses CMS dashboard (no code required) to approve or request edits

### 8.4 Content Release Schedule
- **v1 Launch:** All of Level 1 (Foundations) + Level 2 Modules 1–2 + Islam + Atheism (Level 3)
- **Month 2:** Level 2 Modules 3–6 + JW + Mormonism (Level 3)
- **Month 3:** Level 2 Modules 7–12 + Buddhism (Level 3)
- **Ongoing:** New content monthly to retain premium subscribers

---

## 9. Bible Translations & Scripture API

### 9.1 Primary Translations (v1)
- **New King James Version (NKJV)** — Primary translation
- **New Living Translation (NLT)** — Accessible modern translation
- **King James Version (KJV)** — Public domain, free to use
- **Kenneth Wuest Expanded Translation** — Word-for-word expanded Greek NT; verify licensing before committing

### 9.2 Bible Scripture API
- **Recommended:** API.Bible (api.bible) — free tier, includes NKJV, NLT, KJV and 2,000+ translations
- Developer registers for a free API key
- App fetches any verse on demand by reference (e.g. John 3:16)
- KJV can be bundled directly (fully public domain)
- Wuest translation: verify separately — may require direct publisher licensing

---

## 10. Feature Breakdown

### 10.1 User Accounts & Authentication
- Email/password sign up and login
- Social login (Google, Apple)
- **Auth provider:** Firebase Authentication
- User profile: name, profile photo, church (optional)
- Progress, streaks, and history saved to account
- Push notifications via Firebase Cloud Messaging (FCM)

---

### 10.2 Flashcard Review
- Shown at the end of every module as a review tool
- Users can also access flashcard decks independently
- Simple flip-card UI: question on front, answer on back
- User marks each card as "Got it" or "Review again"
- Contributes to the daily review streak

---

### 10.3 Memory Verse Drill

Two drill modes per module:

#### Mode 1 — Reference Mode
- Full verse text is displayed
- Scripture reference is hidden
- User identifies the correct reference from multiple choice options
- Tests *recognition*

#### Mode 2 — Completion Mode
- Scripture reference is shown
- Part of the verse text is blanked out
- User completes the missing words — typing or multiple choice
- Tests *recall*

#### Scoring
- Each drill session is scored (e.g. 7/10)
- Score saved to profile — users can re-drill to beat their score
- Completing a daily drill contributes to the Memory Verse Streak

---

### 10.4 Streaks System

Three separate streaks shown on the home dashboard:

| Streak | Trigger | Always Free? |
|--------|---------|--------------|
| 📚 Study Streak | Completing at least one lesson per day | Yes |
| 🙏 Prayer Streak | Tapping "I prayed today" | Yes |
| ✍️ Memory Verse Streak | Completing a memory verse drill | Yes |

- All streaks always free — core to the mission
- Milestone badges: 7 days, 30 days, 100 days per streak

---

### 10.5 Prayer Reminder & Prayer Streak
- Users set daily prayer reminder time(s) during onboarding or settings
- Push notification via Firebase Cloud Messaging (FCM)
- Encouraging mission-focused messages
- User taps "I prayed today" to log and maintain streak
- Always free — prayer is never behind a paywall

---

### 10.6 What Happens After All Content Is Finished

**Default — Community Becomes the Product:**
Once all content is completed, users shift toward active field work. The learning was training — now the world is their classroom. The community testimony feed is where they report back.

**Supporting strategies:**
- New lessons released monthly — premium subscribers always have something new
- Users re-drill flashcards and memory verses for higher scores

---

### 10.7 Community — Testimony Feed

#### Post Types
1. **🙏 Soul Saved** — Someone came to Christ
2. **⚔️ Argument Won** — Successfully defended the faith
3. **📖 Milestone** — Completed a module, hit a streak, earned a badge

#### Post Structure
- Post type tag
- Short testimony (280 character limit)
- Optional: worldview engaged / module completed
- Reactions: 🙏 Praise God, 🔥 Keep Going (no like counts)
- Comments: short encouragement replies

#### Feed Rules
- No follower counts, no vanity metrics
- No promotional content
- Moderated via report button
- Always free to access and post

---

### 10.8 Quick Prep Mode
- User picks a worldview and gets a rapid-fire cheat sheet
- Top 3 arguments + top 3 responses
- Available after completing that worldview's module
- Free for worldviews the user has already completed

---

### 10.9 Verse of the Day
- Daily scripture on the home screen tied to current level/module
- Always free

---

### 10.10 Share a Flashcard
- Users share any flashcard to WhatsApp, Instagram Stories, etc.
- Branded with PREACH logo
- Free organic marketing

---

## 11. Onboarding Flow

**Goal: Get the user to their first lesson in under 90 seconds.**

```
Screen 1 — Welcome
"PREACH. Know it. Share it. Defend it."
[Get Started]

Screen 2 — Where are you in your faith journey?
○ I'm new to Christianity — start me at the beginning
○ I know my faith — I want to learn to share it
○ I'm ready to defend my faith against tough arguments
○ I want to go through everything from the start
(Routes them to the correct level)

Screen 3 — Your background
○ I'm a new Christian (less than 2 years)
○ I've been a Christian for a while
○ I'm a church leader / pastor

Screen 4 — Set your prayer reminder
"When do you want to pray each day?"
[Time picker]
[Set My Reminder] / [Skip for now]

Screen 5 — Create your account
Name, Email, Password
─── or ───
[Continue with Google]
[Continue with Apple]

Screen 6 — First lesson begins immediately
Routed straight into Lesson 1 of their chosen level.
No extra steps. No extra screens.
```

---

## 12. Monetization — Freemium

### Free Tier
- **Level 1, Module 1 (Who Is God?)** — Entirely free, all lessons
- **Level 2, Module 1 (What Is the Gospel?)** — Entirely free, all lessons *(the gospel is free)*
- **First lesson of every other module** across all three levels
- Locked lessons visible but grayed out with lock icon
- All three streaks — always free
- Community testimony feed — always free
- Prayer reminders — always free
- Verse of the Day — always free

### Premium Tier
- All lessons unlocked across all levels and worldviews
- Full flashcard decks
- Full memory verse drill decks
- Quick Prep Mode (all worldviews)
- Early access to new content

### Pricing (TBD)
- Monthly: $4.99–$7.99/month
- Annual: $34.99–$49.99/year
- 7-day free trial recommended for all new users

---

## 13. Navigation & Information Architecture

```
PREACH App
├── Home (Dashboard)
│   ├── Study + Prayer + Memory Verse streaks
│   ├── Verse of the Day
│   ├── Continue where you left off
│   └── Recommended next lesson
│
├── Learn
│   ├── Level 1 — Foundations (10 Modules)
│   ├── Level 2 — Evangelism (12 Modules)
│   └── Level 3 — Apologetics (5 Worldviews)
│
├── Review
│   ├── Flashcards (by module)
│   └── Memory Verse Drill (by module)
│
├── Quick Prep
│   └── Pick a worldview → cheat sheet
│
├── Community (Testimony Feed)
│   ├── Feed
│   └── Post a Win
│
└── Profile
    ├── Progress & badges
    ├── All three streak histories
    └── Settings (prayer reminders, notifications, subscription)
```

---

## 14. Technical Stack

| Layer | Technology | Reason |
|-------|-----------|--------|
| Frontend | React Native | Cross-platform iOS + Android |
| Database | Firebase Firestore | Real-time, scalable, Firebase ecosystem |
| Authentication | Firebase Auth | Consistency |
| Push Notifications | Firebase Cloud Messaging (FCM) | Prayer reminders, streaks, community |
| Content Management | Sanity or Contentful (v1: Google Sheets) | Update lessons without app store releases |
| Bible Scripture | API.Bible | Free API, includes NKJV, NLT, KJV |
| Payments | RevenueCat | Industry standard for in-app subscriptions |

---

## 15. Admin & Moderation — V1

No custom admin panel in v1. Use existing free tools:

| Task | Tool |
|------|------|
| View user data & stats | Firebase Console |
| Add/edit/update lesson content | CMS dashboard |
| Review flagged community posts | Manual review (founder, ~15 min/day) |
| Track subscriptions & revenue | RevenueCat dashboard |

**V2 Admin Panel** — needed at scale (10,000+ users) for volume moderation, targeted notifications, drop-off analytics, and church leader dashboards.

---

## 16. Legal Checklist (Before Launch)

- [ ] Privacy Policy
- [ ] Terms of Service
- [ ] Apple Developer Account ($99/year)
- [ ] Google Play Developer Account ($25 one-time)
- [ ] API.Bible account and API key
- [ ] RevenueCat account
- [ ] Bible translation licensing verified (NKJV, NLT, Wuest)
- [ ] All content reviewed and approved by theologian before launch

---

## 17. Success Metrics (v1)

| Metric | Target (3 months post-launch) |
|--------|-------------------------------|
| Downloads | 5,000+ |
| Daily Active Users (DAU) | 500+ |
| Module completion rate | > 40% |
| Free → Premium conversion | > 5% |
| Community posts | 200+ |
| Average session length | > 5 minutes |
| D7 retention | > 30% |
| Prayer streak (7-day) rate | > 20% of active users |

---

## 18. Out of Scope (v1)

- AI-powered features of any kind
- AI Roleplay (possible v2 — not confirmed)
- Video content
- Web app
- Worldviews beyond the 5 in v1
- Church admin dashboard
- Custom admin panel
- Multi-language support
- Offline mode

---

## 19. v2 Roadmap (Post-Launch — To Be Confirmed)

- Church/org accounts with congregation progress tracking
- Expanded apologetics worldviews
- Custom admin dashboard
- Video lessons
- Multi-language support (French + Spanish first)
- Web app companion
- AI Roleplay (under consideration)

---

## 20. Design Principles

- **Mission-first:** Every feature serves the goal of equipping believers.
- **Progressive by design:** Users grow through levels — foundations before evangelism, evangelism before apologetics.
- **Simple over clever:** Any believer starts learning within 90 seconds of opening the app.
- **Encouraging, not shaming:** The app celebrates wins and never punishes falling behind.
- **Testimony over metrics:** Community is built on stories, not numbers.
- **Theologically grounded:** Speed never overrides accuracy. Human review is non-negotiable.
- **Prayer is non-negotiable:** Prayer features are always free.
- **The gospel is free:** Level 2 Module 1 is always free. No exceptions.

---

*Document version 1.4 — Three-level structure confirmed. Ready for design and development handoff.*
