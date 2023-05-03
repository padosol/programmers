import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photos) {
        int[] answer = new int[photos.length];
        List<String> list = Arrays.asList(name);
        int j = 0;
        for(String[] photo : photos) {

            for(int i=0;i<photo.length;i++){
                int index = list.indexOf(photo[i]);
                if(index > -1){
                    answer[j] += yearning[index];
                }
            }
            j++;
        }

        return answer;
    }
}