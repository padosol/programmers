import java.util.*;

class Solution {
    
    static Map<String, Integer> book = new HashMap<>();
    static int count = 1;
    public int solution(String word) {
        int answer = 0;
        createBook("", "AEIOU");
        return book.get(word);
    }
    
    
        private static void createBook(String first, String second) {

        if(!first.equals("")){
            if(book.containsKey(first)){
                return;
            }
            book.put(first, count++);
        }

        for(int i=0;i<second.length();i++){
            if(first.length() == second.length()){
                for(int j=1;j<second.length();j++){
                    createBook(first.substring(0,4)+second.charAt(j), "");
                }

            }else{
                createBook(first + second.charAt(i), second);
            }

        }
    }
    
    
}