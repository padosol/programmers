class Solution {
    public int solution(int hp) {
        int answer = 0;
        
        int aa = hp/5;
        hp = hp%5;
        
        int bb = hp/3;
        hp = hp%3;
        
        int cc = hp/1;
        
        return aa+bb+cc;
    }
}