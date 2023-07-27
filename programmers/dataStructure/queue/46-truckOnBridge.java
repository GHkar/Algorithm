import java.util.*;

// 다리를 지나는 트럭
public class Solution {
    public int solution(int bridgeLength, int weight, int[] truckWeights) {
        int bridgeWeight = 0;                       // 현재 다리 위 무게
        Queue<Integer> bridge = new LinkedList<>(); // 다리
        int time = 0;                               // 소요된 시간
        int truckIndex = 0;                         // 대기중인 트럭 인덱스

        // 다리를 비움
        for (int i = 0; i < bridgeLength; i++){
            bridge.add(0);
        }

        // 대기 중인 트럭 큐에 넣어주기
        while(truckIndex < truckWeights.length){
            // 트럭 처리
            bridgeWeight -= bridge.poll();
            int truckWeight = truckWeights[truckIndex];
            // 트럭이 올라갈 수 있으면
            if(bridgeWeight + truckWeight <= weight){
                bridge.add(truckWeight);
                bridgeWeight += truckWeight;
                truckIndex++;
            } else{
                bridge.add(0);
            }
            time++;
        }
      
        // 다리를 비울 때까지 트럭을 진행
        while(bridgeWeight > 0){
            bridgeWeight -= bridge.poll();
            time++;
        }
        return time;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int input1 = 2;
        int input2 = 10;
        int[] input3 = {7, 4, 5, 6};
        int result = answer.solution(input1, input2, input3);

        System.out.print(result);
    }
}
