import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
class Codility2015Calcium {
    private static class Node {
        int id;
        int longestFromhere;
        int cameras;
        List<Node> children;

        Node(int id) { 
            this.id = id;
        }

        public void addChild(Node node) {
            if(children == null) {
                children = new LinkedList<>();
            }
            children.add(node);
        }

        public boolean isLeaf() {
            return children == null;
        }

        public String toString() { 
            StringBuilder s = new StringBuilder("(");
            s.append(id).append(" path ").append(longestFromhere);
            s.append(" cameras ").append(cameras).append(") -> ");
            if(!this.isLeaf()) {
                for(Node c : children) {
                    s.append(c.id).append(" ");
                }
            }
            return s.toString();
        }
    }

    private static Node[] buildTree(int[] A, int[] B) {
        final int N = A.length;
        Node[] nodes = new Node[N+1];
        List<List<Node>> adjs = new ArrayList<>();
        for(int i=0; i<=N; i++) {
            nodes[i] = new Node(i);
            adjs.add(new LinkedList<Node>());
        }

        for(int i=0; i<A.length; i++) {
            int a = A[i];
            int b = B[i];
            adjs.get(a).add(nodes[b]);
            adjs.get(b).add(nodes[a]);
        }
        boolean[] visited = new boolean[N+1];
        LinkedList<Node> que = new  LinkedList<>();

        que.add(nodes[0]);

        while(!que.isEmpty()) {
            Node node = que.removeFirst();
            visited[node.id] = true;
            for(Node adj : adjs.get(node.id)) {
                if(!visited[adj.id]) {
                    node.addChild(adj);
                    que.add(adj);
                }
            }
        }

        return nodes;
    }

    private static void findCamerasNeed(Node root, int pathLimit) {
        if(root.isLeaf() || pathLimit >= 900) {
            root.cameras = 0;
            root.longestFromhere = 0;
            return;
        }
        int cameras = 0;
        int longest = 0; 
        for(Node c : root.children) {
            findCamerasNeed(c, pathLimit);
            cameras += c.cameras;
            int fromHere = c.longestFromhere + 1;
            if(fromHere > pathLimit) {
                cameras++;
            } else if(fromHere + longest > pathLimit) {
                longest = Math.min(fromHere, longest);
                cameras++;
            } else {
                longest = Math.max(fromHere, longest);
            }
        }
        root.cameras = cameras;
        root.longestFromhere = longest;
    }

    public int solution(int[] A, int[] B, int K) {
        // write your code in Java SE 8
        final int N = A.length;
        if(K >= N) return 0;
        Node[] nodes = buildTree(A,B);
        //cameras[longPath] <= K < cameras[shortPath] 
        int shortPath = 0;
        int longPath = 900;
        while(shortPath+1 < longPath) {
            int midPath = (shortPath + longPath) / 2;
            findCamerasNeed(nodes[0], midPath);
            int midCameras = nodes[0].cameras;
            if(midCameras > K) {
                shortPath = midPath;
            } else {
                longPath = midPath;
            }
        }
        return shortPath + 1;
    }
}
