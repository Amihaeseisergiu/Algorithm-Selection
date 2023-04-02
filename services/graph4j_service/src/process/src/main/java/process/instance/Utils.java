package process.instance;

import com.jsoniter.any.Any;
import org.graph4j.Graph;
import org.graph4j.GraphBuilder;

import java.util.Optional;

public class Utils {
    public static Graph constructGraph(Any graphJSON) {
        boolean directed = graphJSON.get("directed").toBoolean();
        boolean multiGraph = graphJSON.get("multigraph").toBoolean();

        int numVertices = graphJSON.get("nodes").size();
        int numEdges = graphJSON.get("edges").size();

        Graph graph;

        if (directed) {
            if (multiGraph) {
                graph = GraphBuilder.empty()
                        .estimatedNumVertices(numVertices).estimatedNumEdges(numEdges)
                        .buildDirectedMultigraph();
            } else {
                graph = GraphBuilder.empty()
                        .estimatedNumVertices(numVertices).estimatedNumEdges(numEdges)
                        .buildDigraph();
            }
        } else {
            if (multiGraph) {
                graph = GraphBuilder.empty()
                        .estimatedNumVertices(numVertices).estimatedNumEdges(numEdges)
                        .buildMultigraph();
            } else {
                graph = GraphBuilder.empty()
                        .estimatedNumVertices(numVertices).estimatedNumEdges(numEdges)
                        .buildGraph();
            }
        }

        for (Any node: graphJSON.get("nodes").asList()) {
            int id = node.get("id").toInt();

            graph.addVertex(id);
        }

        for (Any node: graphJSON.get("edges").asList()) {
            int source = node.get("source").toInt();
            int target = node.get("target").toInt();
            double weight = Optional.ofNullable(node.get("weight")).map(Any::toDouble).orElse(0.0);

            graph.addEdge(source, target);
            graph.setEdgeWeight(source, target, weight);
        }

        return graph;
    }
}
