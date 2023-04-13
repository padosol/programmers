class Solution {
    public String[] solution(String my_str, int n) {
        int length = my_str.length()%n == 0?my_str.length()/n: my_str.length()/n+1;
        String[] answer = new String[length];
        for(int i=0;i<length -1 ;i++){
            answer[i] = my_str.substring(0, n);
            my_str = my_str.substring(n);
        };
        answer[length-1] = my_str;
        for(String item : answer){
            System.out.println(item);
        }

        return answer;
    }
}