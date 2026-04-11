import numpy as np
import gymnasium as gym
from gymnasium import spaces
from tasks import tasks


class TicketTriageEnv(gym.Env):
    def __init__(self, task: tasks.Task = tasks.Task.EASY):
        super().__init__()

        self.task = task

        # 0 = Low, 1 = Medium, 2 = High
        self.action_space = spaces.Discrete(3)

        # 10 numerical features
        self.observation_space = spaces.Box(
            low=0.0, high=1.0, shape=(10,), dtype=np.float32
        )

        self.state = None

    # -------- RESET --------
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        # Task-based difficulty
        if self.task == tasks.Task.EASY:
            self.state = np.random.rand(10) * 0.3
        elif self.task == tasks.Task.MEDIUM:
            self.state = np.random.rand(10) * 0.6
        else:
            self.state = np.random.rand(10)

        return self.state.astype(np.float32), {}

    # -------- STEP --------
    def step(self, action):
        # Simple rule-based ground truth
        score = np.sum(self.state)

        if score < 3:
            correct_action = 0   # Low
        elif score < 6:
            correct_action = 1   # Medium
        else:
            correct_action = 2   # High

        # Reward
        reward = 1.0 if action == correct_action else 0.0

        # Next state
        self.state = np.random.rand(10).astype(np.float32)

        terminated = True   # single-step env
        truncated = False

        info = {
            "correct_action": correct_action
        }

        return self.state, reward, terminated, truncated, info