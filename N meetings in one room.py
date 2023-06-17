def schedule_meetings(start, end):
    # Create a list of tuples (start_time, end_time, meeting_index)
    meetings = [(start[i], end[i], i) for i in range(len(start))]

    # Sort the meetings based on their end times
    sorted_meetings = sorted(meetings, key=lambda x: x[1])

    scheduled_meetings = []
    current_end_time = float('-inf')

    # Iterate through each meeting
    for meeting in sorted_meetings:
        start_time, end_time, index = meeting

        # If the meeting's start time is after the current end time, schedule it
        if start_time >= current_end_time:
            scheduled_meetings.append(index)
            current_end_time = end_time

    return scheduled_meetings

# Example usage
start = [1, 0, 3, 8, 5, 8]
end = [2, 6, 4, 9, 7, 9]
scheduled_meetings = schedule_meetings(start, end)

print("Scheduled Meetings:")
for meeting_index in scheduled_meetings:
    print(f"Meeting{meeting_index + 1}",end=" ")
