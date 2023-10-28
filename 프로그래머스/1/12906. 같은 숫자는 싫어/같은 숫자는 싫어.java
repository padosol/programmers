import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        Stack<Integer> stack = new Stack<>();

        for(int num : arr) {

            if(stack.empty()) {
                stack.push(num);
            } else {

                Integer peek = stack.peek();
                if(peek == num) {
                    continue;
                } else {
                    stack.push(num);
                }

            }
        }

        return stack.stream().mapToInt( a -> a).toArray();
    }
}