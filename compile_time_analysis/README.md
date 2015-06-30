# Time every compilation unit compile time.

When compiling with clang under cmake add `CMAKE_EXPORT_COMPILE_COMMANDS`, which
forces `cmake` to generate a compilation database in json format.  After cmake
invocation (or make) a `compile_command.json` file will be generated.

See `time_compilation.py` for an implementation for measuring time of all
compilation units.
