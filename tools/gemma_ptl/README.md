# Gemma PTL Quick Check (openvino.genai)

## Activate environment

PowerShell:

. C:\path\to\openvino\build-x86_64\install\setupvars.ps1

## Verify runtime availability

python tools/gemma_ptl/check_env.py

This prints package versions and visible devices.

## Optional NPUW logs while running Gemma

$env:OPENVINO_NPUW_LOG_LEVEL="DEBUG"

Then run your Gemma pipeline command on PTL.
