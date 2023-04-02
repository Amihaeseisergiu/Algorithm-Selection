package process.algorithm;

import process.instance.Instance;

import java.util.Map;

public abstract class Algorithm {
    protected Instance instance;

    protected Algorithm(Instance instance) {
        this.instance = instance;
    }

    public abstract void run();
}
