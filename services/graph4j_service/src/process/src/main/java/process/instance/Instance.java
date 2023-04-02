package process.instance;

import com.jsoniter.any.Any;
import org.graph4j.Graph;

public record Instance(Graph graph, Any parameters) {
}
