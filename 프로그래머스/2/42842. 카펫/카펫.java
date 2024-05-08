class Solution {
    public int[] solution(int brown, int yellow) {
        // 클수 없다 라는 조건이 있음.
        int[] answer = new int[2];

        for(int i=1;i * i <= yellow; i++) {

            // 사각형이 충족함
            if(yellow % i == 0) {

                int y = i;          // 세로
                int x = yellow / i; // 가로

                int sum = x * 2 + y * 2 + 4 + x * y; // 총 타일 갯수

                if( sum ==  brown + yellow) {
                    answer[0] = x + 2;
                    answer[1] = y + 2;
                    break;
                }
            }
        }

        return answer;
    }
}