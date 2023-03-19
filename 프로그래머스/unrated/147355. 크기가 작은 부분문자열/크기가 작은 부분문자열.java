
class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int length = p.length();
        for(int i=0;i<t.length() - length+1;i++){
            answer=t.substring(i, length+i).compareTo(p)>0?answer:answer+1;
        }
        return answer;
    }
}