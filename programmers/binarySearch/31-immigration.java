// 입국 심사
public class Solution {
    // 주어진 시간 t가 정답 조건을 만족하는지 검사
    // 검사할 시간, 대기자 수, 각 심사관별 심사 소요 시간
    private boolean isValid(long t, int n, int[] times){
        long c = 0;     // 시간 t 동안 처리할 수 있는 최대 심사 개수
        for (int time : times){
            c += t / time;
        }
        return c >= n;
    }

    public long solution(int n, int[] times) {
        // 이진 탐색 범위 [start, end]
        long start = 0;
        long end = 1000000000000000000L;

        while(end > start){
            long t = (start + end) / 2;

            // 정답 검사, 범위 좁히기
            if(isValid(t, n, times)) {
                end = t;
            } else {
                start = t + 1;
            }
        }
        return start;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int input1 = 6;
        int[] input2 = {7, 10};
        long result = answer.solution(input1, input2);

        System.out.print(result);
    }
}
