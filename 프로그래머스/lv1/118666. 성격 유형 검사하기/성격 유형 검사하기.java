import java.util.*;
class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        Map<String, Integer> map = new HashMap<>();
        map.put("R", 0);
        map.put("T", 0);
        map.put("C", 0);
        map.put("F", 0);
        map.put("J", 0);
        map.put("M", 0);
        map.put("A", 0);
        map.put("N", 0);

        StringBuilder sb = new StringBuilder();
        for(int i=0;i<survey.length;i++){
            int count = choices[i]-4;
            String item = survey[i].split("")[count > 0?1:0];
            System.out.println(item + " : " + Math.abs(count));
            map.put(item, map.get(item) + Math.abs(count));
        }

        sb.append(map.get("R") >= map.get("T") ? "R" : "T");
        sb.append(map.get("C") >= map.get("F") ? "C" : "F");
        sb.append(map.get("J") >= map.get("M") ? "J" : "M");
        sb.append(map.get("A") >= map.get("N") ? "A" : "N");

        System.out.println(sb.toString());




        return sb.toString();
    }
}