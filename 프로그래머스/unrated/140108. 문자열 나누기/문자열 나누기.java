class Solution {
    public int solution(String s) {
        int answer = 0;
        char[] ch = s.toCharArray();
        int now = 0;
        int tmp=0;
        for(int i=0;i<s.length();i++){
            tmp = ch[now] == ch[i]?tmp+1:tmp-1;
            if(tmp == 0){
                answer++;
                now=i+1;
            }
        }
        if(tmp != 0){
            answer++;
        }
        
        return answer;
    }
}