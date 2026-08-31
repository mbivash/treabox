from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class EpisodeStatus(str, Enum):
    IDEA = "idea"
    SCRIPTED = "scripted"
    RENDERED = "rendered"
    PUBLISHED = "published"
    MEASURED = "measured"
    FAILED = "failed"


@dataclass(slots=True)
class TrendSignal:
    topic: str
    source: str
    score: float = 0.0
    evidence_url: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class StoryIdea:
    title: str
    premise: str
    hook: str
    structure: str
    novelty: float = 0.0
    retention_potential: float = 0.0
    trend_fit: float = 0.0
    production_cost: float = 0.0

    @property
    def score(self) -> float:
        # Weighted for short-form storytelling; production cost is a penalty.
        return (
            0.30 * self.retention_potential
            + 0.25 * self.hook_score()
            + 0.20 * self.novelty
            + 0.15 * self.trend_fit
            - 0.10 * self.production_cost
        )

    def hook_score(self) -> float:
        # Initial deterministic heuristic; replace/augment with learned model later.
        words = self.hook.split()
        curiosity = any(w.lower() in {"never", "secret", "why", "impossible", "until", "wrong", "mystery"} for w in words)
        return min(1.0, len(words) / 12.0 + (0.25 if curiosity else 0.0))


@dataclass(slots=True)
class Scene:
    scene_id: str
    duration_s: float
    background: str
    character: str
    action: str
    emotion: str = "neutral"
    dialogue: str = ""
    camera: str = "static"
    sfx: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Episode:
    episode_id: str
    idea: StoryIdea
    scenes: list[Scene]
    status: EpisodeStatus = EpisodeStatus.IDEA
    output_path: str | None = None
    platform_ids: dict[str, str] = field(default_factory=dict)
    metrics: dict[str, float] = field(default_factory=dict)
