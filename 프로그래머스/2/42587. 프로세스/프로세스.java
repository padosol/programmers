import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[] priorities, int location) {
        
        int answer = 0;
        
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int a : priorities) {
            queue.add(a);
        }
        
        while(!queue.isEmpty()) {

            for(int i=0;i<priorities.length;i++) {

                if( priorities[i] == queue.peek() ) {
                    queue.poll();
                    answer++;

                    if( location == i ) {
                        queue.clear();
                        break;
                    }
                    
                }
            }
        }
        
        
        return answer;
    }
}