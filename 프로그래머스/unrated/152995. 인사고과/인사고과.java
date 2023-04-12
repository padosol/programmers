import java.util.*;
class Solution {
    public int solution(int[][] scores) {
              int answer = 1;
        int[] wan = scores[0];
        Arrays.sort(scores, (a, b) -> a[0] == b[0] ? a[1] - b[1] : b[0] - a[0]);

        int max = 0;

        for(int[] item : scores){

            if(item[1] < max){
                if(item.equals(wan)){
                    return -1;
                }
            }else{
                if(item[0] + item[1] > wan[0] + wan[1]){
                    answer++;
                }
                max = Math.max(max, item[1]);
            }
        }

        return answer;
    }
}