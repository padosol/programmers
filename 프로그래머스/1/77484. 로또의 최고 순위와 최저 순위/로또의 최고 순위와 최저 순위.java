class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[]{};

        int count = 0;
        int rank = 7;

        for(int j=0;j<lottos.length;j++) {

            if(lottos[j] == 0){
                count++;
                continue;
            }

            for(int i=0;i<win_nums.length;i++) {

                if(lottos[j] == win_nums[i]){
                    rank--;
                }

            }

        }
        
        int high = rank-count==7?6:rank-count;
        int low = rank==7?6:rank;

        return new int[]{high, low};
    }
}