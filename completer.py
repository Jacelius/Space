

import curses

def celestial_object_selection(stdscr):
    # Define a list of options
    options = ["Moon", "Mars"]
    # Set up the screen
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr("Which celestial object would you like to know the distance to?:\n")
    # Print the options
    for i, opt in enumerate(options):
        stdscr.addstr(f"{opt}\n")
    current_option = -1
    # Loop until the user selects an option
    while True:
        # Highlight the first option if no option is selected
        if current_option == -1:
            current_option = 0
            stdscr.addstr(current_option+1, 0, options[current_option], curses.A_REVERSE)
        # Get input from the user
        key = stdscr.getch()
        # Move up or down with arrow keys
        if key == curses.KEY_UP and current_option > 0:
            stdscr.addstr(current_option+1, 0, options[current_option])
            current_option -= 1
            stdscr.addstr(current_option+1, 0, options[current_option], curses.A_REVERSE)
        elif key == curses.KEY_DOWN and current_option < len(options)-1:
            stdscr.addstr(current_option+1, 0, options[current_option])
            current_option += 1
            stdscr.addstr(current_option+1, 0, options[current_option], curses.A_REVERSE)
        # Select an option with Enter
        elif key == curses.KEY_ENTER or key == 10 or key == 13:
            break
    # Return the selected option
    return options[current_option]

def observer_selection(stdscr):
    options = ["My Coordinates", "Paris", "London", "New York", "Tokyo"]
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr("From which observer location? your own location or a specific location?\n")
    for i, opt in enumerate(options):
        stdscr.addstr(f"{opt}\n")
    current_option = 0
    stdscr.addstr(current_option+1, 0, options[current_option], curses.A_REVERSE)
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_option > 0:
            stdscr.addstr(current_option+1, 0, options[current_option])
            current_option -= 1
            stdscr.addstr(current_option+1, 0, options[current_option], curses.A_REVERSE)
        elif key == curses.KEY_DOWN and current_option < len(options)-1:
            stdscr.addstr(current_option+1, 0, options[current_option])
            current_option += 1
            stdscr.addstr(current_option+1, 0, options[current_option], curses.A_REVERSE)
        elif key == curses.KEY_ENTER or key == 10:
            break
    return options[current_option]