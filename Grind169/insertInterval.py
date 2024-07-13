def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals = sorted(intervals, key=lambda x: x[0])
    new_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= new_intervals[-1][1]:
            new_intervals[-1][0] = min(intervals[i][0], new_intervals[-1][0])
            new_intervals[-1][1] = max(intervals[i][1], new_intervals[-1][1])
        else:
            new_intervals.append(intervals[i])
    return new_intervals