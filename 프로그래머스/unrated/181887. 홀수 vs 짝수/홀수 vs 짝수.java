class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int n1 = 0;
        int n2 = 0;
        
        for(int i=0;i<num_list.length;i++){
            if( i % 2 == 0) {
                n1 += num_list[i];
            } else {
                n2 += num_list[i];
            }
        }
        
        
        return n1 > n2 ? n1: n2;
    }
}