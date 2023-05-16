class Solution {
    public int[] solution(int[] num_list) {
        int length = num_list.length;       
        int[] answer = new int[length + 1];
        for(int i=0;i<length;i++){
            answer[i] = num_list[i];
        }
        answer[length] = 
            answer[length - 1] > answer[length - 2]?
            answer[length - 1] - answer[length-2] : answer[length - 1] * 2;
        return answer; 
    }
}