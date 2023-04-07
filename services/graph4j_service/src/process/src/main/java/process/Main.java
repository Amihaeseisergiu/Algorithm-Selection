package process;

import process.algorithm.Algorithm;
import process.algorithm.Algorithms;
import process.instance.Instance;
import process.instance.InstanceRepository;
import process.pubsub.Publisher;
import process.pubsub.SelectorAlgorithmPublisher;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        String instancePath = args[0];
        String algorithmName = args[1];
        String fileId = args[2];
        String socketId = args[3];

        List<Publisher> algorithmPublishers = List.of(
                new SelectorAlgorithmPublisher(fileId, algorithmName)
        );

        Instance instance = InstanceRepository.getInstance(instancePath);
        Algorithm algorithm = Algorithms.getMapping(instance, algorithmPublishers).get(algorithmName);

        algorithm.run();

    }
}