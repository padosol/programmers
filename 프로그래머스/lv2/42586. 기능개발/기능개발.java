import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> list = new ArrayList<>();
        Queue<Integer> p_q = new LinkedList<>();
        Queue<Integer> s_q = new LinkedList<>();
        for(int i=0; i< progresses.length;i++){
            p_q.add(progresses[i]);
            s_q.add(speeds[i]);
        }

        while(!p_q.isEmpty()) {

            for(int i=0;i< p_q.size();i++){
                int p = p_q.poll();
                int s = s_q.poll();

                p_q.add(p+s);
                s_q.add(s);
            }

            boolean flag = true;
            int count = 0;
            while(flag) {
                if(!p_q.isEmpty() && p_q.peek() >= 100){
                    count++;
                    p_q.remove();
                    s_q.remove();
                } else {
                    flag = false;
                }
            }
            if(count != 0){
                list.add(count);
            }
        }

        return list.stream().mapToInt(x->x).toArray();
    }
}