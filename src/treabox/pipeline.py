from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4

from .domain import Episode, EpisodeStatus, Scene, StoryIdea, TrendSignal
from .ideas import generate_seed_ideas, rank_ideas


@dataclass(slots=True)
class PipelineConfig:
    character: str = "bobo"
    target_duration_s: int = 45


class ContentPipeline:
    """Orchestrates the content factory without binding it to any vendor/API."""

    def __init__(self, config: PipelineConfig | None = None) -> None:
        self.config = config or PipelineConfig()

    def choose_idea(self, signal: TrendSignal) -> StoryIdea:
        ideas = generate_seed_ideas(signal, self.config.character)
        return rank_ideas(ideas)[0]

    def storyboard(self, idea: StoryIdea) -> list[Scene]:
        # Placeholder deterministic storyboard. Later an LLM adapter will emit the same Scene schema.
        return [
            Scene("s01", 4, "home", self.config.character, "walk", "neutral", "Something feels wrong.", "wide"),
            Scene("s02", 5, "street", self.config.character, "notice", "curious", "What is that?", "push_in"),
            Scene("s03", 7, "street", self.config.character, "touch", "surprised", "Oh no.", "close"),
            Scene("s04", 8, "chaos", self.config.character, "run", "terrified", "RUN!", "shake", ["impact"]),
            Scene("s05", 8, "chaos", self.config.character, "fall", "shocked", "Wait...", "zoom_out"),
            Scene("s06", 7, "mystery", self.config.character, "look_back", "afraid", "You opened it too.", "close"),
            Scene("s07", 6, "black", self.config.character, "freeze", "confused", "", "static"),
        ]

    def create_episode(self, signal: TrendSignal) -> Episode:
        idea = self.choose_idea(signal)
        scenes = self.storyboard(idea)
        return Episode(str(uuid4()), idea, scenes, EpisodeStatus.SCRIPTED)
