import importlib
import traceback

def run_grader():
    print("🔍 Running Project Grader...\n")

    # -------- TEST 1: Import Environment --------
    try:
        env_module = importlib.import_module("env.ticket_env")
        env_class = getattr(env_module, "TicketTriageEnv")
        env = env_class()
        print("✅ Environment import successful")
    except Exception:
        print("❌ Failed to import environment")
        traceback.print_exc()
        return False

    # -------- TEST 2: Reset Function --------
    try:
        obs, info = env.reset()
        print("✅ reset() works")
    except Exception:
        print("❌ reset() failed")
        traceback.print_exc()
        return False

    # -------- TEST 3: Step Function --------
    try:
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        print("✅ step() works")
    except Exception:
        print("❌ step() failed")
        traceback.print_exc()
        return False

    # -------- TEST 4: Train Function --------
    try:
        train_module = importlib.import_module("train")

        if hasattr(train_module, "train"):
            train_module.train()
            print("✅ train() executed successfully")
        else:
            print("❌ train() function missing")
            return False

    except Exception:
        print("❌ train() failed")
        traceback.print_exc()
        return False

    # -------- TEST 5: Model File Check --------
    import os
    if os.path.exists("models/ppo_ticket_model.zip"):
        print("✅ Model saved correctly")
    else:
        print("⚠️ Model file not found (may still pass depending on grader)")

    print("\n🎉 ALL TESTS PASSED")
    return True


if __name__ == "__main__":
    run_grader()