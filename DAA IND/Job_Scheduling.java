import java.util.*;

class Job {
    int jobId;
    int deadline;
    int profit;

    public Job(int jobId, int deadline, int profit) {
        this.jobId = jobId;
        this.deadline = deadline;
        this.profit = profit;
    }
}

public class Job_Scheduling {
    public static void main(String[] args) {
        List<Job> jobs = new ArrayList<>();
        jobs.add(new Job(1, 2, 40));
        jobs.add(new Job(2, 1, 19));
        jobs.add(new Job(3, 2, 27));
        jobs.add(new Job(4, 1, 25));
        jobs.add(new Job(5, 3, 15));

        Result result = profitScheduling(jobs);
        
        // Print scheduled job IDs and total profit
        System.out.println("Scheduled Jobs: " + result.scheduledJobs);
        System.out.println("Total Profit: " + result.totalProfit);
    }

    public static class Result {
        List<Integer> scheduledJobs;
        int totalProfit;

        public Result(List<Integer> scheduledJobs, int totalProfit) {
            this.scheduledJobs = scheduledJobs;
            this.totalProfit = totalProfit;
        }
    }

    public static Result profitScheduling(List<Job> jobs) {
        // Sort the jobs based on profit in descending order
        jobs.sort((a, b) -> b.profit - a.profit);

        boolean[] slots = new boolean[jobs.size()];
        int totalProfit = 0;

        List<Integer> scheduledJobIds = new ArrayList<>();

        for (Job job : jobs) {
            for (int j = Math.min(jobs.size(), job.deadline) - 1; j >= 0; j--) {
                if (!slots[j]) {
                    totalProfit += job.profit;
                    slots[j] = true;
                    scheduledJobIds.add(job.jobId);
                    break;
                }
            }
        }

        return new Result(scheduledJobIds, totalProfit);
    }
}
