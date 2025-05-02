import re
import sys
from datetime import datetime, timedelta

def adjust_subtitle_time(input_file, output_file, seconds_to_add):
    time_pattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})")

    def add_seconds(time_str, seconds):
        time_obj = datetime.strptime(time_str, "%H:%M:%S,%f")
        new_time = time_obj + timedelta(seconds=seconds)
        return new_time.strftime("%H:%M:%S,%f")[:-3]

    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    adjusted_lines = []
    for line in lines:
        match = time_pattern.match(line)
        if match:
            start_time = add_seconds(match.group(1), seconds_to_add)
            end_time = add_seconds(match.group(2), seconds_to_add)
            adjusted_lines.append(f"{start_time} --> {end_time}\n")
        else:
            adjusted_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(adjusted_lines)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python adjust_srt.py input.srt output.srt seconds_to_add")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    seconds_to_add = float(sys.argv[3])

    adjust_subtitle_time(input_file, output_file, seconds_to_add)
    print(f"Adjusted subtitles saved to {output_file}")

