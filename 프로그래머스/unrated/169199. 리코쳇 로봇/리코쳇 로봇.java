import java.util.*;
class Solution {
    public int solution(String[] board) {
        int answer = 0;
        int x = 1,y = 0;

        int xSize = board[0].length();
        int ySize = board.length;
        Boolean[][] check = new Boolean[ySize][xSize];

        // 우선 배열로 만들었음
        String[][] newBoard = new String[ySize][xSize];
        int[] position = {}; // 좌표를 저장하는 배열
        for(int i =0; i < newBoard.length;i++){
            if(board[i].indexOf("R") > -1){
                position = new int[]{i, board[i].indexOf("R")};
                check[i][board[i].indexOf("R")] = true;  // 현재위치 중복 제거 현재위치에 올 수 있는 최단거리를 확인하기 위해서이다.
            }
            newBoard[i] = board[i].split("");
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.add(position);
        // BFS를 적용하기 위해서
        int[] dx = {0,-1,0,1};
        int[] dy = {1,0,-1,0};
        Boolean is = false;
        while(!queue.isEmpty()) { // queue가 비었을 때 까지 실행
            answer++;
            int queueCycle = queue.size();
            for(int j=0;j<queueCycle;j++){
                if(is)break;

                int[] nowPosition = queue.poll();

                // 좌표를 얻었음 이제 이걸로 상하좌우 계속 달려나가아함
                check[nowPosition[0]][nowPosition[1]] = true;
                for (int i = 0; i < 4; i++) {
                    int tmpX = nowPosition[x];
                    int tmpY = nowPosition[y];

                    Boolean flag = true;
                    while (flag) {
                        tmpX += dx[i];
                        tmpY += dy[i];
                        if (tmpX >= 0 && tmpY >= 0 && tmpX < xSize && tmpY < ySize) {
                            if (newBoard[tmpY][tmpX].equals("D")) {
                                position = new int[]{tmpY - dy[i], tmpX - dx[i]};
                                flag = false;
                            }
                        } else {
                            position = new int[]{tmpY - dy[i], tmpX - dx[i]};
                            flag = false;
                        }
                    }

                    if (check[position[0]][position[1]] == null) { // 비어있는지 확인
                        check[position[0]][position[1]] = true;
                        queue.add(position);
                    }

                    if (newBoard[position[0]][position[1]].equals("G")) {
                        System.out.println(position[0] + " = " + position[1]);
                        is = true;
                        queue.clear();
                        break;
                    }
                }


            }
        }

        return is?answer:-1;
    }
}