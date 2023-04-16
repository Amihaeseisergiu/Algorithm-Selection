package process.pubsub;

import org.json.JSONObject;
import process.network.Envelope;

public class AlgorithmsDataPublisher extends Publisher {
    private final String fileId;
    private final String algorithmName;
    private final String algorithmType;
    private final JSONObject envelope;

    public AlgorithmsDataPublisher(String fileId, String algorithmName, String algorithmType) {
        super(System.getenv("DATA_AGGREGATOR_TOPIC"), System.getenv("ALGORITHMS_DATA_KEY"), "topic");
        this.fileId = fileId;
        this.algorithmName = algorithmName;
        this.algorithmType = algorithmType;
        this.envelope = Envelope.sendAlgorithmData(fileId, algorithmName, algorithmType);
    }

    public void send(JSONObject data) {
        envelope.put("payload", data);
        super.send(envelope);
    }
}

