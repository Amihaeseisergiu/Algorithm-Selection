package process.network;

import org.json.JSONObject;

public class Envelope {
    private static final String libraryName = System.getenv("LIBRARY_NAME");

    public static JSONObject sendAlgorithmData(String fileId, String algorithmName, String algorithmType) {
        return new JSONObject()
                .put("header",
                        new JSONObject()
                                .put("file_id", fileId)
                                .put("algorithm_name", algorithmName)
                                .put("algorithm_type", algorithmType)
                                .put("library_name", libraryName)
                );
    }

    public static JSONObject sendUserData(String socketId, String algorithmName) {
        return new JSONObject()
                .put("header",
                        new JSONObject()
                                .put("socket_id", socketId)
                                .put("library_name", libraryName)
                                .put("algorithm_name", algorithmName)
                );
    }
}
