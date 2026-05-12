# ── Stage 1: Base image ───────────────────────────────────────────────────────
# We use the official Python 3.11 slim image.
# 'slim' means it strips out a lot of unnecessary OS tools,
# making the final image smaller and faster to download on Render.
FROM python:3.11-slim

# ── Stage 2: Set working directory ───────────────────────────────────────────
# All commands from here on run inside /app inside the container.
# Think of this as 'cd /app' but it also creates the folder if it doesn't exist.
WORKDIR /app

# ── Stage 3: Install dependencies ────────────────────────────────────────────
# We copy requirements.txt FIRST — before copying any app code.
# Why? Docker builds in layers. If requirements.txt hasn't changed,
# Docker reuses the cached pip install layer from last time.
# This means rebuilds after code changes take seconds, not minutes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Stage 4: Copy application code ───────────────────────────────────────────
# Now we copy everything else.
# .dockerignore (we'll create this next) controls what gets excluded.
COPY app/ ./app/
COPY model/heart_model.joblib ./model/heart_model.joblib

# ── Stage 5: Expose the port ──────────────────────────────────────────────────
# This tells Docker "the app inside listens on port 8000".
# It doesn't actually open the port — docker-compose handles that mapping.
EXPOSE 8000

# ── Stage 6: Start the app ────────────────────────────────────────────────────
# This is the command that runs when the container starts.
# --host 0.0.0.0 means "accept connections from outside the container"
# Without this, the app only listens internally and you can't reach it.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]