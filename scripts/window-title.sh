#!/bin/bash

# Get the workspace number of the currently focused window
current_workspace=$(xdotool get_desktop)

# Get the list of open applications in the current workspace
open_apps=$(wmctrl -lx | awk -v workspace="$current_workspace" '$2 == workspace {print $3}')

# Display the list of open applications
echo "$open_apps" | cut -d'.' -f2- | tr '\n' ' ' | sed 's/-$//'| sed 's/processing-app-Base/Arduino IDE/' | sed 's/Cannot get client list properties./Desktop/' 
