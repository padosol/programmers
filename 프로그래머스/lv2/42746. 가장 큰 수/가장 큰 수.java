import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        List<String> numList = new ArrayList<>();
        for(int number : numbers){
            numList.add(String.valueOf(number));
        }

        Collections.sort(numList, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return (o1+ o2).compareTo(o2 + o1);
            }
        });

        StringBuilder sb = new StringBuilder();
        for(int i=numList.size()-1; i > -1; i--){
            sb.append(numList.get(i));
        }
        
        if( Integer.parseInt(numList.get(numList.size()-1)) == 0){
            return "0";
        } else {
            return sb.toString();
        }
    }
}