# Tooling Strategy: Developer MCPs

To maintain high velocity and spec fidelity, we utilize the following Model Context Protocol (MCP) servers in the development environment:

1. **git-mcp**: 
   - **Purpose**: Enables the AI agent to manage version control, creating meaningful commit messages and branches based on the tasks it completes.
   - **Configuration**: Standard stdio transport; connected to the project root.

2. **filesystem-mcp**:
   - **Purpose**: Allows the agent to read, write, and list files across the directory structure, essential for managing the `/specs` and `/skills` folders.

3. **Tenx MCP Sense**:
   - **Purpose**: Acts as the "Black Box" flight recorder, tracking all agent thinking traces for later verification and debugging.