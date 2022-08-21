package com.seven;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BJ1260 {
    static int[][] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        int V=Integer.parseInt(st.nextToken());
        graph=new int[N][N];

        for(int i=0;i<M;i++){
            st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            graph[a-1][b-1]=1;
            graph[b-1][a-1]=1;
        }

        boolean[] visited=new boolean[N];

        System.out.print(V+" ");
        visited[V-1]=true;
        dfs(graph,N,V-1,visited);
        System.out.println();

        System.out.print(V+" ");
        bfs(graph,N,V-1);
    }

    public static void bfs(int[][] arr,int N,int a){
        Queue<Integer> queue=new LinkedList<>();
        boolean[] visited=new boolean[N];
        queue.offer(a);
        visited[a]=true;

        while(!queue.isEmpty()){
            int tmp=queue.poll();
            for(int i=0;i<N;i++){
                if(visited[i]) continue;

                if(arr[tmp][i]==1){
                    visited[i]=true;
                    queue.offer(i);
                    System.out.print((i+1)+" ");
                }
            }
        }
    }

    public static void dfs(int[][] arr,int N,int a,boolean[] visited){
        for(int i=0;i<N;i++){
            if(arr[a][i]==1){
                if(visited[i]) continue;

                visited[i]=true;
                System.out.print((i+1)+" ");
                dfs(arr,N,i,visited);
            }
        }
    }
}
