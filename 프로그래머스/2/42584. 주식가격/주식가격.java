import java.util.*;
class Solution {
    public int[] solution(int[] prices) {

        int[] answer = new int[prices.length];
        
        Arrays.fill(answer, 0);
        
        for(int i=0;i< prices.length;i++) {

            int price = prices[i];

            for(int j=i+1;j<prices.length;j++) {

                if(price <= prices[j]){
                    answer[i]++;
                } else {
                    answer[i]++;
                    break;
                }

            }

        }

        return answer;
    }
}