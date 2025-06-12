import nuke
import os
import re

def missing_frames():
    try:
        node = nuke.selectedNode()
        if node.Class() != 'Read':
            nuke.message("❗ Please select a Read node.")
            return

        file_path = node['file'].evaluate()
        start_frame = int(nuke.root()['first_frame'].value())
        end_frame = int(nuke.root()['last_frame'].value())

        # Pattern 1: padded placeholder (e.g. %04d, ####, $F4)
        match = re.search(r"(.*)(%0\dd|#+|\$F\d?)(.*)", file_path)
        if match:
            prefix, pad_token, suffix = match.groups()
            padding = int(re.search(r'\d+', pad_token).group()) if re.search(r'\d+', pad_token) else 4
        else:
            # Pattern 2: literal frame number (e.g. shotname.1001.exr)
            match = re.search(r"(.*?\.)(\d{2,6})(\.[a-zA-Z0-9]+)$", file_path)
            if match:
                prefix, pad_digits, suffix = match.groups()
                padding = len(pad_digits)
            else:
                nuke.message(f"❌ Could not parse frame pattern in path:\n{file_path}")
                return

        missing_frames = []
        for frame in range(start_frame, end_frame + 1):
            frame_str = str(frame).zfill(padding)
            full_path = f"{prefix}{frame_str}{suffix}"
            if not os.path.exists(full_path):
                missing_frames.append(frame)

        if missing_frames:
            nuke.message(f"❌ Missing Frames Detected:\n{', '.join(map(str, missing_frames))}")
        else:
            nuke.message("✅ All frames are present!")

    except Exception as e:
        nuke.message(" Error: " + str(e))