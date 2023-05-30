import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        boolean flag = true;
        Queue<Integer> start = new LinkedList<>();
        Queue<Integer> bridge = new LinkedList<>();

        for(int i=0;i< truck_weights.length;i++){
            start.add(truck_weights[i]);
        }

        Queue<Integer> end = new LinkedList<>();

        while(flag) {
            answer++;

            int truck = 0;

            if( !start.isEmpty() && weight - start.peek() > -1 ) {
                truck = start.poll();
            }

            bridge.add(truck);
            weight -= truck;


            if(bridge.size() == bridge_length){
                int end_truck = bridge.poll();
                if( end_truck != 0)  end.add(end_truck);
                weight += end_truck;
            }

            if(end.size() == truck_weights.length) {
                answer++;
                flag = false;
            }
        }

        return answer;
    }
}