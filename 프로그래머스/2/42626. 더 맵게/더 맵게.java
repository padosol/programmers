import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] scoville, int K) {
        
        int count = 0;
        
        PriorityQueue<Integer> scovilles = new PriorityQueue<>();
        
        for(int i=0;i<scoville.length;i++) {
            scovilles.add(scoville[i]);
        }
        
        while(!scovilles.isEmpty()) {

            if(scovilles.peek() >= K){
                scovilles.clear();
            } else if (scovilles.size() == 1){
                count = -1;
                scovilles.clear();
            } else {
                int first = scovilles.poll();
                int second = scovilles.poll();

                int newScoville = first + (second * 2);
                scovilles.add(newScoville);

                count++;
            }
        }
        
        return count;

    }
}