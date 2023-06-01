import java.util.Arrays;

// 쿼드압축 후 개수 세기
public class Solution {

    // 0과 1의 개수를 한 번에 담을 수 있는 클래스
    private static class Count {
        public final int zero;
        public final int one;

        public Count(int zero, int one){
            this.zero = zero;
            this.one = one;
        }

        public Count add(Count other){
            return new Count(zero + other.zero, one + other.one);
        }
    }

    // 재귀 method
    private Count count(int offsetX, int offsetY, int size, int[][] arr){
        int h = size / 2;
        for(int x = offsetX; x < offsetX+size; x++){
            for(int y = offsetY; y < offsetY + size; y++){
                // 원소가 섞여 있는 경우
                if(arr[y][x] != arr[offsetY][offsetX]){
                    return count(offsetX, offsetY, h, arr)
                            .add(count(offsetX + h, offsetY, h, arr))
                            .add(count(offsetX, offsetY + h, h, arr))
                            .add(count(offsetX + h, offsetY + h, h, arr));
                }
            }
        }

        // 모든 원소가 같은 값인 경우
        if(arr[offsetY][offsetX] == 1){
            return new Count(0, 1);
        }
        return new Count(1, 0);
    }
    public int[] solution(int[][] arr){
        Count count = count(0, 0, arr.length, arr);
        return new int[] {count.zero, count.one};

    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[][] input = {{1,1,0,0},{1,0,0,0},{1,0,0,1},{1,1,1,1}};
        int[] result = answer.solution(input);

        System.out.print(Arrays.toString(result));
    }
}
