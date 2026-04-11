from enum import Enum

class Task(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

TASK_DESCRIPTIONS = {
    Task.EASY:   "Simple queries (password reset, basic issues)",
    Task.MEDIUM: "Moderate issues (billing, account problems)",
    Task.HARD:   "Complex issues (technical bugs, escalations)"
}