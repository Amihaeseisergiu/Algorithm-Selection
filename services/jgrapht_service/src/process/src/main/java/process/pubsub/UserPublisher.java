package process.pubsub;

import org.json.JSONObject;
import process.network.Envelope;

public class UserPublisher extends Publisher {
    private final String socketId;
    private final String algorithmName;
    private final JSONObject envelope;

    public UserPublisher(String socketId, String algorithmName) {
        super(System.getenv("USER_METRICS_TOPIC"), socketId + "_user_metric", "direct");
        this.socketId = socketId;
        this.algorithmName = algorithmName;
        this.envelope = Envelope.sendUserData(socketId, algorithmName);
    }

    public void send(JSONObject data) {
        String eventName = data.getString("event_name");
        JSONObject payload = data.getJSONObject("payload");

        envelope.getJSONObject("header").put("event_name", eventName);
        envelope.put("payload", payload);

        super.send(envelope);
    }
}