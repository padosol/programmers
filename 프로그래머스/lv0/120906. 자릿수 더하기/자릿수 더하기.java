import java.util.*;

class Solution {
    public int solution(int n) {
        
        return Integer.parseInt(Arrays.stream(String.valueOf(n).split("")).reduce((i, v) -> {
            return String.valueOf(Integer.parseInt(i) + Integer.parseInt(v));
        }).get());
    }
}