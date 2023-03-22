package process;

import process.algorithm.Algorithm;
import process.algorithm.Algorithms;
import process.instance.Instance;
import process.instance.InstanceRepository;

public class Main {
    public static void main(String[] args) {
        String instancePath = args[0];
        String algorithmName = args[1];

        Instance instance = InstanceRepository.getInstance(instancePath);
        Algorithm algorithm = Algorithms.getMapping(instance).get(algorithmName);

        algorithm.run();
    }
}