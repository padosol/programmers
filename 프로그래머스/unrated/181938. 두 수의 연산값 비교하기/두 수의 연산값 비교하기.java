class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String tmp = String.valueOf(a) + String.valueOf(b);
        int n = Integer.parseInt(tmp);
        
        
        return n > 2*a*b?n:2*a*b;
    }
}