package process.pubsub;

import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.impl.DefaultCredentialsProvider;

public class ConnectionProvider {
    private static final ConnectionFactory connectionFactory = new ConnectionFactory();

    static {
        connectionFactory.setHost("rabbitmq");

        String rabbitmqUser = System.getenv("RABBITMQ_USER");
        String rabbitmqPass = System.getenv("RABBITMQ_PASS");
        connectionFactory.setUsername(rabbitmqUser);
        connectionFactory.setPassword(rabbitmqPass);
    }

    private ConnectionProvider() {}

    public static ConnectionFactory getConnectionFactory() {
        return connectionFactory;
    }
}
