import java.util.Arrays;
class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        
                int limit = m;
        boolean[] blank = new boolean[n];

        Arrays.fill(blank, false);

        for(int i=0;i<section.length;i++) {
            blank[section[i]-1] = true;
        }

        boolean check = false;
        for(int i=0;i<n;i++) {

            if(limit == 0){
                check = false;
                limit = m;
            }

            if(check) {
                limit -= 1;
                continue;
            }

            if(blank[i]){
                check = true;
                answer++;
                limit -= 1;
            }
        }
        
        return answer;
    }
}