import java.util.*;

// 길 찾기 게임
public class Solution {
    // 노드
    private static class Node {
        public final int value;
        public final int x;
        public final int y;

        public Node left;
        public Node right;

        private Node(int value, int x, int y){
            this.value = value;
            this.x = x;
            this.y = y;
        }
    }

    // 트리 구성 후, 루트 노드를 반환
    private Node constructTree(Node[] nodes){
        Node root = nodes[0];

        // 트리 구성
        for (int i = 1; i < nodes.length; i++){
            insert(root, nodes[i]);
        }
        return root;
    }

    // 트리에 삽입
    private void insert(Node root, Node node){
        // x 좌표에 따라 root 노드가 나타내는 트리에 node 삽입
        if(node.x < root.x){
            if(root.left == null){
                root.left = node;
            }else {
                insert(root.left, node);
            }
        }else{
            if(root.right == null){
                root.right = node;
            }else{
                insert(root.right, node);
            }
        }
    }

    // 전위 순회
    private void pre(Node node, List<Integer> visits){
        if (node == null) return;

        visits.add(node.value);
        pre(node.left, visits);
        pre(node.right, visits);
    }

    // 후위 순회
    private void post(Node node, List<Integer> visits){
        if (node == null) return;

        post(node.left, visits);
        post(node.right, visits);
        visits.add(node.value);
    }

    public int[][] solution(int[][] nodeInfo) {
        Node[] nodes = new Node[nodeInfo.length];
        for(int i = 0; i < nodes.length; i++){
            nodes[i] = new Node(i + 1, nodeInfo[i][0], nodeInfo[i][1]);
        }
        // y 좌표로 내림차순 정렬
        Arrays.sort(nodes, (a, b) -> b.y - a.y);

        Node root = constructTree(nodes);

        List<Integer> preorder = new ArrayList<>();
        pre(root, preorder);

        List<Integer> postorder = new ArrayList<>();
        post(root, postorder);

        return new int[][]{
                preorder.stream().mapToInt(Integer::intValue).toArray(),
                postorder.stream().mapToInt(Integer::intValue).toArray(),
        };
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[][] input = {{5,3},{11,5},{13,3},{3,5},{6,1},{1,3},{8,6},{7,2},{2,2}};
        int[][] result = answer.solution(input);

        System.out.print(Arrays.deepToString(result));
    }
}
