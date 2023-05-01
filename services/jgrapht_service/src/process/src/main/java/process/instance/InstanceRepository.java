package process.instance;

import com.jsoniter.JsonIterator;
import com.jsoniter.any.Any;
import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultEdge;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class InstanceRepository {
    public static Instance getInstance(String instancePath) {
        try {
            String jsonString = JsonIterator.deserialize(Files.readString(Paths.get(instancePath))).toString();
            Any rootJSON = JsonIterator.deserialize(jsonString);
            Any graphJSON = rootJSON.get("graph");
            Any parametersJSON = rootJSON.get("parameters");

            Graph<Integer, DefaultEdge> graph = Utils.constructGraph(graphJSON);

            return new Instance(graph, parametersJSON);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
