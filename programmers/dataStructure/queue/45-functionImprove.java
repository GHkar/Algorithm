import java.util.*;

// 기능 개발
public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // progresses와 speed를 순서대로 참조할 수 있도록 큐에 넣음
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < progresses.length; i++){
            q.add(i);
        }

        List<Integer> result = new ArrayList<>();
        int days = 0;   // 현재 시간
        int count = 0;  // 작업 동시 완료 수
        while(!q.isEmpty()){
            // index번째의 작업 검사
            int index = q.poll();

            // 작업해야하는 일 수 계산
            int expiration = (int) Math.ceil((double) (100 - progresses[index]) / speeds[index]);

            if(expiration > days){
                if(days != 0){
                    result.add(count);
                    count = 0;
                }
                days = expiration;
            }
            count++;
        }
        // 남은 카운트 기록
        result.add(count);
        return result.stream().mapToInt(Integer::intValue).toArray();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[] input1 = {93, 30, 55};
        int[] input2 = {1, 30, 5};
        int[] result = answer.solution(input1, input2);

        System.out.print(Arrays.toString(result));
    }
}
