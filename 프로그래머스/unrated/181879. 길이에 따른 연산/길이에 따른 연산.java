class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        
        for(int i=0; i<num_list.length;i++){
                    if( num_list.length >= 11){
            answer+=num_list[i];
            
        }else {
            if(answer == 0) answer = 1;
            answer *= num_list[i];
        }
        }
        

        
        return answer;
    }
}