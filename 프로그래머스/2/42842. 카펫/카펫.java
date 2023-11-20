class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];

        for(int i=1;i*i<=yellow;i++) {
            if(yellow % i == 0) {

                int first = i;
                int second = yellow / i;

                int sum = first * 2 + second * 2 + 4 + first * second;

                if(sum == yellow + brown) {
                    answer[0] = second + 2;
                    answer[1] = first + 2;
                    break;
                }
            }
        }


        return answer;
    }
}