#!/bin/bash
echo "Running Models-organizer"

# Path to the virtual environment
VENV_PATH="your venv path"

# Path to the ComfyUI application
APP_PATH="your models folder path, where app.py will be located"

# Open a new terminal window
echo "Launching Models-organizer"
IP=$(hostname -I | awk '{print $1}')  # This gets the first IP address
gnome-terminal --working-directory="$VENV_PATH" -- bash -c "source $VENV_PATH/bin/activate; streamlit run $APP_PATH/app.py; exec bash"
