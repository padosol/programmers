import java.util.*;

class Solution {
    static boolean flag = true;
    public long solution(int[] sequence) {
        long answer = 0;

        if(sequence.length == 1){
            return Math.abs(sequence[0]);
        }
        List<Long> list = new ArrayList<>();
        Arrays.stream(sequence).mapToLong(x -> x).reduce(0, (i , v) -> {
            if(flag){
                list.add(i + v);
                flag = false;
                return i + v;
            }else{
                list.add(i + (v * -1));
                flag = true;
                return i + (v * -1);
            }
        });
        long max = list.stream().mapToLong(x -> x).max().getAsLong();
        long min = list.stream().mapToLong(x -> x).min().getAsLong();

        if( (max < 0 && min < 0)){
            answer = Math.abs(min);
        }else if( max > 0 && min > 00){
            answer = max;
        }else{
            answer = Math.abs(max-min);
        }

        return answer;
    }
}