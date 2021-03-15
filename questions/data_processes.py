def find_last_activity(activities):
    all_activities = [activity for activity in activities if activity]

    return max(all_activities)
