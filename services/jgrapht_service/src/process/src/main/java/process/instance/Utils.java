package process.instance;

import com.jsoniter.any.Any;
import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.builder.GraphTypeBuilder;
import org.jgrapht.util.SupplierUtil;

import java.util.Optional;

public class Utils {
    public static Graph<Integer, DefaultEdge> constructGraph(Any graphJSON) {
        boolean directed = graphJSON.get("directed").toBoolean();
        boolean multiGraph = graphJSON.get("multigraph").toBoolean();

        Graph<Integer, DefaultEdge> graph;

        if (directed) {
            graph = GraphTypeBuilder
                    .directed().allowingMultipleEdges(true).allowingSelfLoops(true)
                    .vertexSupplier(SupplierUtil.createIntegerSupplier())
                    .edgeSupplier(SupplierUtil.DEFAULT_EDGE_SUPPLIER)
                    .weighted(true).buildGraph();
        } else {
            graph = GraphTypeBuilder
                    .undirected().allowingMultipleEdges(true).allowingSelfLoops(true)
                    .vertexSupplier(SupplierUtil.createIntegerSupplier())
                    .edgeSupplier(SupplierUtil.DEFAULT_EDGE_SUPPLIER)
                    .weighted(true).buildGraph();
        }

        for (Any node: graphJSON.get("nodes").asList()) {
            int id = node.get("id").toInt();

            graph.addVertex(id);
        }

        for (Any node: graphJSON.get("edges").asList()) {
            int source = node.get("source").toInt();
            int target = node.get("target").toInt();
            double weight = Optional.ofNullable(node.get("weight")).map(Any::toDouble).orElse(0.0);

            graph.setEdgeWeight(graph.addEdge(source, target), weight);
        }

        return graph;
    }
}
