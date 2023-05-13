class Solution {
    public int solution(String num_str) {
        int answer = 0;
        
        for(String item : num_str.split("")){
            answer += Integer.parseInt(item);
        }
        
        
        return answer;
    }
}