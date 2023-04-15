class Solution {
    public int solution(int n) {
        int answer = 0;
        return Math.sqrt(n) % 1 == 0 ? 1: 2;
    }
}