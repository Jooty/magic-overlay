from tkinter import *
import linux_wm_utils
import window;

# 0 - Normal Player
# 1 - Hall Monitors
# 2 - Developers (only available in debug build)
# 3 - Game Master

# Test: remove later
# process = linux_wm_utils.get_wizard_process()
# if process is not None:
#     pid = process.info['pid']
#     geometry = linux_wm_utils.get_overlay_position(pid);
# else:
#     print("No Wizard process was found!")
#     exit()
    
window = window.Window("MAGIC Overlay")