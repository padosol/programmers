import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        for(int item : arr) {
            if(stack.empty()) {
                stack.push(item);
                list.add(item);
            } else {
                int tmp = stack.pop();
                if( tmp != item ){
                    list.add(item);
                    stack.push(item);
                } else {
                    stack.push(tmp);
                }

            }
        }

        return list.stream().mapToInt(x -> x).toArray();
    }
}