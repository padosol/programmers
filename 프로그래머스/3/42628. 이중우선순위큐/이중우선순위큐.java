import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[]{0,0};

        Queue<Integer> min = new PriorityQueue<>();
        Queue<Integer> max = new PriorityQueue<>(Collections.reverseOrder());

        for(String operation : operations) {

            String[] data = operation.split(" ");
            String type = data[0];
            int value = Integer.valueOf(data[1]);
            int num = 0;

            switch(type) {
                case "I":
                    max.add(value);
                    min.add(value);
                    break;
                case "D":
                    if(max.isEmpty() && min.isEmpty()){
                        break;
                    }
                    
                    if(value == -1) {
                        num = min.peek();
                        min.poll();
                        max.remove(num);
                    }

                    if(value == 1) {
                        num = max.peek();
                        max.poll();
                        min.remove(num);
                    }

                    break;
            }

        }

        if(min.size() > 0 && max.size() > 0) {
            answer = new int[]{max.poll(), min.poll()};
        } else {
            answer = new int[]{0,0};
        }

        return answer;
    }
}