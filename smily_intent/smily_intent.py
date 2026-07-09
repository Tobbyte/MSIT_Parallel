import sys
import subprocess
import os


def run_smiley_code(filename, emoji_indent="😊"):
    # Find the exact folder where THIS runner.py file lives
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Combine it with your target filename to get the absolute path
    full_path = os.path.join(script_dir, filename)

    with open(full_path, "r", encoding="utf-8") as f:
        custom_code = f.read()

    standard_code = custom_code.replace(emoji_indent, "    ")

    process = subprocess.Popen(
        [sys.executable, "-c", standard_code],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = process.communicate()

    if stdout:
        print(stdout)
    if stderr:
        print(f"Error:\n{stderr}", file=sys.stderr)


if __name__ == "__main__":
    run_smiley_code("script_with_emojis.py", emoji_indent="😊")
