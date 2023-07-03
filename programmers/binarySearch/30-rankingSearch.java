import java.util.*;
import java.util.function.Consumer;

// 순위 검색
public class Solution {
    // 조건별 리스트 생성
    private Map<String, List<Integer>> buildScoresMap(String[] info){
        // 조건과 해당 조건에 맞는 점수 리스트
        Map<String, List<Integer>> scoresMap = new HashMap<>();

        // 전처리
        for (String s : info){
            String[] tokens = s.split(" ");
            int score = Integer.parseInt(tokens[tokens.length - 1]);
            // scoresMap에 추가
            forEachKey(0, "", tokens, key -> {
                scoresMap.putIfAbsent(key, new ArrayList<>());
                scoresMap.get(key).add(score);
            });
        }

        // 정렬
        for(List<Integer> list : scoresMap.values()){
            Collections.sort(list);
        }

        return scoresMap;
    }

    // 지원자가 만들 수 있는 / 만족하는 모든 조건 찾기
    private void forEachKey(int index, String prefix, String[] tokens, Consumer<String> action) {
        if(index == tokens.length - 1){
            // prefix가 만들어진 검색 조건
            action.accept(prefix);
            return;
        }

        forEachKey(index+1, prefix + tokens[index], tokens, action);
        forEachKey(index+1, prefix + "-", tokens, action);
    }

    // 조건에 맞는 지원자의 수를 세기
    private int count(String query, Map<String, List<Integer>> scoresMap){
        String[] tokens = query.split(" (and )?");
        String key = String.join("", Arrays.copyOf(tokens, tokens.length - 1));

        if (!scoresMap.containsKey(key)) return 0;
        List<Integer> scores = scoresMap.get(key);

        int score = Integer.parseInt(tokens[tokens.length - 1]);

        return scores.size() - binarySearch(score, scoresMap.get(key));
    }

    // 이진 탐색 - 크거나 같은 값 중 가장 작은 값
    private int binarySearch(int score, List<Integer> scores){
        // 이진 탐색으로 인덱스 찾기 [start, end]
        int start = 0;
        int end = scores.size() - 1;

        while(end > start){
            // 중간 값에 따라 범위 좁히기
            int mid = (start + end) / 2;

            if (scores.get(mid) >= score){
                end = mid;
            } else {
                start = mid + 1;
            }
        }

        if (scores.get(start) < score){
            return scores.size();
        }
        return start;
    }

    public int[] solution(String[] info, String[] query) {
        Map<String, List<Integer>> scoresMap = buildScoresMap(info);

        // 정답, 문의 조건 순회
        int[] answer = new int[query.length];
        for(int i = 0; i < answer.length; i++){
            // 정답 구하기
            answer[i] = count(query[i], scoresMap);
        }
        return answer;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String[] input1 = {"java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"};
        String[] input2 = {"java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"};
        int[] result = answer.solution(input1, input2);

        System.out.print(Arrays.toString(result));
    }
}
