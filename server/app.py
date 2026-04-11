from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import uvicorn

from env.ticket_env import TicketTriageEnv
from tasks.tasks import Task   # ✅ FIXED IMPORT

app = FastAPI()

# -------- REQUEST MODEL --------
class ActionRequest(BaseModel):
    action: int
    task: Task = Task.EASY   # ✅ FIXED TYPE

    @field_validator("action")   # ✅ pydantic v2 syntax
    def validate_action(cls, v):
        if v not in (0, 1, 2):
            raise ValueError("action must be 0, 1, or 2")
        return v


# -------- RESET --------
@app.post("/reset")
def reset(task: Task = Task.EASY):
    env = TicketTriageEnv(task=task)
    app.state.env = env

    state, _ = env.reset()
    return {
        "state": state.tolist(),
        "task": task.value   # ✅ return string
    }


# -------- STEP --------
@app.post("/step")
def step(req: ActionRequest):
    env = getattr(app.state, "env", None)

    if env is None:
        raise HTTPException(status_code=400, detail="Call /reset first")

    state, reward, terminated, truncated, info = env.step(req.action)

    return {
        "state": state.tolist(),
        "reward": float(reward),
        "done": terminated or truncated,
        "info": info
    }


# -------- MAIN --------
if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860, reload=True)