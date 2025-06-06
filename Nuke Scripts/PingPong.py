import nuke

# Toggle stereo views (left ↔ right)
def toggle_eye_view():
    views = nuke.views()
    if len(views) < 2:
        nuke.message("Stereo views not detected. At least two views are required.")
        return

    viewer = nuke.activeViewer()
    if viewer is None:
        nuke.message("No active Viewer found.")
        return

    current_view = viewer.view()
    try:
        current_index = views.index(current_view)
        next_index = (current_index + 1) % len(views)
        viewer.setView(views[next_index])
    except ValueError:
        viewer.setView(views[0])  # default to first view if mismatch

# Add menu and shortcut
stereo_menu = nuke.menu("Nuke").addMenu("Stereo")
stereo_menu.addCommand("Toggle Eye View", toggle_eye_view, "shift+e")
