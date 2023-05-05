import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> anserList = new ArrayList<>();
        Map<String, Integer> mapData = new HashMap<>();

        // mapData 에 장르별 총 플레이 횟수 저장함
        for(int i=0; i<genres.length; i++) {
            String key = genres[i];
            if(mapData.containsKey(key)) {
                // 키가 있으면
                mapData.put(key, mapData.get(key) + plays[i]);
            } else {
                // 키가 없으면
                mapData.put(key, plays[i]);
            }
        }
        // 플레이 횟수 많은 순으로 정렬
        List<Map.Entry<String, Integer>> listData = new ArrayList<>(mapData.entrySet());
        Collections.sort(listData, new Comparator<Map.Entry<String, Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                return o2.getValue() - o1.getValue();
            }
        });

        for(Map.Entry<String, Integer> item : listData) {

            List<Integer> index = new ArrayList<>();
            List<Integer> count = new ArrayList<>();

            String key = item.getKey();

            for(int i=0; i<plays.length;i++){
                if( !genres[i].equals(key) ) continue;
                index.add(i);
                count.add(plays[i]);
            }

            int[][] result = new int[index.size()][2];
            for(int i=0;i<index.size();i++){
                result[i][0] = index.get(i);
                result[i][1] = count.get(i);
            }

            Arrays.sort(result, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return o2[1] - o1[1];
                }
            });
            for(int i=0; i<result.length; i++){
                if(i == 2) break;
                anserList.add(result[i][0]);

            }
        }

        return anserList.stream().mapToInt(i -> i).toArray();
    }
}