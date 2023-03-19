class Solution {
    public int[] solution(int m, int n, int startX, int startY, int[][] balls) {
        int[] answer = new int[balls.length];

        for(int i=0;i< balls.length;i++){
            int tmpX;
            int tmpY;
            if(balls[i][0] == startX){
                tmpX = m-balls[i][0] < balls[i][0]?m + (m-balls[i][0]):-balls[i][0];
                tmpY = startY > balls[i][1]?n + (n-balls[i][1]):-balls[i][1];
            }else if(balls[i][1] == startY){
                tmpY = n-balls[i][1] < balls[i][1]?n + (n-balls[i][1]):-balls[i][1];
                tmpX = startX > balls[i][0]?m + (m-balls[i][0]):-balls[i][0];
            }else{
                tmpX = (startX + balls[i][0]) < (m-startX) + (m-balls[i][0])?-balls[i][0]:m+(m-balls[i][0]);
                tmpY = (startY + balls[i][1]) < (n-startY) + (n-balls[i][1])?-balls[i][1]:n+(n-balls[i][1]);
            }
            int res1 = (startX - balls[i][0])*(startX - balls[i][0]) + (startY-tmpY)*(startY-tmpY);
            int res2 = (startX - tmpX)*(startX - tmpX) + (startY-balls[i][1])*(startY-balls[i][1]);
            answer[i] = res1 > res2?res2:res1;
        }


        return answer;
    }
}