{
    "targets": [
        {
            "target_name": "control_modifiers",
            "cflags!": ["-fno-exceptions"],
            "cflags_cc!": ["-fno-exceptions"],
            "sources": ["src/lib.cc"],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            'defines': ['NAPI_DISABLE_CPP_EXCEPTIONS'],
            "conditions": [
                ["OS=='win'", {
                "defines": ["BUILD_FOR_WINDOWS"]
                }]
            ]
        }
    ]
}
