import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;

        PriorityQueue<Integer> pq = Arrays.stream(scoville)
                .boxed()
                .collect(Collectors.toCollection(PriorityQueue::new));


        int min = pq.peek();

        while(min < K && pq.size() != 1) {

            answer++;
            int n1 = pq.poll();
            int n2 = pq.poll();
            int shake = n1 + (n2 * 2);
            pq.add(shake);
            min = pq.peek();
        }

        if ( pq.peek() < K )return -1;

        return answer;
    }
}