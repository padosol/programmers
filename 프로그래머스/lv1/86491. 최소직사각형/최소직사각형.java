class Solution {
    public int solution(int[][] sizes) {
        int answer = suffle(sizes);
        return answer;
    }
    
    public int suffle(int[][] sizes){
        int x = 0;
        int y = 0;
        for(int[] item : sizes){
            int tmp=0;
            if(item[0] < item[1]){
                tmp = item[0];
                item[0] = item[1];
                item[1] = tmp;
            }
            x = x < item[0]?item[0] : x;
            y = y < item[1]?item[1] : y;
        }
        return x*y;
    }
}