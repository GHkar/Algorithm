import java.util.Arrays;
import java.util.stream.IntStream;

// 모의고사
public class Solution {
    // 각 수포자들의 규칙
    private static final int[][] RULES = {
            {1,2,3,4,5},
            {2,1,2,3,2,4,2,5},
            {3,3,1,1,2,2,4,4,5,5}
    };

    // 문제 번호가 정의해둔 규칙에서 몇 번째인가
    private int getPicked(int person, int problem) {
        int[] rule = RULES[person];
        int index = problem % rule.length;
        return rule[index];
    }

    public int[] solution(int[] answers){
        int[] corrects = new int[3];
        int max = 0;

        for(int problem = 0; problem < answers.length; problem++){
            int answer = answers[problem];

            // 각 수포자별로 정답 개수 세기
            for (int person = 0; person < 3; person++){
                int picked = getPicked(person,problem);
                if (answer == picked){
                    // max 업데이트하기
                    if(++corrects[person] > max){
                        max = corrects[person];
                    }
                }
            }
        }

        // 정답을 가장 많이 맞춘 사람
        final int maxCorrects = max;
        return IntStream.range(0,3)
                .filter(i->corrects[i] == maxCorrects)
                .map(i->i+1)    // 0 기반 인덱스를 1 기반 인덱스로 변환
                .toArray();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[] input = {1,2,3,4,5};
        int[] result = answer.solution(input);

        System.out.print(Arrays.toString(result));
    }
}
