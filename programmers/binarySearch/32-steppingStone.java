import java.util.Arrays;

// 징검다리
/*
*** 바위 n개를 이용하여 특정 거리 d에 대해 모든 지점 사이의 거리가 d 이상이 되는 d 중 가장 큰 값을 구하여라
* 1. 바위 위치를 앞에서부터 순회
* 2. 인접한 바위 사이의 거리를 구하면서 거리가 d보다 작으면 바위를 하나 없앰
* 3. 모두 반복했을 때 없앤 바위 개수가 n보다 같거나 작으면 d는 조건을 만족함
* */
public class Solution {
    private boolean isValid(int d, int[] rocks, int n){
        int removed = 0;    // 제거한 바위 개수
        int last = 0;       // 마지막 바위 위치
        for (int rock : rocks){
            if(rock - last < d){
                removed++;
                continue;
            }
            last = rock;
        }
        return removed <= n;
    }

    public int solution(int distance, int[] rocks, int n) {
        // 이진 탐색 범위 [start, end)
        int start = 1;
        int end = distance + 1;
        // 도착 지점과 마지막 바위 사이의 거리 추가
        rocks = Arrays.copyOf(rocks, rocks.length + 1);
        rocks[rocks.length - 1] = distance;
        Arrays.sort(rocks);

        while(end - start > 1){
            int d = (start + end) / 2;
            // d 조건 검사 후 범위 좁히기
            if(isValid(d, rocks, n)){
                start = d;
            } else{
                end = d;
            }
        }
        return start;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int input1 = 25;
        int[] input2 = {2, 14, 11, 21, 17};
        int input3 = 2;
        int result = answer.solution(input1, input2, input3);

        System.out.print(result);
    }
}
