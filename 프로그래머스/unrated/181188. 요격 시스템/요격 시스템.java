import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;

        Arrays.sort(targets, (o1, o2) -> {
            return o1[1] - o2[1];
        });

        int length = targets.length;
        int start = 0;

        for(int i=0;i<length;i++){
            int s = targets[i][0];
            int e = targets[i][1];

            if( s < start ){
                continue;
            } else {
                answer++;
                start = e;
            }
        }

        return answer;
    }
}