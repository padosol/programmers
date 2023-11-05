import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int length = jobs.length;
        int time = 0;
        int index = 0;

        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);

        Queue<int[]> qJobs = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);

        while(index < length || !qJobs.isEmpty()) {

            while( index < length && time >= jobs[index][0] ) {
                qJobs.offer(jobs[index++]);
            }

            if(qJobs.isEmpty()) {
                time = jobs[index][0];
            } else {
                int[] now = qJobs.poll();
                answer += time - now[0] + now[1];
                time += now[1];
            }
        }


        return answer/length;


    }
}