import java.util.*;
class Solution {
    public int[] solution(int n) {
        
        
        List<Integer> answer = new ArrayList<>();
        
        for(int i=1;i<=n;i++){
            if(i % 2 != 0){
                answer.add(i);
            }
        }
        
        return answer.stream().mapToInt(a -> a).toArray();
    }
}