#!/bin/bash

# Function to check if a process is running
is_process_running() {
    pgrep -f "$1" > /dev/null
}

# Close the program if it's running
if is_process_running "your_program_name"; then
    echo "Closing the program..."
    pkill -f "your_program_name"
    sleep 2  # Wait for the process to terminate
fi

# Use black to format all files
echo "Formatting files using Black..."
black .

# Launch the program
echo "Launching the program..."
python your_program.py  # Replace 'your_program.py' with your actual program file
