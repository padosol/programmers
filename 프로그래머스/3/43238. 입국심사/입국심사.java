
import java.util.Arrays;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0L;
        int length = times.length;

        Arrays.sort(times);

        long maxTime = (long) times[length - 1] * n; 
        long minTime = 1;  

        while(minTime <= maxTime) {

            long avgTime = (minTime + maxTime) / 2;
            long count = 0;

            for(int i=0;i<length;i++) {
                count += avgTime / times[i];  
                if(count >= n) break; 
            }

            if(count < n) minTime = avgTime + 1;
            else maxTime = avgTime - 1;
            
        }
        return minTime;
    }
}