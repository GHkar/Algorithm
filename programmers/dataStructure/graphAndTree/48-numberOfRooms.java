import java.util.*;

// 방의 개수
public class Solution {
    // 좌표 정보를 담은 정점 클래스 vertex
    private static class Vertex {
        public final int x;
        public final int y;
        public final String id;                         // 해당 좌표에 정점이 있는가
        public final Set<String> connectedVertices;     // 연결된 정점들

        public Vertex(int x, int y){
            this.x = x;
            this.y = y;
            this.id = id(x, y);
            this.connectedVertices = new HashSet<>();
        }

        public static String id(int x, int y){
            return String.format("(%d, %d)", x, y);
        }
    }

    private static final int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};
    private static final int[] dy = {-1, -1, 0, 1, 1, 1, 0, -1};
    public int solution(int[] arrows) {
        int count = 0;
        Map<String, Vertex> vertices = new HashMap<>();

        // 원점
        Vertex v = new Vertex(0, 0);
        vertices.put(v.id, v);

        // 입력받은 방향 순회
        for(int d : arrows){
            for(int i = 0; i < 2; i++) {    // 대각선으로 이동 시, 실제로는 두 개의 방을 생성하는 경우(예: 모래 시계 모양)를 위해 이동 로직을 두 번 반복 (정점을 세분화 하는 것)
                int x = v.x + dx[d];
                int y = v.y + dy[d];
                String id = Vertex.id(x, y);

                // 해당 좌표를 방문한 적이 없다면 새로운 정점 객체를 생성 후 넣어 줌
                if (!vertices.containsKey(id)) {
                    vertices.put(id, new Vertex(x, y));
                } else if (!v.connectedVertices.contains(id)) {  // 간선의 존재 유무를 확인하여, 기존 간선이 없다면 새로운 방이 생김
                    count++;
                }

                // 간선 연결 후 새로운 좌표로 이동
                Vertex u = vertices.get(id);
                v.connectedVertices.add(u.id);
                u.connectedVertices.add(v.id);
                v = vertices.get(id);
            }
        }

        return count;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[] input = {6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0};
        int result = answer.solution(input);

        System.out.print(result);
    }
}
