class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int n1 = 0;
        int n2 = 1;
        
        for(int i=0;i<num_list.length;i++){
            n1 += num_list[i];
            n2 *= num_list[i];
        }
        
        n1 *= n1;
        
        
        return n1>n2?1:0;
    }
}