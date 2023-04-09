package process;

import process.algorithm.Algorithm;
import process.algorithm.Algorithms;
import process.instance.Instance;
import process.instance.InstanceRepository;
import process.pubsub.Publisher;
import process.pubsub.SelectorAlgorithmPublisher;
import process.pubsub.UserInitPublisher;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        String instancePath = args[0];
        String algorithmName = args[1];
        String fileId = args[2];
        String socketId = args[3];
        double start_time = Double.parseDouble(args[4]);

        List<Publisher> algorithmPublishers = List.of(
                new SelectorAlgorithmPublisher(fileId, algorithmName)
        );

        Instance instance = InstanceRepository.getInstance(instancePath);
        Algorithm algorithm = Algorithms.getMapping(instance, algorithmPublishers).get(algorithmName);

        new UserInitPublisher(socketId, algorithmName).send(
                String.valueOf(System.currentTimeMillis() / 1000.0 - start_time));

        algorithm.run();
    }
}