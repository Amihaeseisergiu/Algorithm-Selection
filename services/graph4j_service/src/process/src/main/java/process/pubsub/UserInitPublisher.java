package process.pubsub;

import process.network.Envelope;

public class UserInitPublisher extends Publisher {
    private final String socketId;
    private final String algorithmName;

    public UserInitPublisher(String socketId, String algorithmName) {
        super(System.getenv("USER_METRICS_TOPIC"), socketId + "_user_metric", "direct");
        this.socketId = socketId;
        this.algorithmName = algorithmName;
    }

    public void send(String time) {
        String envelope = Envelope.sendUserInitTime(socketId, algorithmName, time);
        super.send(envelope);
    }
}
