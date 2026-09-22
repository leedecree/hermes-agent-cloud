#!/bin/bash
set -e

echo "=== Starting Hermes Cloud Gateway ==="

HERMES_DIR="${HOME}/.hermes"
mkdir -p "$HERMES_DIR"

# Write credentials to .env
cat <<EOF > "$HERMES_DIR/.env"
TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
TELEGRAM_ALLOWED_USERS=${TELEGRAM_ALLOWED_USERS}
GEMINI_API_KEY=${GEMINI_API_KEY}
GROQ_API_KEY=${GROQ_API_KEY}
OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
OPENAI_API_KEY=${OPENAI_API_KEY}
EOF

# Ensure model configuration
MODEL_PROVIDER="${MODEL_PROVIDER:-gemini}"
MODEL_NAME="${MODEL_NAME:-gemini-2.5-flash}"

cat <<EOF > "$HERMES_DIR/config.yaml"
model:
  provider: ${MODEL_PROVIDER}
  default: ${MODEL_NAME}
gateway:
  platforms:
    - telegram
telegram:
  allowed_users: [${TELEGRAM_ALLOWED_USERS}]
EOF

echo "Configuration generated:"
echo " - Model: ${MODEL_PROVIDER}/${MODEL_NAME}"
echo " - Telegram Allowed Users: ${TELEGRAM_ALLOWED_USERS}"

# 1. Start lightweight keep-alive / healthcheck server on $PORT
python3 /app/web_health.py &
HEALTH_PID=$!
echo "Health server started (PID $HEALTH_PID)"

# 2. Trap signals for graceful shutdown
cleanup() {
    echo "Shutting down services..."
    kill "$HEALTH_PID" 2>/dev/null || true
    exit 0
}
trap cleanup SIGTERM SIGINT

# 3. Start Hermes Gateway
echo "Starting Hermes Gateway (Foreground)..."
exec hermes gateway run
