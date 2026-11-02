import curses

def draw_cdda_ui(stdscr, p_x, p_y, logs, state):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    for y in range(h - 6):
        for x in range(w - 30):
            if x == p_x and y == p_y:
                stdscr.addstr(y, x, "@", curses.A_BOLD)
            else:
                stdscr.addstr(y, x, ".")
                
    stdscr.vline(0, w - 30, '|', h)
    stdscr.hline(h - 6, 0, '-', w)
    
    stdscr.addstr(1, w - 28, f"GOLD: {state.get('gold', 0)}")
    stdscr.addstr(3, w - 28, "TARGET STATS:")
    for i, (k, v) in enumerate(state.get('target_stats', {}).items()):
        stdscr.addstr(4 + i, w - 28, f"{k}: {v}")
        
    stdscr.addstr(h - 5, 2, "MESSAGE LOG:")
    for i, log in enumerate(logs[-3:]):
        stdscr.addstr(h - 4 + i, 2, log)
        
    stdscr.refresh()