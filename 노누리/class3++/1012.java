import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[][] arr;
    static int N,M;
    static int[][] move={{-1,0},{1,0},{0,1},{0,-1}};
    static int cnt;
    static Queue<int[]> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int T=Integer.parseInt(st.nextToken());

        for(int t=0;t<T;t++){
            cnt=0;
            st=new StringTokenizer(br.readLine());
            M= Integer.parseInt(st.nextToken());
            N= Integer.parseInt(st.nextToken());
            int K= Integer.parseInt(st.nextToken());
            arr=new int[M][N];

            for(int i=0;i<K;i++){
                st=new StringTokenizer(br.readLine());
                int a=Integer.parseInt(st.nextToken());
                int b=Integer.parseInt(st.nextToken());
                arr[a][b]=1;
            }

            queue=new LinkedList<>();
            for(int i=0;i<M;i++){
                for(int j=0;j<N;j++){
                    if(arr[i][j]==1){
                        arr[i][j]=0;
                        int[] tmp={i,j};
                        queue.add(tmp);
                        bfs();
                        cnt++;
                    }
                }
            }
            sb.append(cnt+"\n");
        }
        System.out.print(sb);
    }

    private static void bfs(){
        while(!queue.isEmpty()){
            int[] tmp=queue.poll();
            int x=tmp[0];
            int y=tmp[1];
            for(int i=0;i<4;i++){
                if(x+move[i][0]>=0 && x+move[i][0]<M && y+move[i][1]>=0 && y+move[i][1]<N) {
                    if (arr[x + move[i][0]][y + move[i][1]] == 1) {
                        arr[x + move[i][0]][y + move[i][1]]=0;
                        int[] xy = {x + move[i][0], y + move[i][1]};
                        queue.add(xy);
                    }
                }
            }
        }
    }
}

