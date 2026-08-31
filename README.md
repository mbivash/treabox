# TREABOX — Autonomous Short-Video Content Factory

> Research-first automation system for generating original short-form stories, rendering deterministic character animation, publishing to YouTube/Instagram/Facebook, and learning from performance.

## Vision

TREABOX is **not a SaaS**. It is an automation engine for operating one or more content channels with minimal manual work.

The initial format is a recurring minimalist stick-character story universe. The system should:

1. Discover trends and proven story patterns.
2. Generate original ideas without copying source videos.
3. Score ideas for hook strength, novelty, retention potential, and production cost.
4. Turn the selected idea into a structured script/storyboard.
5. Render scenes from deterministic character/action primitives.
6. Generate narration, music and sound effects.
7. Assemble a vertical MP4.
8. Generate platform-specific metadata.
9. Publish to YouTube Shorts, Instagram Reels and Facebook Reels through supported APIs/automation adapters.
10. Collect analytics and feed results back into idea scoring.

## Core principle

**Steal the signal, not the content.** TREABOX may learn from public trends and successful formats, but generated videos must be original and must not simply download/repost other creators' copyrighted videos.

## Architecture

```text
Trend Sources
     |
     v
Trend Normalizer ---> Pattern Library
     |                     |
     +---------> Idea Engine
                    |
                    v
               Idea Scorer
                    |
                    v
              Story Generator
                    |
                    v
              Scene Plan JSON
                    |
        +-----------+-----------+
        |           |           |
   Animation      Voice       Audio
        |           |           |
        +-----------+-----------+
                    |
                    v
              FFmpeg Renderer
                    |
                    v
             Platform Metadata
                    |
        +-----------+-----------+
        |           |           |
       YouTube   Instagram   Facebook
        |           |           |
        +-----------+-----------+
                    |
                    v
                 Metrics
                    |
                    v
             Learning Engine
                    |
                    +------> Idea Scorer
```

## Repository layout

- `src/treabox/domain.py` — shared data models and validation.
- `src/treabox/ideas.py` — deterministic idea scoring primitives.
- `src/treabox/pipeline.py` — orchestration state machine.
- `config/character.json` — initial character universe.
- `config/story_templates.json` — reusable story structures.
- `docs/ARCHITECTURE.md` — implementation plan and decisions.
- `examples/episode.json` — example scene plan.

## Status

**Phase 0 — foundation.** No automatic posting or real-money service is enabled by default. The next milestones are trend adapters, LLM provider adapters, deterministic 2D rendering, TTS, FFmpeg assembly, and platform publishing adapters.

## Safety / platform compliance

Publishing adapters should use official APIs where available and respect each platform's terms, rate limits, copyright rules, spam policies, and monetization requirements. Credentials belong in environment variables or a secret manager, never in Git.
