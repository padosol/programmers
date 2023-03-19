import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        char ch = (char)97;
        String[] ss = s.split("");
        String[] strArr = new String[26];
        for(int i=97;i<123;i++){
            strArr[i-97] = String.valueOf((char)i);
        }
        // 최종 리스트 이걸사용해야함
        List<String> strArrList = new ArrayList<String>(Arrays.asList(strArr));

        String[] skips = skip.split("");
        List<String> skipsList = new ArrayList<String>(Arrays.asList(skips));
        for(String item : strArr){
            if(skipsList.contains(item)){
                strArrList.remove(item);
            }
        }

        for(String item : ss){

            int count = strArrList.indexOf(item)+index;
            while(count >= strArrList.size()){
                count -= strArrList.size();
            }

            answer += strArrList.get(count);

        }

        return answer;
    
    }
}