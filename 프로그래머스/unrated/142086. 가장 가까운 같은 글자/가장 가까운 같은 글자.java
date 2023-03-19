class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        int tmp=-1;
        for(int i =0;i<s.length();i++){
            tmp = s.lastIndexOf(s.charAt(i) , i-1);
            answer[i] = tmp<0?-1:i-tmp;
        }
        
        return answer;
    }
}