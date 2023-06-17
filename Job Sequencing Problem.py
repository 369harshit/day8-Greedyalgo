def job_sequencing(jobs):
    # Sort jobs based on their profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [0] * max_deadline  # Initialize the schedule as a list of zeros
    total_jobs_done = 0
    total_profit = 0

    for job in jobs:
        deadline = job[1]
        # Find the nearest available slot before the deadline
        while deadline > 0:
            if schedule[deadline - 1] == 0:
                schedule[deadline - 1] = job[0]  # Assign the job to the slot
                total_jobs_done += 1
                total_profit += job[2]
                break
            deadline -= 1

    return total_jobs_done, total_profit, schedule

# Example usage
jobs = [(1, 2, 100), (2, 1, 50), (3, 2, 25), (4, 1, 60), (5, 3, 125)]
job_count, max_profit, job_schedule = job_sequencing(jobs)

print("Number of Jobs Done:", job_count)
print("Maximum Profit:", max_profit)
print("Job Schedule:", job_schedule)
