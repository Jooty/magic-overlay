import psutil
import Xlib
import Xlib.display

WIZARD_GRAPHICAL_CLIENT_NAME = "WizardGraphical"

def get_wizard_process():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == WIZARD_GRAPHICAL_CLIENT_NAME:
            return process
        
def get_overlay_position(process_id):
    # Iterate through the x11 window hierachy to find the wizard window.
    display = Xlib.display.Display()
    root = display.screen().root
    window_ids = root.get_full_property(display.intern_atom('_NET_CLIENT_LIST'), Xlib.X.AnyPropertyType).value
    geometry = None
    for window_id in window_ids:
        window = display.create_resource_object('window', window_id)
        window_pid = window.get_full_property(display.intern_atom('_NET_WM_PID'), Xlib.X.AnyPropertyType).value[0]
        if window_pid == process_id:
            geometry = window.get_geometry()
            
    if geometry is not None:
        # Get the total screen width and height.
        screen_width = display.screen().width_in_pixels
        screen_height = display.screen().height_in_pixels
        
        # The center of the screen for Xlib is 0, 0. Convert it to the top left corner.
        x = int(abs(geometry.x + screen_width / 4))
        y = int(abs(geometry.y + screen_height / 2))
        
        # Now use the window width and height to get the top left corner of the window.
        x = int(abs(x - geometry.width / 2))
        y = int(abs(y - geometry.height / 2))
        
        return (x, y)
    else:
        return None