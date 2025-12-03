# Project Report

## Methods Examined
- `getPythonParseObject`
- `checkIfParsablePython`
- `getFunctionDefinitions`
- `getImport`
- `getFunctionAssignments`

## Activities Done

### Fuzzing
`fuzz.py` was created inside the `FAME_ML` folder to fuzz the five selected methods. Executing this file creates a `fuzz_results.txt` inside the same directory, detailing all of the things found throughout the fuzzing process.

### Forensics
Forensics was implemented locally within all of the methods inside `py_parser.py`. Rather than print to a log file, I decided to just have the logs displayed in the console during execution.

### Continuous Integration
Finally, I created a `dispatch-fuzz.yml` workflow to run the fuzzing file (which inherently tests the logging too). The file for this is uploaded as an artifact inside the GitHub Actions run.

## Lessons Learned
Overall, I learned a lot about implementing both fuzzing and logging, as well as refreshed my memory on GitHub Actions. I struggled a little bit to get used to the current setup—which is probably why it's a good idea to do these things as you go along!