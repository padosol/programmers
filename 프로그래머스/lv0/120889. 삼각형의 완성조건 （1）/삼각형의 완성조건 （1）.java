import java.util.*;
class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        
        Arrays.sort(sides);
        
        return sides[2] < sides[1] + sides[0] ? 1:2;
    }
}