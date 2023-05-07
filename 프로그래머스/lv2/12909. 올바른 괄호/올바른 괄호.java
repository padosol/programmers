import java.util.*;
class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i=0;i<s.length();i++){
            if(stack.empty()) {
                stack.push(s.charAt(i));
            } else {
                if(s.charAt(i) == '(') {
                    stack.push(s.charAt(i));
                } else {
                    char t = stack.pop();
                    if( t == ')' ){
                        stack.push(t);
                    }
                }
            }
        }
        return stack.empty();
    }
}