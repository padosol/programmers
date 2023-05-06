import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int length = citations.length;
        for(int i=0;i<length;i++) {
            int h = i+1;
            for(int j=0;j<length;j++){

                if(citations[j] >= h){
                    int h_up = length - j;
                    int h_down = j+1;

                    if(h_up >= h && h_down <= h){
                        answer = h;
                    }
                }
            }
        }
        return answer;
    }
}