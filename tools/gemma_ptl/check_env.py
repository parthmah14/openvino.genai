#!/usr/bin/env python3
"""PTL readiness check for OpenVINO GenAI repo usage."""

from __future__ import annotations

import json
import sys

import openvino as ov
import openvino_genai


def main() -> int:
    core = ov.Core()
    summary = {
        "python": sys.version.split()[0],
        "openvino": getattr(ov, "__version__", "unknown"),
        "openvino_genai": getattr(openvino_genai, "__version__", "unknown"),
        "available_devices": list(core.available_devices),
        "npu_present": "NPU" in list(core.available_devices),
    }
    print("GEMMA_PTL_GENAI_RESULT=" + json.dumps(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
