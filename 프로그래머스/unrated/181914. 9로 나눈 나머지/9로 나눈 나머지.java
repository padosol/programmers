import java.util.*;
class Solution {
    public int solution(String number) {
        int answer = 0;
        String[] nums = number.split("");

        for(int i=0;i<number.length();i++){
            answer += Integer.parseInt(nums[i]);
        }

        return answer%9;
    }
}