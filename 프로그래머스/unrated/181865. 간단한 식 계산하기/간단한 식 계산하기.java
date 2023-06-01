class Solution {
    public int solution(String binomial) {
        int answer = 0;
        
        String[] str = binomial.split(" ");
        int num1 = Integer.parseInt(str[0]);
        int num2 = Integer.parseInt(str[2]);
        
        switch(str[1]){
            case "*":
                answer = num1 * num2;
                break;
            case "+":
                answer = num1 + num2;
                break;
            case "-":
                answer = num1 - num2;
                break;
        }
        
        return answer;
    }
}