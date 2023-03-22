package process.instance;

import com.google.gson.JsonObject;

public record Instance(Boolean directed, Boolean multiGraph, String graph, JsonObject parameters) {
}
