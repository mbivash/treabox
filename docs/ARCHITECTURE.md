# TREABOX architecture

## Phase 1 — prove the factory

The first milestone is one command that can turn a trend signal into a valid episode JSON. Rendering and publishing are adapters, so the core remains testable without credentials.

### 1. Trend adapters

Interface:

```python
class TrendSource:
    def fetch(self) -> list[TrendSignal]: ...
```

Adapters will eventually cover YouTube trends/search, Google Trends, Reddit, news and platform-specific signals. They provide evidence, not content to repost.

### 2. Idea engine

Input: normalized trend signals + historical channel performance.

Output: many original story concepts.

Scoring dimensions:

- hook strength
- novelty
- trend fit
- expected retention
- production cost
- character/world fit
- historical similarity penalty

Later: replace heuristic weights with a learned model trained on our own published episodes.

### 3. Story engine

LLM provider produces a structured storyboard, not free-form video prompts. The output must conform to the `Scene` schema.

Hard constraints:

- recurring character IDs only
- allowed actions only
- target duration
- no copyrighted character imitation
- original dialogue
- scene-level visual instructions

### 4. Deterministic animation engine

The first renderer should use vector/2D primitives. Bobo is built from stable shapes and an action library. This avoids character drift and reduces generation cost.

Potential implementation options: SVG/canvas, Remotion, or a lightweight Python renderer. The renderer consumes `Scene` objects and outputs scene clips.

### 5. Audio engine

Adapters for TTS, background music and SFX. Keep the audio manifest separate so assets can be swapped without rewriting the episode.

### 6. Video assembler

FFmpeg-based composition:

- 9:16 output
- 1080x1920 target
- loudness normalization
- subtitles/captions
- intro/hook timing
- end card only when useful

### 7. Publishing adapters

Each platform is isolated behind:

```python
class Publisher:
    def publish(self, video_path, metadata) -> str: ...
```

Prefer official APIs and comply with platform rules. Browser automation is a fallback only where permitted and technically necessary.

### 8. Analytics + learning

Store per-episode:

- impressions/views
- average watch time
- retention curve when available
- likes/comments/shares
- follows/subscribers
- link/affiliate/lead conversions
- revenue

The optimizer should eventually predict **expected revenue per produced episode**, not simply views.

## Phase 2 — autonomous loop

```text
collect → cluster → generate 50 ideas → score → script top 5
→ render → quality gate → publish → measure → learn → repeat
```

A quality gate must be able to reject an episode before publishing.

## Phase 3 — multi-channel portfolio

Use the same underlying episode to produce platform-specific metadata and safe variants, while avoiding duplicate spam. The system can maintain multiple channels/universes once the first channel demonstrates repeatable performance.

## Non-goals

- reposting copyrighted videos
- artificial views/likes/comments
- bypassing platform anti-spam controls
- promising guaranteed income

## Definition of success

The project is successful when it can operate a real channel for 30 days with minimal manual intervention and demonstrate measurable improvement in content performance over successive batches.
