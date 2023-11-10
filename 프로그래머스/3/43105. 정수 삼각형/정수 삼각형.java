import java.util.Arrays;
class Solution {
    public int solution(int[][] triangle) {
        int[] answer = new int[]{};

        int[][] result = new int[triangle.length][];
        for(int i=0;i< triangle.length;i++) {

            int[] tmp = new int[triangle[i].length];
            Arrays.fill(tmp, 0);

            result[i] = tmp;
        }

        result[0][0] = triangle[0][0];

        for(int i=0;i<triangle.length-1;i++) {

            int[] layer = result[i];
            int[] nextLayer = triangle[i+1];

            for(int j=0;j<layer.length;j++) {
                int first = layer[j] + nextLayer[j];
                int second = layer[j] + nextLayer[j+1];

                // 값이 들어있으면 꺼내서 확인
                int existFirst = result[i+1][j];
                result[i+1][j] = Math.max(existFirst, first);

                int existSecond = result[i+1][j+1];
                result[i+1][j+1] = Math.max(existSecond, second);
            }
        }

        return Arrays.stream(result[triangle.length-1]).max().getAsInt();
    }
}