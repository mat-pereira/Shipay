def log_info(message: str):
    print(f"[ℹ️INFO] {message}")

def log_success(message: str):
    print(f"[✅SUCCESS] {message}")

def log_warning(message: str):
    print(f"[⚠️WARNING] {message}")

def log_error(message: str, exc=None):
    print(f"[❌ERROR] {message}")
    if exc:
        print(f"Exception: {exc}")

def log_debug(message: str):
    print(f"[🔍DEBUG] {message}")