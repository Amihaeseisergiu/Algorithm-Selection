package process.instance;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.builder.GraphTypeBuilder;
import org.jgrapht.nio.json.JSONImporter;
import org.jgrapht.util.SupplierUtil;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.StringReader;

public class InstanceRepository {
    public static Instance getInstance(String instancePath) {
        try {
            Gson gson = new Gson();
            String content = gson.fromJson(new FileReader(instancePath), String.class);
            JsonObject root = JsonParser.parseString(content).getAsJsonObject();

            JsonObject graph = root.get("graph").getAsJsonObject();
            JsonObject parameters = root.get("parameters").getAsJsonObject();

            Boolean directed = graph.get("directed").getAsBoolean();
            Boolean multiGraph = graph.get("multigraph").getAsBoolean();

            return new Instance(directed, multiGraph, graph.toString(), parameters);
        } catch (FileNotFoundException e) {
            return new Instance(false, false, "", null);
        }
    }

    public static Graph<String, DefaultEdge> getGraph(Instance instance) {
        Graph<String, DefaultEdge> graph;

        if (instance.directed()) {
            graph = GraphTypeBuilder
                    .directed().allowingMultipleEdges(instance.multiGraph()).allowingSelfLoops(instance.multiGraph())
                    .weighted(true).vertexSupplier(SupplierUtil.createStringSupplier())
                    .edgeSupplier(SupplierUtil.DEFAULT_EDGE_SUPPLIER).buildGraph();
        } else {
            graph = GraphTypeBuilder
                    .undirected().allowingMultipleEdges(instance.multiGraph()).allowingSelfLoops(instance.multiGraph())
                    .weighted(true).vertexSupplier(SupplierUtil.createStringSupplier())
                    .edgeSupplier(SupplierUtil.DEFAULT_EDGE_SUPPLIER).buildGraph();
        }

        JSONImporter<String, DefaultEdge> importer = new JSONImporter<>();
        importer.importGraph(graph, new StringReader(instance.graph()));

        return graph;
    }
}
