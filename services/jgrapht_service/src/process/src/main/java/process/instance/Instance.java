package process.instance;

import com.jsoniter.any.Any;
import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultEdge;

public record Instance(Graph<Integer, DefaultEdge> graph, Any parameters) {
}
