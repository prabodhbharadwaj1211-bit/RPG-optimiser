import curses
import json
import os
from terminal_renderer import draw_cdda_ui

def main(stdscr):
    curses.curs_set(0)
    
    state_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'player_state.json')
    try:
        with open(state_path, 'r') as f:
            state = json.load(f)
    except FileNotFoundError:
        state = {"gold": 0, "target_stats": {}}
        
    x, y = 15, 10
    logs = ["Welcome to the wasteland.", "Move: WASD | Optimize: O | Quit: Q"]
    
    while True:
        draw_cdda_ui(stdscr, x, y, logs, state)
        
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == ord('w'):
            y -= 1
        elif key == ord('s'):
            y += 1
        elif key == ord('a'):
            x -= 1
        elif key == ord('d'):
            x += 1
        elif key == ord('o'):
            logs.append("Running matrix linear solvers...")
            
if __name__ == "__main__":
    curses.wrapper(main)