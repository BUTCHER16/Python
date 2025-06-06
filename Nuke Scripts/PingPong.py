import nuke
import threading
import time

# Shared toggle control variable
eye_toggle_running = [False]  # Mutable list for thread-safe toggle

# Function that runs in background thread
def eye_pingpong_loop(interval=0.2):  # ← faster toggle (was 0.5)
    views = nuke.views()
    if len(views) < 2:
        nuke.executeInMainThread(lambda: nuke.message("Need at least 2 stereo views."))
        return

    while eye_toggle_running[0]:
        def toggle():
            viewer = nuke.activeViewer()
            if not viewer:
                return
            current = viewer.view()
            next_view = views[1] if current == views[0] else views[0]
            viewer.setView(next_view)

        # Toggle view on main thread
        nuke.executeInMainThread(toggle)
        time.sleep(interval)

# Function triggered by menu/shortcut
def toggle_eye_pong():
    if eye_toggle_running[0]:
        eye_toggle_running[0] = False
        nuke.tprint("👁️ Eye toggle stopped.")
    else:
        eye_toggle_running[0] = True
        thread = threading.Thread(target=eye_pingpong_loop, args=(0.2,))  # ← speed here too
        thread.daemon = True
        thread.start()
        nuke.tprint("👁️ Eye toggle started (Shift+E to stop).")

# Add menu item with shortcut
stereo_menu = nuke.menu("Nuke").addMenu("Stereo")
stereo_menu.addCommand("Auto Toggle Eyes (Shift+E)", toggle_eye_pong, "shift+e")
