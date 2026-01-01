class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

class JobScheduling:
    @staticmethod
    def profit_scheduling(jobs):
        # Sort jobs based on profit in descending order
        jobs.sort(key=lambda job: job.profit, reverse=True)

        max_deadline = max(job.deadline for job in jobs)
        slots = [None] * max_deadline  # Track scheduled jobs
        total_profit = 0

        for job in jobs:
            # Find a free slot for this job (starting from its deadline)
            for j in range(min(max_deadline, job.deadline) - 1, -1, -1):
                if slots[j] is None:
                    slots[j] = job.job_id
                    total_profit += job.profit
                    break

        # Collect scheduled job IDs
        scheduled_jobs = [job_id for job_id in slots if job_id is not None]
        return scheduled_jobs, total_profit

if __name__ == "__main__":
    jobs = [
        Job(1, 2, 40),
        Job(2, 1, 19),
        Job(3, 2, 27),
        Job(4, 1, 25),
        Job(5, 3, 15)
    ]
    
    scheduled_jobs, total_profit = JobScheduling.profit_scheduling(jobs)
    print("Scheduled Jobs:", scheduled_jobs)
    print("Total Profit:", total_profit)
