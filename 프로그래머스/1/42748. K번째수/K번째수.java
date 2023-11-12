import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        int k = 0;
        for(int[] command : commands) {

            int[] tmp = new int[command[1]-command[0] + 1];

            int ii=0;
            for(int j=command[0]-1;j<=command[1]-1;j++) {
                tmp[ii++] = array[j];
            }

            Arrays.sort(tmp);
            answer[k++] = tmp[command[2]-1];


        }

        return answer;
    }
}