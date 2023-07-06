import java.util.HashMap;
import java.util.Map;

// A로 B 만들기
public class Solution {
    // 단어를 Map으로 변환
    private static Map<Character, Integer> toMap(String word){
        Map<Character, Integer> map = new HashMap<>();
        for (char c : word.toCharArray()){
            map.putIfAbsent(c, 0);
            map.put(c, map.get(c) + 1);
        }
        return map;
    }
    public int solution(String before, String after) {
        return toMap(before).equals(toMap(after)) ? 1 : 0;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input1 = "olleh";
        String input2 = "hello";
        int result = answer.solution(input1, input2);

        System.out.print(result);
    }
}
