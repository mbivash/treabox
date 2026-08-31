from __future__ import annotations

from .domain import StoryIdea, TrendSignal


def rank_ideas(ideas: list[StoryIdea]) -> list[StoryIdea]:
    """Rank ideas from strongest to weakest using the current baseline scorer."""
    return sorted(ideas, key=lambda idea: idea.score, reverse=True)


def generate_seed_ideas(signal: TrendSignal, character: str = "bobo") -> list[StoryIdea]:
    """Create safe, original story seeds from a trend signal.

    This deliberately produces concepts rather than copying source videos.
    An LLM provider can later replace this function while preserving the domain model.
    """
    topic = signal.topic.strip()
    return [
        StoryIdea(
            title=f"{character.title()} discovers {topic}",
            premise=f"{character.title()} encounters an unexpected version of {topic} and makes everything worse.",
            hook=f"{character.title()} should NEVER have touched this.",
            structure="setup_escalation_twist",
            novelty=0.72,
            retention_potential=0.78,
            trend_fit=min(1.0, signal.score),
            production_cost=0.25,
        ),
        StoryIdea(
            title=f"The {topic} problem",
            premise=f"A tiny mistake involving {topic} turns into a ridiculous chain reaction.",
            hook=f"This tiny mistake changed everything.",
            structure="problem_escalation_payoff",
            novelty=0.68,
            retention_potential=0.74,
            trend_fit=min(1.0, signal.score),
            production_cost=0.20,
        ),
        StoryIdea(
            title=f"{character.title()} gets one chance",
            premise=f"{character.title()} has one attempt to solve a strange {topic} challenge.",
            hook=f"He had one chance. Then this happened.",
            structure="challenge_failure_twist",
            novelty=0.80,
            retention_potential=0.82,
            trend_fit=min(1.0, signal.score),
            production_cost=0.30,
        ),
    ]
