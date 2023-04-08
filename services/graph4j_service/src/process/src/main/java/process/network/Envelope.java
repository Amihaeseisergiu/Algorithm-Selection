package process.network;

import org.json.JSONObject;

public class Envelope {
    private static final String libraryName = System.getenv("LIBRARY_NAME");

    public static String createSelectorEnvelope(String fileId, String algorithmName, String result) {
        return new JSONObject()
                .put("header",
                        new JSONObject()
                                .put("file_id", fileId)
                                .put("algorithm_name", algorithmName)
                                .put("library_name", libraryName)
                )
                .put("payload",
                        new JSONObject()
                                .put("result", result)
                ).toString();
    }
}
