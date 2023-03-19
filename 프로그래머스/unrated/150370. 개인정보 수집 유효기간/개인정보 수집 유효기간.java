import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.logging.SimpleFormatter;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Object> list = new ArrayList<>();
        Date date1 = new Date();
        Calendar calToday = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy.MM.dd");
        try {
            date1 = sdf.parse(today);
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }
        calToday.setTime(date1);

        for(int i=0;i<privacies.length;i++){
            String term = privacies[i].split(" ")[1];
            int count = 0;
            for(String item : terms){
                String[] items = item.split(" ");
                if(items[0].equals(term)) {
                    count = Integer.parseInt(items[1]);
                    break;
                }
            }
            Calendar cal = Calendar.getInstance();

            Date date = null;
            try {
                date = sdf.parse(privacies[i].split(" ")[0]);
            } catch (ParseException e) {
                throw new RuntimeException(e);
            }
            cal.setTime(date);

            cal.add(Calendar.MONTH, count);
            cal.add(Calendar.DATE, -1);
            if(cal.get(Calendar.DATE) > 28){
                cal.set(Calendar.DATE, 28);
            }
            if(cal.before(calToday)){

                list.add(i+1);
            }
        }
        int[] answer = new int[list.size()];
        for(int i=0;i<list.size();i++){
            answer[i] = (Integer) list.get(i);
        }

        return answer;
        
    }    

}