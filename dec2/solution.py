
def is_safe(report):
    ascending = report[0] < report[1]
    safe = []
    
    for i in range(len(report) - 1):
        entry_ascending = report[i] < report[i+1]
        diff = abs(report[i] - report[i+1])
        safe.append(int(not (((ascending and entry_ascending) or (not ascending and not entry_ascending)) and (diff >= 1) and (diff <=3))))

    return safe


reports = []
safe_reports = 0
almost_safe_reports = 0

with open("input.txt", "r") as f:
    for line in f: 
        report = list(map(int, line.split()))
        safe = is_safe(report)

        # Report is safe
        if sum(safe) == 0:
            # Report is safe
            safe_reports += 1

        else:
            # Adjust the report by removing a different level and see if it makes it safe
            for i in range(len(report)):
                new_report = list(map(int, line.split()))
                new_report.pop(i)

                safe = is_safe(new_report)
                if sum(safe) == 0:
                    almost_safe_reports += 1
                    break


print(f"Part 1: {safe_reports}")
print(f"Part 2: {almost_safe_reports + safe_reports}")
