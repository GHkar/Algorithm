import java.util.Arrays;

// 카펫
public class Solution {
    public int[] solution(int brown, int yellow){
        for (int width = 3; width <= 5000; width++){
            for (int height = 3; height <= width; height++){
                int boundary = (width + height - 2) * 2;    // 가로 위 아래 2개, 세로는 왼쪽, 오른쪽 2개 (단, 가로의 2개씩 제외)
                int center = width * height - boundary;     // 중간 노란색은, 전체 카펫에서 갈색 바운더리를 제외한 값
                if (brown == boundary && yellow == center) {
                    return new int[] {width, height};
                }
            }
        }
        return null;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int input1 = 10;
        int input2 = 2;
        int[] result = answer.solution(input1, input2);

        System.out.print(Arrays.toString(result));
    }
}
