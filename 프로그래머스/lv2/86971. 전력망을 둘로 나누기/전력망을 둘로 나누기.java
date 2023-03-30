import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int min =101;
        for(int i=0;i<wires.length;i++){
            count = 0;
            int num1 = childNodeCount(wires[i][0], i, wires);
            count = 0;
            int num2 = childNodeCount(wires[i][1], i, wires);
            min = min < Math.abs(num1 - num2)?min:Math.abs(num1-num2);
        }

        int answer = min;
        return answer;
    }
    
    
        static int count = 0;
    public static int childNodeCount(int num, int index, int[][] wires){
        for(int i=0;i<wires.length;i++){
            if(i == index)continue;

            int nextNum = wires[i][0] == num?wires[i][1] : wires[i][1] == num? wires[i][0] : 0;

            if(nextNum == 0)continue;

            if(nextNum > 0){
                childNodeCount(nextNum, i, wires);
            }
        }
        return count++;
    }
    
    
}