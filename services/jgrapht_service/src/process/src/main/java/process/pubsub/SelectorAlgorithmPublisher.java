package process.pubsub;

import process.network.Envelope;

public class SelectorAlgorithmPublisher extends Publisher {
    private final String fileId;
    private final String algorithmName;

    public SelectorAlgorithmPublisher(String fileId, String algorithmName) {
        super(System.getenv("SELECTOR_ALGORITHMS_TOPIC"), "", "fanout");
        this.fileId = fileId;
        this.algorithmName = algorithmName;
    }

    public void send(String result) {
        String envelope = Envelope.sendSelectorAlgorithmResult(fileId, algorithmName, result);
        super.send(envelope);
    }
}
