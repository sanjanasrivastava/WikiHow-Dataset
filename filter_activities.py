import json
import re
import pprint

ALL_ACTIVITIES_FILE = "all_activities.txt"
EXCLUDED_WORDS_FILE = "excluded_words.json"
with open(EXCLUDED_WORDS_FILE) as excfile:
    excluded_words = json.load(excfile)

with open(ALL_ACTIVITIES_FILE) as actfile:
    all_activities = set()
    no_number_pattern = r"[^0-9]+"
    activity_strings = actfile.readlines()
    for actstring in activity_strings:
        skip = False 
        # Assume every activity is of form <name><index>?
        activity = re.search(no_number_pattern, actstring).group(0) 
        if "\n" not in activity:
            activity += "\n"
        for excluded_word in excluded_words:
            if excluded_word in activity: 
                skip = True 
                break 

        if not skip:
            all_activities.add(activity)

print(len(all_activities))

with open("currently_filtered_activities.txt", "w") as currentactfile:
    currentactfile.writelines(list(all_activities))
    