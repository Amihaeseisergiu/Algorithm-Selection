package process.instance;

import com.jsoniter.any.Any;
import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.builder.GraphTypeBuilder;
import org.jgrapht.util.SupplierUtil;

import java.util.Optional;

public class Utils {
    public static Graph<String, DefaultEdge> constructGraph(Any graphJSON) {
        boolean directed = graphJSON.get("directed").toBoolean();
        boolean multiGraph = graphJSON.get("multigraph").toBoolean();

        Graph<String, DefaultEdge> graph;

        if (directed) {
            graph = GraphTypeBuilder
                    .directed().allowingMultipleEdges(multiGraph).allowingSelfLoops(multiGraph)
                    .vertexSupplier(SupplierUtil.createStringSupplier())
                    .edgeSupplier(SupplierUtil.DEFAULT_EDGE_SUPPLIER)
                    .weighted(true).buildGraph();
        } else {
            graph = GraphTypeBuilder
                    .undirected().allowingMultipleEdges(multiGraph).allowingSelfLoops(multiGraph)
                    .vertexSupplier(SupplierUtil.createStringSupplier())
                    .edgeSupplier(SupplierUtil.DEFAULT_EDGE_SUPPLIER)
                    .weighted(true).buildGraph();
        }

        for (Any node: graphJSON.get("nodes").asList()) {
            String id = node.get("id").toString();

            graph.addVertex(id);
        }

        for (Any node: graphJSON.get("edges").asList()) {
            String source = node.get("source").toString();
            String target = node.get("target").toString();
            double weight = Optional.ofNullable(node.get("weight")).map(Any::toDouble).orElse(0.0);

            graph.setEdgeWeight(graph.addEdge(source, target), weight);
        }

        return graph;
    }
}
