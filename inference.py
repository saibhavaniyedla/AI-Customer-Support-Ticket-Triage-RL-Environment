import os
import logging
from openai import OpenAI

from env.ticket_env import TicketTriageEnv
from tasks.tasks import Task   # ✅ correct import

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# -------- ENV VARIABLES --------
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

client = None
if API_KEY:
    client = OpenAI(api_key=API_KEY)
else:
    log.warning("⚠️ No API_KEY found, using fallback logic")


# -------- LLM / FALLBACK --------
def get_action_from_llm(state) -> int:
    """
    Returns:
        0 = Low priority
        1 = Medium priority
        2 = High priority
    """

    # ✅ Fallback (no API key)
    if not client:
        score = sum(state)
        if score < 3:
            return 0
        elif score < 6:
            return 1
        else:
            return 2

    # ✅ LLM mode
    prompt = f"""
You are an AI customer support ticket triage agent.

Classify ticket priority:
0 = Low
1 = Medium
2 = High

State: {state}

Reply ONLY with one number: 0 or 1 or 2
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5,
        )

        raw = response.choices[0].message.content.strip()

        # ✅ robust parsing
        if "2" in raw:
            return 2
        elif "1" in raw:
            return 1
        else:
            return 0

    except Exception as e:
        log.error(f"LLM call failed: {e}")
        return 0


# -------- RUN TASK --------
def run_task(task: Task) -> dict:
    env = TicketTriageEnv(task=task)

    state, _ = env.reset()
    log.info(f"[START] task={task.value} model={MODEL_NAME}")

    action = get_action_from_llm(state.tolist())

    state, reward, terminated, truncated, _ = env.step(action)

    score = float(reward)
    success = score > 0

    log.info(f"[END] task={task.value} action={action} score={score:.2f} success={success}")

    return {
        "task": task.value,
        "action": action,
        "score": score,
        "success": success
    }


# -------- MAIN --------
if __name__ == "__main__":
    results = [run_task(task) for task in Task]   # ✅ FIXED

    print("\n===== FINAL RESULTS =====")
    for r in results:
        print(r)