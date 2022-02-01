import re 
import sys 

FILTERED_WIKIHOW_FILENAME = "currently_filtered_activities_20220118.txt"
FORMATTED_WIKIHOW_FILENAME = "formatted_wikihow_activities.txt"


def format_wikihow_activity(raw_activity):
    check = "Milk" in raw_activity
    # print(raw_activity)
    # print(check)
    strpac = raw_activity.replace("Howto", "")
    if check: print(strpac)
    spltac = re.split("([A-Z])", strpac)
    if check: print(spltac)
    fixac = [spltac[i] + spltac[i + 1] for i in range(1, len(spltac)) if i % 2] # this assumes all activities have a capital letter after Howto
    if check: print(fixac)
    lowac = [ac.lower() for ac in fixac]
    if check: print(lowac)
    if check: print(" ".join(lowac))
    return " ".join(lowac)

def format_wikihow_activities(filtered_fn=FILTERED_WIKIHOW_FILENAME, formatted_fn=FORMATTED_WIKIHOW_FILENAME):
    with open(filtered_fn, "r") as f:
        rawacs = f.readlines()
        acs = [format_wikihow_activity(rawac) for rawac in rawacs]
    
    with open(formatted_fn, "w") as f: 
        for ac in acs: 
            f.write(ac)

if __name__ == "__main__":
    if sys.argv[1] == "format":
        format_wikihow_activities()
