package process.pubsub;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import lombok.RequiredArgsConstructor;
import org.json.JSONObject;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

@RequiredArgsConstructor
public class Publisher {
    private final String topic;
    private final String routingKey;
    private final String exchangeType;

    private void callback(JSONObject message) {
        try(Connection connection = ConnectionProvider.getConnectionFactory().newConnection();
            Channel channel = connection.createChannel()) {
            channel.exchangeDeclare(topic, exchangeType);
            channel.basicPublish(topic, routingKey, null, message.toString().getBytes());
        } catch (IOException | TimeoutException e) {
            throw new RuntimeException(e);
        }
    }

    public void send(JSONObject message) {
        callback(message);
    }
}
