import java.util.HashMap;
import java.util.Map;

// 완주하지 못한 선수
public class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> count = new HashMap<>();

        for (String name : participant){
            count.putIfAbsent(name, 0);
            count.put(name, count.get(name) + 1);
        }

        // 완주 선수 배열을 순회하며 등장 횟수 제외
        for (String name : completion){
            int v = count.get(name) - 1;
            count.put(name, v);
            if(v == 0) count.remove(name);
        }

        return count.keySet().iterator().next();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String[] input1 = {"mislav", "stanko", "mislav", "ana"};
        String[] input2 = {"stanko", "ana", "mislav"};
        String result = answer.solution(input1, input2);

        System.out.print(result);
    }
}
