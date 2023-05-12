import java.util.Arrays;

// 거리두기 확인하기
public class Solution {

    // 방향 (상좌우하) = 반대 방향 인덱스끼리 더하면 3이 됨
    private static final int dx[] = {0, -1, 1, 0};
    private static final int dy[] = {-1, 0, 0, 1};

    // 대기실 자체의 거리두기 검사
    private boolean isDistanced(char[][] room){
        // 대기실의 모든 응시자 위치에 대해 반복
        for(int y = 0; y < room.length; y++){
            for(int x = 0; x < room[y].length; x++) {
                if (room[y][x] != 'P') continue;
                if (!isDistanced(room, x, y)) return false;
            }
        }
        return true;
    }

    // 대기실 응시자[y][x]가 거리두기를 지키는지 검사
    private boolean isDistanced(char[][] room, int x, int y){
        for (int d = 0; d < 4; d++){
            int nx = x + dx[d];
            int ny = y + dy[d];
            if(ny < 0 || ny >= room.length || nx < 0 || nx >= room[ny].length) continue;
            // room[ny][nx]를 통해 다른 응시자에게 도달할 수 있는지 검사
            /*
            - X : 파티션, 다른 응시자에게 도달할 수 없음. 별도의 검사 필요 없음.
            - P : 응시자, 맨해튼 거리 불만족. 거리두기 지켜지지 않음.
            - O : 테이블, 인접한 곳에 다른 응시자가 있다면 거리두기가 지켜지지 않음.
             */
            switch (room[ny][nx]){
                case 'P' : return false;
                case 'O' :
                    // 인접한 곳에 다른 응시자가 있는지 검사
                    if (isNextToVolunteer(room, nx, ny, 3-d)) return false;
                    break;
            }
        }
        return true;
    }

    // exclude 방향을 제외하고 응시자가 존재하는지 검사
    private boolean isNextToVolunteer(char[][] room, int x, int y, int exclude){
        for(int d = 0; d < 4; d++){
            if(d == exclude) continue;

            int nx = x + dx[d];
            int ny = y + dy[d];
            if(ny < 0 || ny >= room.length || nx < 0 || nx >= room[ny].length) continue;
            if (room[ny][nx] == 'P') return true;
        }
        return false;
    }

    public int[] solution(String[][] places){
        int[] answer = new int[places.length];
        for (int i = 0; i < answer.length; i++){
            String[] place = places[i];
            char[][] room = new char[place.length][];
            for (int j = 0; j < room.length; j++){
                room[j] = place[j].toCharArray();
            }
            // 거리두기 검사 후 answer에 기록
            if (isDistanced(room)){
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }

        return answer;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String[][] input =  {{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"}, {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"}, {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"}, {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"}, {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}};
        int[] result = answer.solution(input);

        System.out.print(Arrays.toString(result));
    }
}

